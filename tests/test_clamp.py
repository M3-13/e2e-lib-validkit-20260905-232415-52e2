"""Unit-Tests für validkit.clamp.clamp."""

import pytest

from validkit.clamp import clamp


def test_value_within_bounds_is_unchanged() -> None:
    assert clamp(5, 0, 10) == 5


def test_value_below_lower_bound_is_clamped_to_low() -> None:
    assert clamp(-3, 0, 10) == 0


def test_value_above_upper_bound_is_clamped_to_high() -> None:
    assert clamp(15, 0, 10) == 10


def test_value_equal_to_lower_bound() -> None:
    assert clamp(0, 0, 10) == 0


def test_value_equal_to_upper_bound() -> None:
    assert clamp(10, 0, 10) == 10


def test_float_bounds() -> None:
    assert clamp(2.5, 0.0, 10.0) == 2.5
    assert clamp(-1.5, 0.0, 10.0) == 0.0
    assert clamp(11.5, 0.0, 10.0) == 10.0


def test_mixed_int_float_bounds() -> None:
    assert clamp(3, 0.5, 10) == 3
    assert clamp(0.2, 1, 10) == 1


def test_low_greater_than_high_raises_value_error() -> None:
    with pytest.raises(ValueError):
        clamp(1, 5, 0)


@pytest.mark.parametrize(
    "args",
    [
        ("5", 0, 10),
        (5, "0", 10),
        (5, 0, "10"),
        (None, 0, 10),
        (5, None, 10),
        (5, 0, None),
        (True, 0, 10),
    ],
)
def test_wrong_type_raises_value_error(args) -> None:
    with pytest.raises(ValueError):
        clamp(*args)


def test_value_error_message_does_not_contain_inputs() -> None:
    for args in (("5", 0, 10), (1, 5, 0)):
        with pytest.raises(ValueError) as exc_info:
            clamp(*args)
        message = str(exc_info.value)
        for arg in args:
            assert str(arg) not in message
