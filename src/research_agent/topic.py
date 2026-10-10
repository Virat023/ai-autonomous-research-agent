def validate_topic(topic: str) -> str:
    """Return a cleaned topic, or raise an error if it is blank."""
    cleaned_topic = topic.strip()
    if not cleaned_topic:
        raise ValueError("Topic cannot be blank.")
    return cleaned_topic
