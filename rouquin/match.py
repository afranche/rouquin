from .constants import ANY

from typing import Iterable

import cmath
import re


class RegexMatch(str):
    pass


class NoMatchFound(Exception):
    pass


class Match:
    def _match(self):
        # Would be a very strange error but nevertheless...
        assert isinstance(
            self._match_pairs, Iterable
        ), "The given match pairs can not be looped on."

        for match, result in self._match_pairs:
            if match is ANY:
                return result
            if isinstance(result, Exception):
                raise result
            if isinstance(match, RegexMatch):
                if re.match(match, self._pattern):  # Let re raise if the given regex is invalid
                    return result
            if all(
                True if isinstance(i, float) else False for i in (self._pattern, match)
            ) and cmath.isclose(match, self._pattern):
                return result
            if match == self._pattern:
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
