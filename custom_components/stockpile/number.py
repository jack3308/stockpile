"""StockPile number platform."""
from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo
# from homeassistant.helpers.restore_state import RestoreNumber


from .const import DOMAIN, MANUFACTURER

async def async_setup_entry(
    hass: HomeAssistant, 
    entry: ConfigEntry, 
    async_add_entities: AddEntitiesCallback
) -> None:
    """Set up number platform."""
    async_add_entities([StockPileNumber(entry)])

class StockPileNumber(NumberEntity):
    """StockPile number class."""

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the number."""
        self.entry = entry
        self._attr_unique_id = f"stockpile_{entry.data['name'].lower()}"
        self._attr_name = entry.data['name']
        self._attr_icon = "mdi:counter"
        self._attr_mode = "box"
        try:
            self._attr_native_value = float(entry.data['initial_quantity'])
        except (ValueError, TypeError):
            self._attr_native_value = 0.0
        self._attr_native_min_value = 0
        self._attr_native_max_value = 999
        self._attr_native_step = 1
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self._attr_unique_id)},
            name=entry.data['name'],
            manufacturer=MANUFACTURER
        )

    async def async_added_to_hass(self) -> None:
        """Run when entity about to be added to hass."""
        if state := await self.async_get_last_number_data():
            self._attr_native_value = float(state.state)

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        self._attr_native_value = value