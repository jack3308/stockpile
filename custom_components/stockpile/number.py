"""Number platform for StockPile."""
from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, DEFAULT_QTY, DEFAULT_CONSUME_UNIT, DEFAULT_STOCK_UNIT

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None,
) -> None:
    """Set up the StockPile number platform."""
    entities = []
    
    for item_name, device_data in hass.data[DOMAIN]["devices"].items():
        entities.extend([
            StockPileQuantity(item_name, device_data),
            StockPileConsumeUnit(item_name, device_data),
            StockPileStockUnit(item_name, device_data)
        ])

    async_add_entities(entities)

class StockPileNumberBase(NumberEntity):
    """Base class for StockPile number entities."""

    def __init__(self, name, device_data):
        """Initialize the number."""
        self._name = name
        self._device_data = device_data
        self._value = DEFAULT_QTY
        self._attr_device_info = device_data["device_info"]

class StockPileQuantity(StockPileNumberBase):
    """Representation of a StockPile item quantity."""

    def __init__(self, name, device_data):
        """Initialize the quantity number."""
        super().__init__(name, device_data)
        self._attr_unique_id = f"{name.lower()}_quantity"
        self._attr_native_min_value = 0
        self._attr_native_max_value = 999
        self._attr_native_step = 1
        self._value = device_data["config"].get("initial_quantity", DEFAULT_QTY)

    @property
    def name(self):
        """Return the name of the number."""
        return f"{self._name} Quantity"

    @property
    def native_value(self):
        """Return the current value."""
        return self._value

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        self._value = value

class StockPileConsumeUnit(StockPileNumberBase):
    """Representation of a StockPile consume unit."""

    def __init__(self, name, device_data):
        """Initialize the consume unit number."""
        super().__init__(name, device_data)
        self._attr_unique_id = f"{name.lower()}_consume_unit"
        self._attr_native_min_value = 1
        self._attr_native_max_value = 99
        self._attr_native_step = 1
        self._value = DEFAULT_CONSUME_UNIT

    @property
    def name(self):
        """Return the name of the number."""
        return f"{self._name} Consume Unit"

class StockPileStockUnit(StockPileNumberBase):
    """Representation of a StockPile stock unit."""

    def __init__(self, name, device_data):
        """Initialize the stock unit number."""
        super().__init__(name, device_data)
        self._attr_unique_id = f"{name.lower()}_stock_unit"
        self._attr_native_min_value = 1
        self._attr_native_max_value = 99
        self._attr_native_step = 1
        self._value = DEFAULT_STOCK_UNIT

    @property
    def name(self):
        """Return the name of the number."""
        return f"{self._name} Stock Unit" 