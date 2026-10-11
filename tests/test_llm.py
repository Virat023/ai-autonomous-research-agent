from types import SimpleNamespace

import pytest

from research_agent import llm


def test_generate_response_returns_trimmed_model_response(monkeypatch):
    captured = {}

    def fake_chat(**kwargs):
        captured.update(kwargs)
        return SimpleNamespace(
            message=SimpleNamespace(content="  Local answer. \n")
        )

    monkeypatch.setattr(llm.ollama, "chat", fake_chat)

    result = llm.generate_response("  Explain solar energy.  ")

    assert result == "Local answer."
    assert captured == {
        "model": "llama3.2:3b",
        "messages": [
            {"role": "user", "content": "Explain solar energy."}
        ],
    }


def test_generate_response_rejects_blank_prompt():
    with pytest.raises(ValueError, match="Prompt cannot be blank."):
        llm.generate_response("   ")
