#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


class PytestTestRunner:
    """Runs pytest to discover and run test_app.

    https://pytest-django.readthedocs.io/en/latest/faq.html
    """

    def __init__(self, verbosity=1, failfast=False, keepdb=False, **kwargs):
        self.verbosity = verbosity
        self.failfast = failfast
        self.keepdb = keepdb

    def run_tests(self, test_labels):
        """Run pytest and return the exitcode.

        It translates some of Django's test command option to pytest's.
        """
        import pytest

        argv = []
        if self.verbosity == 0:
            argv.append('--quiet')
        if self.verbosity == 2:
            argv.append('--verbose')
        if self.verbosity == 3:
            argv.append('-vv')
        if self.failfast:
            argv.append('--exitfirst')
        if self.keepdb:
            argv.append('--reuse-db')

        argv.extend(test_labels)
        return pytest.main(argv)


"""test runner without using pytest

deprecated unless you like this way.
see https://docs.djangoproject.com/ja/3.0/topics/testing/advanced/
"""
if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["test_app"])
    sys.exit(bool(failures))
