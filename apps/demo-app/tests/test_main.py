import demo_app.main as main_module
from demo_app.main import format_conversion_message, format_scientist_quote_message, main


def test_format_conversion_message() -> None:
    assert format_conversion_message(24) == "24 degrees Celsius is 75.2 Fahrenheit"


def test_format_scientist_quote_message(monkeypatch) -> None:
    monkeypatch.setattr(
        main_module,
        "random_scientist_quote",
        lambda: "Somewhere, something incredible is waiting to be known. - Carl Sagan",
    )

    assert (
        format_scientist_quote_message()
        == "Scientist quote: Somewhere, something incredible is waiting to be known. - Carl Sagan"
    )


def test_main_prints_conversion_and_quote(capsys, monkeypatch) -> None:
    monkeypatch.setattr(
        main_module,
        "random_scientist_quote",
        lambda: "Nothing in life is to be feared, it is only to be understood. - Marie Curie",
    )

    main()
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == [
        "24 degrees Celsius is 75.2 Fahrenheit",
        "Scientist quote: Nothing in life is to be feared, it is only to be understood. - Marie Curie",
    ]
