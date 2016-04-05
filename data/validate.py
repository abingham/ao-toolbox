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

from collections import Counter, deque
import sys

import yaml


SEEKING_KEY = 0
HAVE_KEY = 1


def _classifications(events, path):
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
    yield from _classifications(events, deque())


def validate(stream):
    all_classifications = list(classifications(yaml.parse(stream)))

    paths = Counter(c[0] for c in all_classifications)
    for k in [k for k, v in paths.items() if v > 1]:
        yield 'duplicated code: {}'.format(k)

    codes = Counter('/'.join(c[1]) for c in all_classifications)
    for k in [k for k, v in codes.items() if v > 1]:
        yield 'duplicate path: {}'.format(k)


if __name__ == '__main__':
    path = sys.argv[1]
    with open(path, 'r') as f:
        for error in validate(f):
            print(error)
