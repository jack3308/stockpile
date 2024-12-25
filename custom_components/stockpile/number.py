"""Number platform for StockPile."""
from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, MANUFACTURER

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the StockPile number."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([StockPileNumber(config_entry, data)])

class StockPileNumber(NumberEntity):
    """Representation of a StockPile number."""

    def __init__(self, config_entry: ConfigEntry, data: dict) -> None:
        """Initialize the number."""
        self._config_entry = config_entry
        self._attr_unique_id = f"stockpile_{data['name'].lower()}_pile"
        self._attr_name = f"{data['name']} Pile"
        self._value = data["initial_quantity"]
        
        # Device info
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self._attr_unique_id)},
            name=data["name"],
            manufacturer=MANUFACTURER,
            model="Inventory Item"
        )
        
        # Number entity attributes
        self._attr_native_min_value = 0
        self._attr_native_max_value = 999
        self._attr_native_step = 1
        self._attr_mode = "box"

    async def async_added_to_hass(self) -> None:
        """Handle entity which will be added."""
        await super().async_added_to_hass()
        
        # Restore previous state
        last_state = await self.async_get_last_state()
        if last_state is not None and last_state.state not in (None, "unknown", "unavailable"):
            self._value = float(last_state.state)

    @property
    def native_value(self) -> float:
        """Return the current value."""
        return self._value

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        self._value = value