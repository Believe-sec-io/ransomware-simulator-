import logging
from pathlib import Path


LOG_DIRECTORY = Path("logs")
LOG_FILE = LOG_DIRECTORY / "simulation.log"


def setup_logger() -> logging.Logger:
    """Create and configure the simulator logger."""

    LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("RansomwareSimulator")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()
