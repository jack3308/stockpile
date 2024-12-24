"""Config flow for StockPile."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

ITEM_SCHEMA = vol.Schema({
    vol.Required("name"): str,
    vol.Optional("initial_quantity", default=0): int,
    vol.Optional("min_threshold", default=1): int,
    vol.Optional("unit_of_measurement", default="units"): str,
})

CONFIG_SCHEMA = vol.Schema({
    vol.Required("items"): vol.All(
        vol.List(ITEM_SCHEMA),
        vol.Length(min=1)
    )
}) 