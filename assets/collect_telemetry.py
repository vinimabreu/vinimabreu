"""Collect the public numbers the mission console shows, and write them to telemetry.json.

    python3 assets/collect_telemetry.py

Everything here is public and re-checkable: the repo list from the GitHub API,
the test count each README states, and the latest article from the DEV API.
Standard library only, so the daily workflow needs no install step. A repo
whose README states no test count is listed with tests = null and is not
added to the total; nothing is estimated.
"""

from __future__ import annotations

import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
USER = "vinimabreu"
# Not projects: the profile itself and two placeholder repos.
SKIP = {USER, "-", "minikube-prt-replica"}
# The flagships, in the order the README shows them.
FLAGSHIPS = ["revenue-loop", "sequence-gate", "tenant-fence", "langgraph-production", "taint-trail", "betorskip"]

TEST_PATTERNS = (
    re.compile(r"tests?-(\d[\d,]*)(?:%20passing)?-", re.I),          # shields badge
    re.compile(r"(\d[\d,]*)\s+(?:deterministic\s+|passing\s+|automated\s+)?tests\b", re.I),
)


def get(url: str, token: str | None = None) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": f"{USER}-profile-telemetry"})
    if token and "api.github.com" in url:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def stated_tests(readme: str) -> int | None:
    for pattern in TEST_PATTERNS:
        match = pattern.search(readme)
        if match:
            return int(match.group(1).replace(",", ""))
    return None


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN")
    repos = json.loads(get(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner", token))
    projects = []
    for repo in repos:
        if repo["fork"] or repo["private"] or repo["name"] in SKIP:
            continue
        try:
            readme = get(f"https://raw.githubusercontent.com/{USER}/{repo['name']}/{repo['default_branch']}/README.md").decode("utf-8", "replace")
        except Exception:
            readme = ""
        projects.append({
            "name": repo["name"],
            "created": repo["created_at"][:10],
            "pushed": repo["pushed_at"][:10],
            "description": repo["description"] or "",
            "tests": stated_tests(readme),
        })
    projects.sort(key=lambda p: p["created"], reverse=True)
    # CI state of each flagship: the conclusion of its latest finished workflow run.
    for project in projects:
        if project["name"] not in FLAGSHIPS:
            continue
        try:
            runs = json.loads(get(f"https://api.github.com/repos/{USER}/{project['name']}/actions/runs"
                                  f"?per_page=5&status=completed", token))["workflow_runs"]
            project["ci"] = runs[0]["conclusion"] if runs else None
        except Exception:
            project["ci"] = None
    articles = json.loads(get(f"https://dev.to/api/articles?username={USER}&per_page=1000"))
    latest = articles[0] if articles else None
    data = {
        "collected": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "projects": projects,
        "project_count": len(projects),
        "tests_total": sum(p["tests"] for p in projects if p["tests"]),
        "repos_with_tests": sum(1 for p in projects if p["tests"]),
        "last_launch": projects[0]["name"] if projects else None,
        "last_launch_date": projects[0]["created"] if projects else None,
        "articles_published": len(articles),
        "latest_article": {"title": latest["title"], "date": latest["published_at"][:10], "url": latest["url"]} if latest else None,
        "flagships": FLAGSHIPS,
    }
    (HERE / "telemetry.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{data['project_count']} projects, {data['tests_total']} tests stated in {data['repos_with_tests']} READMEs, "
          f"last launch {data['last_launch']} ({data['last_launch_date']})")


if __name__ == "__main__":
    main()
