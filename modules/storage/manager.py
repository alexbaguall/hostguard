"""Read-only storage target management for HostGuard."""

import configparser
import logging

from modules.core.config import ConfigurationManager
from modules.core.logger import create_logger

from .collector import StorageCollector
from .exceptions import StorageConfigurationError
from .result import StorageSelection
from .selector import StorageSelector
from .target import StorageTarget


class StorageManager:
    """Discover configured targets and select an eligible destination."""

    def __init__(
        self,
        configuration: ConfigurationManager | None = None,
        collector: StorageCollector | None = None,
        selector: StorageSelector | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        """Initialize storage dependencies without performing discovery."""
        self.configuration = configuration or ConfigurationManager()
        self.collector = collector or StorageCollector()
        self.selector = selector or StorageSelector()
        self.logger = logger or create_logger()
        self._targets: list[StorageTarget] | None = None

    def list_targets(self) -> list[StorageTarget]:
        """Discover and return all configured storage targets."""
        self.logger.info("Storage discovery started")
        try:
            configuration = self._load_configuration()
            targets = [
                self._collect_target(configuration, target_id)
                for target_id in self._target_ids(configuration)
            ]
            self._targets = targets
            return list(targets)
        finally:
            self.logger.info("Storage discovery finished")

    def select_target(self) -> StorageSelection:
        """Select a target from the most recent discovery."""
        targets = (
            self._targets
            if self._targets is not None
            else self.list_targets()
        )
        selection = self.selector.select(targets)
        self.logger.info(
            "Target selected: target_id=%s",
            selection.selected_target.id,
        )
        return selection

    def _load_configuration(self) -> configparser.ConfigParser:
        """Load configuration and normalize configuration errors."""
        try:
            configuration = self.configuration.load()
        except (FileNotFoundError, configparser.Error) as error:
            raise StorageConfigurationError(str(error)) from error
        if not configuration.has_section("storage"):
            raise StorageConfigurationError(
                "Missing [storage] configuration section."
            )
        return configuration

    @staticmethod
    def _target_ids(
        configuration: configparser.ConfigParser,
    ) -> list[str]:
        """Return configured target identifiers."""
        raw_targets = configuration.get("storage", "targets", fallback="")
        targets = [
            target.strip()
            for target in raw_targets.split(",")
            if target.strip()
        ]
        if not targets:
            raise StorageConfigurationError(
                "No storage targets are configured."
            )
        return targets

    def _collect_target(
        self,
        configuration: configparser.ConfigParser,
        target_id: str,
    ) -> StorageTarget:
        """Validate one target definition and collect its state."""
        path_key = f"target.{target_id}.path"
        priority_key = f"target.{target_id}.priority"
        path = configuration.get("storage", path_key, fallback="").strip()
        if not path:
            raise StorageConfigurationError(
                f"Missing path for storage target '{target_id}'."
            )
        try:
            priority = configuration.getint("storage", priority_key)
        except (ValueError, configparser.Error) as error:
            raise StorageConfigurationError(
                f"Invalid priority for storage target '{target_id}'."
            ) from error
        description = configuration.get(
            "storage",
            f"target.{target_id}.description",
            fallback="",
        )
        return self.collector.collect(
            target_id=target_id,
            path=path,
            priority=priority,
            description=description,
        )
