from research_agent import cli


def test_main_displays_research_report(monkeypatch, capsys):
    monkeypatch.setattr(cli, "configure_logging", lambda: None)
    monkeypatch.setattr("builtins.input", lambda _: "  climate change  ")
    monkeypatch.setattr(
        cli,
        "research_topic",
        lambda topic: "# Research Report: climate change\n\nA finding [1].",
    )

    cli.main()

    assert capsys.readouterr().out.strip() == (
        "# Research Report: climate change\n\nA finding [1]."
    )


def test_main_displays_error_for_blank_topic(monkeypatch, capsys):
    monkeypatch.setattr(cli, "configure_logging", lambda: None)
    monkeypatch.setattr("builtins.input", lambda _: "   ")

    cli.main()

    assert capsys.readouterr().out.strip() == "Error: Topic cannot be blank."