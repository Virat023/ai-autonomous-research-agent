from research_agent.logging_config import configure_logging
from research_agent.research import research_topic


def main() -> None:
    configure_logging()
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


if __name__ == "__main__":
    main()