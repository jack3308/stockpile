"""Config flow for StockPile."""
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class StockPileConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for StockPile."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Create unique ID from the name
            await self.async_set_unique_id(f"stockpile_{user_input['name'].lower()}")
            self._abort_if_unique_id_configured()
            
            return self.async_create_entry(
                title=user_input["name"],
                data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("name"): str,
                vol.Required("initial_quantity", default=0): int,
            })
        ) 