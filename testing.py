from numpy.ma.testutils import assert_almost_equal

import goldbach as gldbch


def test_is_prime_1():
    assert gldbch.is_prime(3) is True


def test_is_prime_2():
    assert gldbch.is_prime(9) is False


def test_get_circle_area_1():
    assert_almost_equal(153.93, gldbch.get_circle_area(7), decimal=1)
