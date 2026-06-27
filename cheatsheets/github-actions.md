# GitHub Actions Cheat Sheet

## Workflow structure

```yaml
name: CI                          # shown in GitHub UI

on:                               # triggers
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  job-name:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - name: My step
        run: echo "hello"
```

---

## Job dependencies

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps: [...]

  test:
    needs: lint           # waits for lint to pass before starting
    runs-on: ubuntu-latest
    steps: [...]
```

---

## Matrix builds — run one job across multiple values

```yaml
strategy:
  fail-fast: false        # run all matrix variants even if one fails
  matrix:
    python-version: ["3.11", "3.12", "3.13"]

steps:
  - uses: actions/setup-python@v6
    with:
      python-version: ${{ matrix.python-version }}  # substituted per run
```

---

## Secrets — encrypted values stored in GitHub

**Why:** Credentials in YAML are visible in your repo forever (git history).
GitHub's secrets store is encrypted at rest, masked in logs, and never
exposed to forks. The right place for API keys, tokens, and passwords.

**How to add a secret:**
Settings → Secrets and variables → Actions → New repository secret

**How to use in a workflow:**
```yaml
jobs:
  my-job:
    runs-on: ubuntu-latest
    env:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}  # injected at runtime
    steps:
      - run: python my_script.py   # script can read ANTHROPIC_API_KEY from os.environ
```

**Rules:**
- Secret values are masked in logs — GitHub replaces them with `***`
- Never echoed, never available in PRs from forks (security boundary)
- Access syntax: `${{ secrets.YOUR_SECRET_NAME }}`

---

## Environment variables — three scopes

```yaml
# Workflow-level: available to ALL jobs
env:
  LOG_LEVEL: debug

jobs:
  build:
    # Job-level: available to all steps in this job
    env:
      CACHE_DIR: /tmp/cache

    steps:
      - name: My step
        # Step-level: available only to this step
        env:
          STEP_VAR: hello
        run: echo $STEP_VAR
```

**Precedence:** step > job > workflow (narrower scope wins)

---

## Common actions

| Action                   | What it does                         |
|--------------------------|--------------------------------------|
| `actions/checkout@v5`    | Clone the repo into the runner       |
| `actions/setup-python@v6`| Install Python + add to PATH         |
| `actions/setup-node@v4`  | Install Node.js                      |
| `actions/cache@v4`       | Cache directories between runs       |

---

## Template expressions

```yaml
${{ secrets.NAME }}              # secret value
${{ matrix.python-version }}     # matrix variable
${{ github.sha }}                # current commit SHA
${{ github.ref }}                # branch/tag ref (refs/heads/main)
${{ github.event_name }}         # push / pull_request / etc.
```

---

## Quick anatomy

```
.github/
  workflows/
    ci.yml       ← one file = one workflow (can have many)
```
