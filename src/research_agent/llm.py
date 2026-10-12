import ollama


DEFAULT_MODEL = "qwen3:4b"


def generate_response(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """Send a prompt to the local Ollama model and return its response."""
    cleaned_prompt = prompt.strip()
    if not cleaned_prompt:
        raise ValueError("Prompt cannot be blank.")

    response = ollama.chat(
        model=model,
        messages=[
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
            {"role": "user", "content": cleaned_prompt},
        ],
        options={"temperature": 0},
    )

    answer = response.message.content.strip()
    if not answer:
        raise RuntimeError("The language model returned an empty response.")

    return answer
