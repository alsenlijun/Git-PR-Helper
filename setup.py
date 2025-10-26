from setuptools import setup, find_packages

setup(
    name="git-pr-helper",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "git-pr-helper=git_pr_helper.cli:main",
        ]
    },
    install_requires=[
        "gitpython>=3.1.0",
        "semver>=2.13.0"
    ]
)
