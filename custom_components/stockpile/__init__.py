"""The StockPile integration."""
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform
from homeassistant.helpers.device_registry import DeviceRegistry
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN, MANUFACTURER

PLATFORMS = [Platform.NUMBER]

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the StockPile component."""
    if DOMAIN not in config:
        return True

    # Get device registry
    device_registry = DeviceRegistry(hass)
    
    hass.data[DOMAIN] = {
        "items": config[DOMAIN]["items"],
        "devices": {}
    }
    
    for item in config[DOMAIN]["items"]:
        device_id = f"{DOMAIN}_{item['name'].lower().replace(' ', '_')}"
        
        # Register device in Home Assistant
        device = device_registry.async_get_or_create(
            config_entry_id=None,
            identifiers={(DOMAIN, device_id)},
            name=item["name"],
            manufacturer=MANUFACTURER,
            model="Inventory Item",
            sw_version="1.0.0"
        )
        
        hass.data[DOMAIN]["devices"][item["name"]] = {
            "device_info": {
                "identifiers": {(DOMAIN, device_id)},
                "name": item["name"],
                "manufacturer": MANUFACTURER,
                "model": "Inventory Item",
                "sw_version": "1.0.0"
            },
            "config": item
        }
    
    for platform in PLATFORMS:
        hass.async_create_task(
            hass.helpers.discovery.async_load_platform(
                platform, DOMAIN, config[DOMAIN], config
            )
        )
    
    return True 