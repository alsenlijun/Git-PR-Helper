from git import Repo
import re

CONVENTIONAL_TYPES = {
    'feat': 'Features',
    'fix': 'Bug Fixes',
    'perf': 'Performance Improvements',
    'docs': 'Documentation',
    'refactor': 'Refactor',
    'test': 'Tests',
    'chore': 'Chore'
}

def parse_commit_message(msg):
    # naive conventional commit parser
    # examples: "feat(scope): description" or "fix: description"
    m = re.match(r'(?P<type>\w+)(?:\([^)]+\))?:\s*(?P<desc>.+)', msg)
    if m:
        return m.group('type'), m.group('desc')
    return None, msg

def generate_changelog(from_tag, to_ref='HEAD', out='CHANGELOG.md'):
    repo = Repo('.')
    commits = list(repo.iter_commits(f'{from_tag}..{to_ref}'))
    sections = {}
    for c in reversed(commits):
        t, d = parse_commit_message(c.message.splitlines()[0])
        section = CONVENTIONAL_TYPES.get(t, 'Other Changes')
        sections.setdefault(section, []).append(f'- {d} ({c.hexsha[:7]})')
    parts = []
    parts.append(f'# Changelog\n\nChanges since {from_tag}\n')
    for sec, items in sections.items():
        parts.append(f'## {sec}\n')
        parts.extend(items)
        parts.append('\n')
    text = '\n'.join(parts)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(text)
    print('Wrote changelog to', out)
