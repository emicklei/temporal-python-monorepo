import tryout_app.main as main_module
from tryout_app.main import format_quote_message, main


def test_format_quote_message(monkeypatch) -> None:
    monkeypatch.setattr(
        main_module,
        "random_scientist_quote",
        lambda: "The important thing is to never stop questioning. - Albert Einstein",
    )

    assert (
        format_quote_message()
        == "Tryout quote: The important thing is to never stop questioning. - Albert Einstein"
    )


def test_main_prints_quote(capsys, monkeypatch) -> None:
    monkeypatch.setattr(
        main_module,
        "random_scientist_quote",
        lambda: "Science and everyday life cannot and should not be separated. - Rosalind Franklin",
    )

    main()
    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == "Tryout quote: Science and everyday life cannot and should not be separated. - Rosalind Franklin"
    )
