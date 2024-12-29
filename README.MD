# StockPile - Home Assistant Integration

[![hacs\_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)

A Home Assistant integration for managing stockpiles of consumable items.

## Features

*   Track quantities of consumable items

*   Monitor consumption patterns

*   Manage restocking events

*   Schedule consumption and restocking

*   Support different types of consumables

## Installation

1.  Install via HACS (recommended):

    *   Add this repository to HACS as a custom repository

    *   Search for "StockPile" in HACS integrations

    *   Install and restart Home Assistant

2.  Manual Installation:

    *   Copy the `custom_components/stockpile` directory to your Home Assistant's `custom_components` directory

    *   Restart Home Assistant

## Configuration

Add to your `configuration.yaml`:

    stockpile:
      piles:
      - name: wine
        unit: bottles
        initial_quantity: 12
        min_quantity: 2
        max_quantity: 24
        step_size: 1

