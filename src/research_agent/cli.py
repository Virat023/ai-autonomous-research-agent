from research_agent.topic import validate_topic


def main() -> None:
    topic = input("Enter a research topic: ")
    try:
        cleaned_topic = validate_topic(topic)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Research topic: {cleaned_topic}")


if __name__ == "__main__":
    main()
