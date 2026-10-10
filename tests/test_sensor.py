from src.sensor import to_celsius

def test_boiling_point():
    assert to_celsius(212) == 100

def test_freezing_point():
    assert to_celsius(32) == 0

