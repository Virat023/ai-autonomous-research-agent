import pytest

from research_agent.topic import validate_topic


def test_validate_topic_removes_extra_spaces():
    assert validate_topic("  climate change  ") == "climate change"


def test_validate_topic_rejects_blank_text():
    with pytest.raises(ValueError, match="Topic cannot be blank."):
        validate_topic("   ")
