import pytest


class GitHUbIssue:
    @pytest.fixture()
    def go_to_github_issue(self, selenium):
        selenium.get("https://github.com/microsoft/vscode/issues")
