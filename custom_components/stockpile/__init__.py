"""The StockPile integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

# Define the schema for each stockpile entry
STOCKPILE_SCHEMA = vol.Schema({
    vol.Required("name"): cv.string,
    vol.Required("unit"): cv.string,
    vol.Required("initial_quantity"): cv.positive_float,
    vol.Optional("min_quantity", default=0): cv.positive_float,
    vol.Optional("max_quantity"): cv.positive_float,
    vol.Optional("step_size", default=1): cv.positive_float,
})

# Define the main configuration schema
CONFIG_SCHEMA = vol.Schema({
    vol.Required("stockpile"): vol.Schema({
        vol.Required("piles"): vol.All(
            cv.ensure_list,
            [STOCKPILE_SCHEMA]
        )
    })
}, extra=vol.ALLOW_EXTRA)

# PLATFORMS = [Platform.SENSOR, Platform.CALENDAR]
PLATFORMS = [Platform.SENSOR]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the StockPile integration."""
    if "stockpile" not in config:
        return True

    # Store the configuration in hass.data
    hass.data["stockpile"] = {}
    conf = config["stockpile"]

    # Set up each stockpile
    for pile in conf["piles"]:
        pile_name = pile["name"]
        hass.data["stockpile"][pile_name] = pile

    # Forward the setup to the sensor and calendar platforms
    for platform in PLATFORMS:
        hass.async_create_task(
            hass.helpers.discovery.async_load_platform(
                platform, "stockpile", conf, config
            )
        )

    return True 