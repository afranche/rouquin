import pytest

from rouquin import __version__

from rouquin import Match, ANY
from rouquin.match import NoMatchFound, RegexMatch


def test_simple_match():
    assert (
        Match(
            "My super string",
            ("A super string", False),
            ("MY super string", ""),
            ("My super string", True),
        )
        == True
    )


def test_match_on_any():
    assert (
        Match(
            "My super string",
            ("A super string", False),
            ("MY super string", ""),
            (ANY, True),
        )
        is True
    )


def test_raises():
    with pytest.raises(ValueError):
        Match(
            "Some other super string",
            ("A super string", False),
            ("MY super string", ""),
            ("Some other super string", ValueError("This string it too super for me")),
        )


def test_one_pair_required():
    with pytest.raises(ValueError):
        Match("Some other super string")


def test_wrong_pair_given():
    with pytest.raises(ValueError):
        Match("Some other super string", (1, 2, 3), ("yes", "no"))


def test_keep():
    match_object = Match(
        "Some other super string", ("Some other super string", 1), keep=True
    )
    assert type(match_object) is Match


def test_no_match_found():
    with pytest.raises(NoMatchFound):
        Match(
            "Some other super string",
            ("Some string that will never match", 1),
            keep=True,
        )


def test_match_floats():
    assert Match(1.0001, (1.0001, "Oh hello there!")) == "Oh hello there!"


def test_my_regex():
    assert (
        Match(
            "123-654-897",
            (
                RegexMatch(r"(?P<first_test_regex>\d{3}(| |-)\d{3}(| |-)\d{3})"),
                "First!",
            ),
            (RegexMatch(r"(?P<second_test_regex>\d+(| |-)\d+(| |-)\d+)"), "Second!"),
            (RegexMatch(r"^123")),
            "Third!",
        )
        == "First!"
    )


def test_version():
    assert __version__ == "0.1.0"
