from src.sensor import to_celsius, to_kelvin

def test_boiling_point():
    assert to_celsius(212) == 100

def test_freezing_point():
    assert to_celsius(32) == 0

def test_body_temperature():
    assert to_celsius(98.6) == 37

def test_kelvin():
    assert to_kelvin(0) == 273.15
    
