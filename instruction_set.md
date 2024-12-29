### Detailed Instruction Set for LLM

#### Phase 1: Entity Setup

1. Implement a device that will be the parent of all entities for each 'stockpile' entry in home assistant

2. Implement a Sensor Entity for Quantity Tracking

*   Define a new entity class that inherits from Entity.

*   Implement the necessary methods to track the quantity of consumables.

*   Use type annotations for all methods and include docstrings for documentation.

2. Implement the Calendar Entity for Event Management&#x20;

*   Create a calendar entity that can manage events related to stockpile consumption and restocking.

*   Ensure that the calendar entity can handle datetime validations.

*   Ensure state restoration using the standard home assistant state persistence

3. Set Up the Sensor Entities for Pile and Stock Information

*   Create sensor entities to represent different piles and stock types.

*   Implement methods to retrieve and update the state of these sensors.

##### Notes

*   Each entity should persist across home assistant restarts.&#x20;

*   Each entity should use the device/stockpile name as a suffix for the entity, ensuring standard formatting and readability

#### Phase 2: Attributes Implementation

1. Implement Stockpile Quantity Attributes

*   Add attributes to the stockpile entity to track consumption parameters.

*   Implement validation for minimum, maximum, and step values for the quantity.

2. Add Calendar Entity Attributes

*   Implement attributes for the calendar entity to manage event cycles and handle datetime validations.

3. Implement Pile and Stock Attributes

*   Create attributes for different stock types and implement scheduling logic for consumption.

#### Phase 3: Actions Development

*   Develop the stockpile.consume Action

<!---->

*   Implement quantity validation logic.

<!---->

*   Create calendar events upon consumption.

<!---->

*   Manage scheduling for future consumption events.

2. Develop the stockpile.restock Action

*   Handle both standard and custom quantity restocking.

<!---->

*   Implement event history management to track restocking events.

<!---->

*   Develop the stockpile.cycle Action

<!---->

*   Manage cycle periods for consumption.

<!---->

*   Implement logic to handle event chains related to cycles.

4. Develop the stockpile.schedule Action

*   Create events based on user-defined schedules.

<!---->

*   Validate the data structure for scheduling.

#### Phase 4: Critical Implementation Details

*   Data Validation

<!---->

*   Ensure that all consumption steps are valid multiples.

<!---->

*   Validate date/time inputs and check quantity bounds.

<!---->

*   Event Management

<!---->

*   Create historical records for calendar events.

<!---->

*   Store event data in the description field and handle overlaps.

3. Scheduling Logic

*   Implement logic for periodic and scheduled consumption, including conflict management.

#### Phase 5: Testing Scenarios

1. Basic Operations Testing

*   Write unit tests for standard consumption, restocking, and cycle management.

<!---->

*   Edge Cases Testing

<!---->

*   Implement tests for handling multiple targets, schedule conflicts, and cycle transitions.

3. Data Validation Testing

*   Create tests for invalid quantities, schedules, and cycle periods.

#### Phase 6: Implementation Notes

*   Code Organization

<!---->

*   Separate entity logic into different modules (e.g., sensor.py, binary\_sensor.py).

<!---->

*   Create utility functions for common operations and implement error handling.

<!---->

*   Configuration Flow

<!---->

*   Define the flow for device setup, entity registration, service registration, and attribute management.

3. Best Practices

*   Follow Home Assistant coding standards, implement state management, and handle configuration validation.

#### Phase 7: Development Workflow

1. Initial Setup and Configuration Validation

*   Ensure that the integration is properly set up and validated before proceeding.

<!---->

*   Entity Implementation

<!---->

*   Implement the entities as defined in the previous phases.

<!---->

*   Service Implementation

<!---->

*   Define and implement the services that will interact with the entities.

<!---->

*   Integration Testing

<!---->

*   Conduct thorough testing of the integration to ensure functionality.

<!---->

*   Documentation Generation

<!---->

*   Generate documentation for the integration, including usage examples and configuration details.

