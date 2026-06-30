"""Configuration management for HostGuard."""

import configparser
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config" / "hostguard.ini"


class ConfigurationManager:
    """Read HostGuard configuration from an INI file."""

    def __init__(self, path: Path = DEFAULT_CONFIG_PATH) -> None:
        """Initialize the manager with a configuration file path."""
        self.path = path

    def load(self) -> configparser.ConfigParser:
        """Read and return the configuration file."""
        if not self.path.is_file():
            raise FileNotFoundError(
                f"Configuration file not found: {self.path}"
            )

        configuration = configparser.ConfigParser()
        configuration.read(self.path, encoding="utf-8")
        return configuration
