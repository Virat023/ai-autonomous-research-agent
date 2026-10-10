from research_agent.cli import main


def test_main_displays_cleaned_topic(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "  climate change  ")

    main()

    assert capsys.readouterr().out.strip() == "Research topic: climate change"


def test_main_displays_error_for_blank_topic(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "   ")

    main()

    assert capsys.readouterr().out.strip() == "Error: Topic cannot be blank."
