# Input booleans

Component: [`input_boolean`](https://www.home-assistant.io/integrations/input_boolean/)

Input booleans do not support `unique_id`. This prevents them from being edited
in the UI.

Input booleans do not support `friendly_name`. This prevents them from being
customized in the UI. A friendly name should be set in `customize.yaml`. But since `name` does not define the entity id, this could also be used to set a friendly name.

## Occupancy

Input booleans that set the occupancy mode for the house. These have an `occupancy` prefix on purpose. This prefix is used in automations to synchronise all entities.

Entity | Description
--- | ---
`occupancy_asleep` | Everyone is asleep
`occupancy_away` | Everyone is away. No-one is home. This does not need to be the same as a presence sensor, but is related.
`occupancy_guests` | When the house is in guest mode, some automations will not run.
`occupancy_home` | At least someone is at home. This is the default occupancy.
`occupancy_party` | Party time! If this mode is active, some automations will not run.
`occupancy_vacation` | Everybody is away for a longer period of time. Mostly overnight. This mode is used to automatically switch of the lights to simulate presence and to save energy.
