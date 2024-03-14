import goldbach as gldbch


def test_is_prime_1():
    assert gldbch.is_prime(3) is True


def test_is_prime_2():
    assert gldbch.is_prime(9) is False

