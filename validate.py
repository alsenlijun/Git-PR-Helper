import re

TITLE_TEMPLATE = re.compile(r'^(feat|fix|docs|chore|perf|refactor)(\(.+\))?:\s.+', re.IGNORECASE)

def validate_pr(title, body=None):
    if not TITLE_TEMPLATE.match(title):
        return False, 'Title does not follow Conventional Commits (e.g. feat: add world)'
    # optional body checks
    if body:
        if len(body.strip()) < 10:
            return False, 'PR body too short'
    return True, 'OK'
