"""Job event communication boundary for HostGuard."""

from collections.abc import Callable

from .event import JobEvent


EventSubscriber = Callable[[JobEvent], None]


class EventBus:
    """Define the interface for future Job Engine event subscribers."""

    def publish(self, event: JobEvent) -> None:
        """Accept an event without dispatching it in this sprint."""

    def subscribe(self, subscriber: EventSubscriber) -> None:
        """Accept a subscriber without registering it in this sprint."""

    def unsubscribe(self, subscriber: EventSubscriber) -> None:
        """Accept a subscriber without unregistering it in this sprint."""
