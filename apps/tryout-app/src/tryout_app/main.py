from quotes import random_scientist_quote


def format_quote_message() -> str:
    return f"Tryout quote: {random_scientist_quote()}"


def main() -> None:
    print(format_quote_message())


if __name__ == "__main__":
    main()
