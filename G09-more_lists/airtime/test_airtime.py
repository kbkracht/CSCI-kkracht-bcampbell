import airtime

def test_1():
    assert airtime.airtime(5,[1,2,3,5,6]) == 1

def test_2():
    assert airtime.airtime(5,[1,1,1,1,1]) == 0

def test_3():
    assert airtime.airtime(5,[1,3,4,4,4]) == 1

