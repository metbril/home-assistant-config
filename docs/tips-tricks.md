# Tips & Tricks

Editing your configuration

- [Tracking your lovelace UI file](#tracking-your-lovelace-ui-file)
- [Testing and debugging automations with automation editor](#testing-and-debugging-automations-with-automation-editor)

Database

- [Limit database growth](#limit-database-growth)

## Tracking your Lovelace UI file

To start tracking the lovelace UI file `.storage/lovelace`, you need to force-add it to git:

```bash
git add -f .storage/lovelace
```

## Testing and debugging automations with automation editor

Using the automation editor is an easy way to test automations or to create temporary automations for debugging.

To use the automation editor in combination with packages, there needs to be [a separate `automations.yaml` file in the root of the config directory](./automations.yaml), with a least one properly formatted automation. My config has a dummy automation to prevent that the configuration becomes invalid.

## Limit database growth

To limit database growth, I limit [recording](https://home-assistant.io/components/recorder/) as much as possible and purge the database daily for values older than 3 days.

* * *

[< Back](./)
