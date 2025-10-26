import argparse
from .changelog import generate_changelog
from .bump import suggest_bump
from .validate import validate_pr

def main():
    parser = argparse.ArgumentParser(prog='git-pr-helper')
    sub = parser.add_subparsers(dest='cmd')

    p_ch = sub.add_parser('changelog', help='Generate changelog from commits')
    p_ch.add_argument('--from-tag', required=True)
    p_ch.add_argument('--to-ref', default='HEAD')
    p_ch.add_argument('--out', default='CHANGELOG.md')

    p_bump = sub.add_parser('bump', help='Suggest semantic version bump')
    p_bump.add_argument('--from-tag', required=True)
    p_bump.add_argument('--to-ref', default='HEAD')

    p_val = sub.add_parser('validate', help='Validate PR title/body')
    p_val.add_argument('--title', required=True)
    p_val.add_argument('--body-file', required=False)

    args = parser.parse_args()
    if args.cmd == 'changelog':
        generate_changelog(args.from_tag, args.to_ref, args.out)
    elif args.cmd == 'bump':
        bump = suggest_bump(args.from_tag, args.to_ref)
        print(bump)
    elif args.cmd == 'validate':
        body = None
        if args.body_file:
            with open(args.body_file, 'r', encoding='utf-8') as f:
                body = f.read()
        ok, msg = validate_pr(args.title, body)
        if not ok:
            print('INVALID PR:', msg)
            raise SystemExit(1)
        print('PR valid')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
