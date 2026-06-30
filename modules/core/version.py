"""Version access for HostGuard."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_VERSION_PATH = PROJECT_ROOT / "VERSION"


class Version:
    """Read the HostGuard version from the project VERSION file."""

    def __init__(self, path: Path = DEFAULT_VERSION_PATH) -> None:
        """Initialize version access and read the version file."""
        self.path = path
        self.value = self._read()

    def _read(self) -> str:
        """Read and return the current HostGuard version."""
        return self.path.read_text(encoding="utf-8").strip()
