from research_agent import logging_config


def test_configure_logging_uses_info_level_and_format(monkeypatch):
    captured = {}

    def fake_basic_config(**kwargs):
        captured.update(kwargs)

    monkeypatch.setattr(logging_config.logging, "basicConfig", fake_basic_config)

    logging_config.configure_logging()

    assert captured["level"] == logging_config.logging.INFO
    assert captured["format"] == "%(asctime)s %(levelname)s %(name)s: %(message)s"
