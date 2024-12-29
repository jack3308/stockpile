# Home Assistant Stockpile Integration

## 1. Core Concepts & Context Setting

First, ensure the LLM understands that this is a Home Assistant integration for managing stockpiles of consumable items. The integration needs to track:

*   Quantity of items

*   Consumption patterns

*   Restocking events

*   Scheduling of events

*   Different types of consumables (medication, food, etc.)

### Key Abstractions

Have the LLM understand these core concepts:

*   **Pile**: The collective consumable (e.g., "wine", "dog food")

*   **Stock**: The unit of measurement (e.g., "bottle", "meal")

*   **Stockpile**: The device

## 2. Development Structure

Guide the LLM to develop the integration in this order:

### Phase 1: Entity Setup

1.  Create the base number entity for quantity tracking

2.  Implement the calendar entity for event management

3.  Set up the sensor entities for pile and stock information

### Phase 2: Attributes Implementation

1.  Start with stockpile\_quantity attributes

    *   Focus on consumption parameters

    *   Implement validation for min/max/step values

2.  Add calendar entity attributes

    *   Handle datetime validations

    *   Implement cycle management

3.  Implement pile and stock attributes

    *   Handle different stock types

    *   Implement scheduling logic

### Phase 3: Actions Development

Break down each action into smaller components:

1.  `stockpile.consume`:

    *   Quantity validation

    *   Calendar event creation

    *   Schedule management

2.  `stockpile.restock`:

    *   Standard vs custom quantity handling

    *   Event history management

3.  `stockpile.cycle`:

    *   Cycle period management

    *   Event chain handling

4.  `stockpile.schedule`:

    *   Event creation

    *   Data structure validation

## 3. Critical Implementation Details

Guide the LLM to pay special attention to:

### Data Validation

*   Ensure consumption steps are valid multiples

*   Validate date/time inputs

*   Check quantity bounds

### Event Management

1.  Calendar Events:

    *   Always create historical records

    *   Store event data in description field

    *   Handle event overlaps

### Scheduling Logic

1.  For periodic consumption:

    *   Remove future events appropriately

    *   Calculate next event timing

2.  For scheduled consumption:

    *   Handle multiple schedule types

    *   Manage schedule conflicts

## 4. Testing Scenarios

Have the LLM implement tests for:

1.  Basic Operations:

    *   Standard consumption

    *   Standard restocking

    *   Cycle management

2.  Edge Cases:

    *   Multiple target handling

    *   Schedule conflicts

    *   Cycle transitions

3.  Data Validation:

    *   Invalid quantities

    *   Invalid schedules

    *   Invalid cycle periods

## 5. Implementation Notes

### Code Organization

Guide the LLM to:

1.  Separate entity logic

2.  Create utility functions for common operations

3.  Implement proper error handling

4.  Use type hints and documentation

### Configuration Flow

1.  Device setup

2.  Entity registration

3.  Service registration

4.  Attribute management

### Best Practices

1.  Follow Home Assistant coding standards

2.  Implement proper state management

3.  Use appropriate debugging

4.  Handle configuration validation

## 6. Development Workflow

Guide the LLM through:

1.  Initial setup and configuration validation

2.  Entity implementation

3.  Service implementation

4.  Integration testing

5.  Documentation generation

Remember to have the LLM validate each step before moving to the next phase.
