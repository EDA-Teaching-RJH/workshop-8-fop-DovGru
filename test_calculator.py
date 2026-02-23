from calculator import square

def test_square():
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")