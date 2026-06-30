"""Logging infrastructure for HostGuard."""

import logging
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LOG_PATH = PROJECT_ROOT / "logs" / "hostguard.log"


def create_logger(
    name: str = "hostguard",
    level: int = logging.INFO,
    log_path: Path = DEFAULT_LOG_PATH,
) -> logging.Logger:
    """Create or return a configured HostGuard logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    resolved_path = log_path.resolve()
    for handler in logger.handlers:
        if (
            isinstance(handler, logging.FileHandler)
            and Path(handler.baseFilename) == resolved_path
        ):
            return logger

    log_path.parent.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(log_path, encoding="utf-8")
    handler.setLevel(level)
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s: %(message)s"
        )
    )
    logger.addHandler(handler)
    return logger
