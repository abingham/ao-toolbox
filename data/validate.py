# Basic validation of AO YAML data files.
#
# It checks for things like:
#  - correct parsing of the data files
#  - duplicate codes
#  - duplicate branch paths
#
# Run the script like this:
#
#    python validate.py <yaml file>
#
# It will print any errors it sees. If it doesn't print anything, then
# everything is OK with the file.
#
# This also includes a few simple unittests. To run them, use:
#
#   python -m unittest validate.py

from collections import Counter, deque
import sys
import unittest

import yaml


# These are used for state tracking in event processing.
SEEKING_KEY = 0
HAVE_KEY = 1


def _classifications(events, path):
    "Implementation detail of event processing."
    state = SEEKING_KEY
    for event in events:
        if isinstance(event, yaml.MappingStartEvent):
            yield from _classifications(events, path)
            if state == HAVE_KEY:
                path.pop()
                state = SEEKING_KEY
        elif isinstance(event, yaml.MappingEndEvent):
            return
        elif isinstance(event, yaml.ScalarEvent):
            if state == SEEKING_KEY:
                path.append(event.value)
                state = HAVE_KEY
            else:
                yield (event.value, list(path))
                path.pop()
                state = SEEKING_KEY


def classifications(events, path=None):
    "Produce sequence of `(code, path)` tuples from YAML parsing events."
    yield from _classifications(events, deque())


def validate(stream):
    """Validate a stream of YAML AO classifications.

    This produces a sequence of strings, one for each error (i.e. duplicated
    path or code) in the stream. Also, if the YAML can't be parsed for some
    reason, the exception from the YAML parser is propagated out.

    """
    all_classifications = list(classifications(yaml.parse(stream)))

    paths = Counter(c[0] for c in all_classifications)
    for k in [k for k, v in paths.items() if v > 1]:
        yield 'duplicate code: {}'.format(k)

    codes = Counter('/'.join(c[1]) for c in all_classifications)
    for k in [k for k, v in codes.items() if v > 1]:
        yield 'duplicate path: {}'.format(k)


class ValidateTests(unittest.TestCase):
    def test_no_errors(self):
        stream = """
foo:
  bar:
    baz: 1
  fnord:
    fjord: 2
"""
        self.assertListEqual(
            list(validate(stream)),
            [])

    def test_duplicate_path(self):
        stream = """
foo:
  bar:
    baz: 1
  bar:
    baz: 2
"""
        self.assertListEqual(
            list(validate(stream)),
            ['duplicate path: foo/bar/baz'])

    def test_duplicate_code(self):
        stream = """
foo:
  bar: 1
  baz:
    fnord: 1
"""
        self.assertListEqual(
            list(validate(stream)),
            ['duplicate code: 1'])

if __name__ == '__main__':
    path = sys.argv[1]
    with open(path, 'r') as f:
        for error in validate(f):
            print(error)
