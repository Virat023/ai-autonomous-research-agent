from research_agent import cli


def test_main_displays_and_saves_research_report(monkeypatch, capsys, tmp_path):
    report = "# Research Report: climate change\n\nA finding [1]."

    monkeypatch.setattr(cli, "configure_logging", lambda: None)
    monkeypatch.setattr("builtins.input", lambda _: "  climate change  ")
    monkeypatch.setattr(cli, "research_topic", lambda topic: report)
    monkeypatch.setattr(cli, "REPORTS_DIR", tmp_path)

    cli.main()

    output = capsys.readouterr().out
    assert report in output
    assert "Saved report:" in output

    saved_reports = list(tmp_path.glob("climate-change-*.md"))
    assert len(saved_reports) == 1
    assert saved_reports[0].read_text(encoding="utf-8") == report


def test_main_displays_error_for_blank_topic(monkeypatch, capsys):
    monkeypatch.setattr(cli, "configure_logging", lambda: None)
    monkeypatch.setattr("builtins.input", lambda _: "   ")

    cli.main()

    assert capsys.readouterr().out.strip() == "Error: Topic cannot be blank."