"""Sensor platform for StockPile."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, DEFAULT_NAME

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None,
) -> None:
    """Set up the StockPile sensor platform."""
    # For demo, we'll create a single item
    entities = []
    for item in hass.data[DOMAIN].get("items", []):
        entities.append(StockPileNameSensor(item["name"]))
    async_add_entities(entities)

class StockPileNameSensor(SensorEntity):
    """Representation of a StockPile item name sensor."""

    def __init__(self, name):
        """Initialize the sensor."""
        self._name = name
        self._attr_unique_id = f"{name}_stockpile"

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._name.title()} Stockpile"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._name 