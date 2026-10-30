# AI Autonomous Research & Analyst Agent

A local research assistant that searches the web, gathers source text, and uses a language model to create a short report with source links and citations.

## Current features

- Accepts a research topic in the command line.
- Searches the web and retrieves available page text.
- Uses search snippets when a page cannot be retrieved.
- Generates a short report with numbered citations using Ollama and Qwen 3.
- Reports when some sources were available only as search snippets.
- Rejects model responses that omit citations or cite unknown sources.
- Saves each report as a timestamped Markdown file in the `reports/` folder.

Reports are model-generated and should be checked against their linked sources. A citation marker confirms that a source number exists; it does not independently verify every claim.

## Technology

- Python 3.12
- uv for dependencies and project commands
- pytest for tests
- DDGS for web search
- HTTPX and Beautiful Soup for retrieving and extracting page text
- Ollama with the `qwen3:4b` local model

## Getting started

### Prerequisites

Install Python 3.12, Git, uv, and Ollama.

### Set up the project

Clone the repository and enter its folder:

```powershell
git clone https://github.com/Virat023/ai-autonomous-research-agent.git
cd ai-autonomous-research-agent
```

Install dependencies and download the model:

```powershell
uv sync
ollama pull qwen3:4b
```

Make sure Ollama is running. Start the assistant interactively:

```powershell
uv run research-agent
```

Or pass a topic directly:

```powershell
uv run research-agent "solar energy"
```

The report appears in the terminal and is saved as a timestamped Markdown file in `reports/`. After the app finishes, run the tests from the PowerShell prompt:

```powershell
uv run pytest
```

## Current limitations

Some websites block automated page retrieval. When that happens, the agent may use the search result snippet and note this in the report. The model can make mistakes, so check important findings against the linked sources.

## License

No license has been selected yet.