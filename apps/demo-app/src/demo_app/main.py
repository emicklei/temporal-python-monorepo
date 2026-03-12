from converters import DegreesToFahrenheit
from quotes import random_scientist_quote


def format_conversion_message(degrees_celsius: float) -> str:
    fahrenheit = DegreesToFahrenheit(degrees_celsius)
    return f"{degrees_celsius} degrees Celsius is {fahrenheit} Fahrenheit"


def format_scientist_quote_message() -> str:
    quote = random_scientist_quote()
    return f"Scientist quote: {quote}"


def main() -> None:
    print(format_conversion_message(24))
    print(format_scientist_quote_message())


if __name__ == "__main__":
    main()
