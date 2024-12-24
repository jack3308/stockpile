"""The StockPile integration."""
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from .const import DOMAIN

PLATFORMS = [Platform.SENSOR, Platform.NUMBER]

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the StockPile component."""
    hass.data.setdefault(DOMAIN, {})
    
    # Load platforms
    await hass.async_create_task(
        hass.helpers.discovery.async_load_platform("sensor", DOMAIN, {}, config)
    )
    await hass.async_create_task(
        hass.helpers.discovery.async_load_platform("number", DOMAIN, {}, config)
    )
    
    return True 