import argparse
import re
from datetime import datetime
from pathlib import Path

from research_agent.logging_config import configure_logging
from research_agent.research import research_topic


REPORTS_DIR = Path("reports")


def save_report(topic: str, report: str) -> Path:
    """Save a report as a timestamped Markdown file."""
    topic_slug = re.sub(r"[^a-z0-9]+", "-", topic.strip().lower()).strip("-")
    topic_slug = topic_slug or "research"
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / f"{topic_slug}-{timestamp}.md"
    report_path.write_text(report, encoding="utf-8")
    return report_path


def main(argv: list[str] | None = None) -> None:
    configure_logging()

    parser = argparse.ArgumentParser(
        description="Research a topic and save a cited Markdown report."
    )
    parser.add_argument(
        "topic",
        nargs="*",
        help="Research topic. If omitted, you'll be prompted.",
    )
    args = parser.parse_args(argv)

    topic = " ".join(args.topic).strip()
    if not topic:
        topic = input("Enter a research topic: ")

    try:
        report = research_topic(topic)
    except ValueError as error:
        print(f"Error: {error}")
        return
    except RuntimeError as error:
        print(f"Research failed: {error}")
        return

    print(report)

    try:
        report_path = save_report(topic, report)
    except OSError as error:
        print(f"Could not save report: {error}")
    else:
        print(f"\nSaved report: {report_path}")


if __name__ == "__main__":
    main()