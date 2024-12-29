"""Sensor platform for StockPile integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import (
    DOMAIN,
    PILE_SENSOR_NAME,
    STOCK_SENSOR_NAME,
    ATTR_UNIT,
    ATTR_MIN_QUANTITY,
    ATTR_MAX_QUANTITY,
    ATTR_STEP_SIZE,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the StockPile sensor platform."""
    if discovery_info is None:
        return

    entities = []
    
    # Create sensors for each pile in the configuration
    for pile in discovery_info["piles"]:
        pile_name = pile["name"]
        
        # Create device registry entry for this stockpile
        device_id = f"stockpile_{pile_name}"
        
        # Create pile sensor (tracks overall quantity)
        entities.append(
            PileSensor(
                pile_name,
                pile["initial_quantity"],
                pile["unit"],
                device_id,
                pile.get("min_quantity", 0),
                pile.get("max_quantity"),
                pile.get("step_size", 1),
            )
        )
        
        # Create stock sensor (tracks individual items)
        entities.append(
            StockSensor(
                pile_name,
                pile["initial_quantity"],
                pile["unit"],
                device_id,
            )
        )

    add_entities(entities)

class PileSensor(NumberEntity):
    """Number entity for adjusting pile quantities."""

    def __init__(
        self,
        name: str,
        initial_quantity: float,
        unit: str,
        device_id: str,
        min_quantity: float,
        max_quantity: float | None,
        step_size: float,
    ) -> None:
        """Initialize the pile number entity."""
        self._attr_name = PILE_SENSOR_NAME.format(name)
        self._attr_unique_id = f"pile_{name}"
        self._attr_native_value = initial_quantity
        self._attr_native_unit_of_measurement = unit
        
        # Number entity specific attributes
        self._attr_native_min_value = min_quantity
        self._attr_native_max_value = max_quantity if max_quantity is not None else 9999999
        self._attr_native_step = step_size
        self._attr_mode = "box"  # Use a text input box for precise number entry
        
        # Device registry info
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device_id)},
            name=f"StockPile {name}",
            manufacturer="StockPile",
            model="Pile Tracker",
        )
        
        # Additional attributes
        self._attr_extra_state_attributes = {
            ATTR_UNIT: unit,
        }

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        self._attr_native_value = value
        self.async_write_ha_state()

class StockSensor(SensorEntity):
    """Sensor for tracking individual stock items."""

    def __init__(
        self,
        name: str,
        initial_quantity: float,
        unit: str,
        device_id: str,
    ) -> None:
        """Initialize the stock sensor."""
        self._attr_name = STOCK_SENSOR_NAME.format(name)
        self._attr_unique_id = f"stock_{name}"
        self._attr_native_value = initial_quantity
        self._attr_native_unit_of_measurement = unit
        # self._attr_device_class = SensorDeviceClass.QUANTITY
        
        # Device registry info
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device_id)},
            name=f"StockPile {name}",
            manufacturer="StockPile",
            model="Pile Tracker",
        ) 