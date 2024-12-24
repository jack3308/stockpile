"""Number platform for StockPile."""
from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, DEFAULT_QTY

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None,
) -> None:
    """Set up the StockPile number platform."""
    entities = []
    for item in hass.data[DOMAIN].get("items", []):
        entities.append(StockPileQuantity(item["name"]))

    async_add_entities(entities)

class StockPileQuantity(NumberEntity):
    """Representation of a StockPile item quantity."""

    def __init__(self, name):
        """Initialize the number."""
        self._name = name
        self._value = DEFAULT_QTY
        self._attr_unique_id = f"{name}_pile"
        self._attr_native_min_value = 0
        self._attr_native_max_value = 999
        self._attr_native_step = 1

    @property
    def name(self):
        """Return the name of the number."""
        return f"{self._name.title()} Quantity"

    @property
    def native_value(self):
        """Return the current value."""
        return self._value

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        self._value = value 