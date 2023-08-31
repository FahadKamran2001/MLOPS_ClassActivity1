from i200983 import fibNum

def test_fibNum():
    assert 0 == fibNum(1)
    assert 1 == fibNum(2)
    assert 1 == fibNum(3)
    assert 2 == fibNum(4)
    assert 3 == fibNum(5)
    assert 5 == fibNum(6)
    assert 8 == fibNum(7)
    assert 13 == fibNum(8)
    assert 21 == fibNum(9)
    assert 34 == fibNum(10)
    assert 55 == fibNum(11)
    assert 89 == fibNum(12)
    assert 144 == fibNum(13)
    