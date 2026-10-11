import logging


def configure_logging() -> None:
    """Set a consistent format for application log messages."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
