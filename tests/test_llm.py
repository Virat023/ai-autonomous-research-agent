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
        "model": "qwen3:4b",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a source-grounded research assistant. "
                    "Use only the supplied sources. "
                    "Return exactly two sentences, with no heading or bullet list. "
                    "Put a citation such as [1] at the end of every factual "
                    "sentence, using only the source numbers provided. "
                    "If you cannot follow these rules, return: INSUFFICIENT EVIDENCE"
                ),
            },
            {"role": "user", "content": "Explain solar energy."},
        ],
        "options": {"temperature": 0},
    }


def test_generate_response_rejects_blank_prompt():
    with pytest.raises(ValueError, match="Prompt cannot be blank."):
        llm.generate_response("   ")
