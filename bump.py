from git import Repo
import re
import semver

def parse_commit_type(msg):
    m = re.match(r'(?P<type>\w+)(?:\([^)]+\))?:', msg)
    return m.group('type') if m else None

def suggest_bump(from_tag, to_ref='HEAD'):
    repo = Repo('.')
    commits = list(repo.iter_commits(f'{from_tag}..{to_ref}'))
    level = 0  # 0 patch, 1 minor, 2 major
    for c in commits:
        msg = c.message.splitlines()[0]
        if 'BREAKING CHANGE' in c.message or 'BREAKING-CHANGE' in c.message:
            level = max(level, 2)
            continue
        t = parse_commit_type(msg)
        if t == 'feat':
            level = max(level, 1)
        elif t == 'fix' and level < 1:
            level = max(level, 0)
    try:
        cur = semver.VersionInfo.parse(from_tag.lstrip('v'))
    except Exception:
        cur = semver.VersionInfo.parse('0.0.0')
    if level == 2:
        nextv = cur.bump_major()
    elif level == 1:
        nextv = cur.bump_minor()
    else:
        nextv = cur.bump_patch()
    return str(nextv)
