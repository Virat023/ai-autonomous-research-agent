import ollama


DEFAULT_MODEL = "llama3.2:3b"


def generate_response(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """Send a prompt to the local Ollama model and return its response."""
    cleaned_prompt = prompt.strip()
    if not cleaned_prompt:
        raise ValueError("Prompt cannot be blank.")

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": cleaned_prompt}],
    )
    answer = response.message.content.strip()
    if not answer:
        raise RuntimeError("The language model returned an empty response.")

    return answer
