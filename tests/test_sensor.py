from src.sensor import to_celsius

def test_boiling_point():
    assert to_celsius(212) == 100

def test_freezing_point():
    assert to_celsius(32) == 0

def test_room_temperature():
    assert to_celsius(68) == 20

def test_hot_weather():
    assert to_celsius(86) == 30
