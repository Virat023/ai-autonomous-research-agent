# AI Autonomous Research & Analyst Agent

An AI-powered research agent designed to gather information, analyze evidence, and generate structured reports with citations.

## Project goals

- Research a user-provided topic systematically.
- Gather information from relevant sources.
- Analyze and synthesize findings.
- Produce reports supported by citations.
- Handle unreliable sources and research errors transparently.

## Current status

The project is under active development. The command-line app currently accepts a topic, removes extra spaces, and rejects blank input. Web search and page text extraction are available as separate components, but are not yet connected to the command-line workflow. AI analysis and report generation are planned.

## Technology

- Python 3.12
- uv for Python dependencies and project commands
- pytest for tests
- DDGS for web search
- HTTPX and Beautiful Soup for retrieving and extracting page text

## Getting started

### Prerequisites

Install Python 3.12, Git, and uv.

### Set up the project

Clone the repository and enter its folder:

```powershell
git clone https://github.com/Virat023/ai-autonomous-research-agent.git
cd ai-autonomous-research-agent