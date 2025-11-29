# tests/test_simplemathglh.py

import simplemathglh as sm


def test_numberplus():
    assert sm.numberplus(1, 2) == 3


def test_numberminus():
    assert sm.numberminus(5, 3) == 2


def test_numbermultiply():
    assert sm.numbermultiply(4, 3) == 12


def test_numberdivision():
    assert sm.numberdivision(10, 2) == 5


def test_numbermod():
    # 10 = 3 * 3 + 1
    assert sm.numbermod(10, 3) == 1
