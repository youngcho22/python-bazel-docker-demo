from fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(5) == [ 0, 1, 1, 2, 3 ]


if __name__ == "__main__":
    import sys
    import pytest

    sys.exit(pytest.main([ "-sv", __file__ ]))
