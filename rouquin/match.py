import cmath
import re
from typing import Iterable

from .constants import ANY
from .matchers import RegexMatcher


class NoMatchFound(Exception):
    pass


def _process(pattern, match):
    if match is ANY:
        return True
    if isinstance(match, RegexMatcher):
        return bool(re.match(match, pattern))
    if all(
        True if isinstance(i, float) else False for i in (pattern, match)
    ) and cmath.isclose(match, pattern):
        return True
    if match == pattern:
        return True
    return False


class Match:
    def _match(self):
        # Would be a very strange error but nevertheless...
        assert isinstance(
            self._match_pairs, Iterable
        ), "The given match pairs can not be looped on."

        for match, result in self._match_pairs:
            # TL;DR: If both the pattern and match object are list or tuples, attempt to match each items of those two
            # lists (all need to match). If the previous conditions did not succeed or if it does not match, compare
            # the match object and pattern object.

            if (
                isinstance(match, (list, tuple))
                and isinstance(self._pattern, (list, tuple))
                and len(self._pattern) == len(match)
                and all(_process(p, m) for p, m in zip(self._pattern, match))
            ) or _process(self._pattern, match):
                if isinstance(result, Exception):
                    raise result
                return result
        raise NoMatchFound

    def __init__(self, pattern, *args, **kwargs):
        if not args:
            raise ValueError("At least one match pair must be given.")
        if any(isinstance(pair, (list, tuple)) and len(pair) != 2 for pair in args):
            raise ValueError("Invalid pair was passed.")

        self._pattern = pattern
        self._match_pairs = args
        self._match_result = None

        if not kwargs.get("lazy", False):
            self._match()

    @property
    def match(self):
        return self._match()

    def __new__(cls, pattern, *args, lazy=False, **kwargs):
        inst = super(Match, cls).__new__(cls)
        inst.__init__(pattern, lazy=lazy, *args)

        return inst if "keep" in kwargs and kwargs["keep"] else inst.match
