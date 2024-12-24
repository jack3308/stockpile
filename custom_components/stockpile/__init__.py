"""The StockPile integration."""
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from .const import DOMAIN

PLATFORMS = [Platform.SENSOR, Platform.NUMBER]

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the StockPile component."""
    if DOMAIN not in config:
        return True

    # Store the config data
    hass.data[DOMAIN] = config[DOMAIN]
    
    # Load platforms
    for platform in PLATFORMS:
        hass.async_create_task(
            hass.helpers.discovery.async_load_platform(
                platform, DOMAIN, config[DOMAIN], config
            )
        )
    
    return True 