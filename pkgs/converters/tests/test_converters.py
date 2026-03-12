from converters import DegreesToFahrenheit


def test_degrees_to_fahrenheit() -> None:
    assert DegreesToFahrenheit(24) == 75.2
