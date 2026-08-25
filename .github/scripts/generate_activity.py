import json
import os
import urllib.request
from datetime import datetime, timezone
from collections import Counter, defaultdict

USER = os.environ.get("GITHUB_USER", "FerrariForever95")
TOKEN = os.environ["GITHUB_TOKEN"]
OUT = "assets/github-activity.svg"

query = """
query($login:String!) {
  user(login:$login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { date contributionCount }
        }
      }
      commitContributionsByRepository(maxRepositories: 100) {
        repository { name }
        contributions(first: 100) { totalCount }
      }
    }
    repositories(first: 100, ownerAffiliations: OWNER, privacy: PUBLIC) {
      totalCount
    }
  }
}
"""

payload = json.dumps({"query": query, "variables": {"login": USER}}).encode()
req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=payload,
    headers={
        "Authorization": f"bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": USER,
    },
)

with urllib.request.urlopen(req) as response:
    data = json.load(response)

user = data["data"]["user"]
calendar = user["contributionsCollection"]["contributionCalendar"]
days = [d for w in calendar["weeks"] for d in w["contributionDays"]]
total = calendar["totalContributions"]

months = Counter()
for day in days:
    months[day["date"][:7]] += day["contributionCount"]

active_days = sum(1 for d in days if d["contributionCount"] > 0)
longest = current = 0
for d in days:
    if d["contributionCount"] > 0:
        current += 1
        longest = max(longest, current)
    else:
        current = 0

repos = user["contributionsCollection"]["commitContributionsByRepository"]
repo_count = sum(1 for r in repos if r["contributions"]["totalCount"] > 0)

last_12 = sorted(months.items())[-12:]
max_month = max((v for _, v in last_12), default=1)

W, H = 1000, 500
svg = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="1000" height="500" rx="24" fill="#0d1117"/>
<rect x="1" y="1" width="998" height="498" rx="23" fill="none" stroke="#30363d"/>
<style>
.title{{font:700 25px system-ui,sans-serif;fill:#e6edf3}}
.label{{font:600 12px system-ui,sans-serif;fill:#8b949e;letter-spacing:1.4px}}
.value{{font:700 30px system-ui,sans-serif;fill:#e6edf3}}
.month{{font:600 12px system-ui,sans-serif;fill:#8b949e}}
.small{{font:500 11px system-ui,sans-serif;fill:#6e7681}}
</style>
<text x="42" y="48" class="title">GITHUB ACTIVITY / TELEMETRY</text>
<text x="42" y="70" class="small">FerrariForever95 · contribution history</text>
''']

stats = [("CONTRIBUTIONS", total), ("ACTIVE DAYS", active_days), ("LONGEST RUN", longest), ("REPOSITORIES", repo_count)]
for i, (label, value) in enumerate(stats):
    x = 42 + i * 235
    svg.append(f'<text x="{x}" y="108" class="label">{label}</text>')
    svg.append(f'<text x="{x}" y="142" class="value">{value:,}</text>')

svg.append('<line x1="42" y1="168" x2="958" y2="168" stroke="#21262d"/>')
svg.append('<text x="42" y="198" class="label">MONTHLY COMMIT ACTIVITY</text>')

base_y = 395
chart_x = 60
bar_w = 58
gap = 16
for i, (month, count) in enumerate(last_12):
    x = chart_x + i * (bar_w + gap)
    h = 150 * count / max_month if max_month else 0
    y = base_y - h
    svg.append(f'<rect x="{x}" y="{y:.1f}" width="{bar_w}" height="{h:.1f}" rx="7" fill="#238636" opacity="0.9"/>')
    svg.append(f'<text x="{x + bar_w/2}" y="{base_y + 24}" text-anchor="middle" class="month">{month[5:]}</text>')
    svg.append(f'<text x="{x + bar_w/2}" y="{max(y - 8, 225):.1f}" text-anchor="middle" class="small">{count}</text>')

svg.append('<text x="42" y="455" class="small">BUILD  →  COMMIT  →  TEST  →  DEBUG  →  REPEAT</text>')
svg.append('<text x="958" y="455" text-anchor="end" class="small">Updated automatically</text>')
svg.append('</svg>')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))
