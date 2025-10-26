# Git PR Helper

**Git PR Helper** is a small DevOps productivity CLI that automates common pull-request and release tasks:
- generate a changelog draft from commit messages
- create a release draft (CHANGELOG.md)
- suggest semantic version bumps (major/minor/patch) based on Conventional Commits
- validate PR title and body against templates
- simple GitHub Actions workflow example included

This project is ready to publish on GitHub and accept sponsorships.

## Features
- `git-pr-helper changelog` — create a changelog draft from commits between two refs
- `git-pr-helper bump` — suggest next semantic version using commit types (feat, fix, BREAKING CHANGE)
- `git-pr-helper validate` — validate PR title/body against a small template
- Minimal dependencies; works as a CLI helper in CI or locally

## Install
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Usage examples
```bash
# Generate changelog from last tag to HEAD
git-pr-helper changelog --from-tag v1.2.0 --to-ref HEAD --out CHANGELOG.md

# Suggest bump (prints 'patch' / 'minor' / 'major')
git-pr-helper bump --from-tag v1.2.0 --to-ref HEAD

# Validate a PR title and body using local files (for CI)
git-pr-helper validate --title "feat: add new API" --body-file pr_body.md
```

## GitHub Actions example
A sample workflow is provided under `.github/workflows/pr-check.yml` to run validations on pull requests.

## Sponsor
If this tool saves you time reviewing PRs and writing release notes, please consider sponsoring the project on GitHub Sponsors.

## License
MIT
