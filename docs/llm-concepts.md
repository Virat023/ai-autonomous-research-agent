# LLM Integration Concepts

A large language model (LLM) receives text and generates a response.

The application sends a request containing:
- The user’s research question.
- Instructions about the response format.
- Optional settings such as a response length limit.

The model returns a response. The application should check that the response is usable before relying on it.

An LLM can make mistakes. Research findings must still be checked against collected sources and citations.

A local model runs on the user’s computer. A hosted model runs on another service and may require an account, an API key, or payment. We will review these requirements before choosing a provider.
