import pytest

from rouquin import ANY as _
from rouquin import Match, NoMatchFound, RegexMatcher, __version__


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
            (_, True),
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


def test_regex():
    assert (
        Match(
            "123-654-897",
            (
                RegexMatcher(r"(?P<first_test_regex>\d{3}(| |-)\d{3}(| |-)\d{3})"),
                "First!",
            ),
            (RegexMatcher(r"(?P<second_test_regex>\d+(| |-)\d+(| |-)\d+)"), "Second!"),
            (RegexMatcher(r"^123")),
            "Third!",
        )
        == "First!"
    )


"""
    filename, content = Match(action,
        (TASK_ACTION_EXPORT_TRANSACTIONS, admin_tools.export_transactions(task_info)),
        (TASK_ACTION_EXPORT_GRASSAVOYEORDER, admin_tools.export_grassavoyeorder(task_info)),
        (TASK_ACTION_EXPORT_GRASSAVOYEINVOICE, admin_tools.export_grassavoyeinvoice(task_info)),
    )

    elif action == TASK_ACTION_EXPORT_TRANSACTIONS:
        filename, content = admin_tools.export_transactions(task_info)
    elif action == TASK_ACTION_EXPORT_GRASSAVOYEORDER:
        filename, content = admin_tools.export_grassavoyeorder(task_info)
    elif action == TASK_ACTION_EXPORT_GRASSAVOYEINVOICE:
        filename, content = admin_tools.export_grassavoyeinvoice(task_info)
"""


def test_multiple_match():
    my_first_val = "Oggy"
    my_second_val = "McFrites"

    assert (
        Match(
            (my_first_val, my_second_val),
            (("Albert", "Donovan"), "First!"),
            ((_, _), "Second!"),
        )
        == "Second!"
    )

    with pytest.raises(ValueError):
        Match(
            (my_first_val, my_second_val),
            (
                (RegexMatcher(r"^O\w{3}$"), _),
                ValueError("I'm raising an exception."),
            ),
            (("Oggy", "McFrites"), "Second!"),
        )


def test_version():
    assert __version__ == "0.1.0"
