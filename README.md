# Metbril's 🤓 Home Assistant Configuration

[![Check configuration](https://github.com/metbril/home-assistant-config/workflows/Check%20configuration/badge.svg)](https://github.com/metbril/home-assistant-config/actions?query=workflow%3A%22Check+configuration%22)

This repository contains my configuration for Home Assistant. It is installed on a Raspberry Pi model 2B.

## Editing

### Lovelace

To start tracking the lovelace UI file `.storage/lovelace`, you need to force-add it to git:

```bash
git add -f .storage/lovelace
```

### Automation Editor

Using the automation editor is an easy way to test automations or to create temporary automations for debugging.

To use the automation editor in combination with packages, there needs to be [a separate `automations.yaml` file in the root of the config directory](./automations.yaml), with a least one properly formatted automation. My config has a dummy automation to prevent that the configuration becomes invalid.

## Database

To limit database growth, I limit [recording](https://home-assistant.io/components/recorder/) as much as possible and purge the database daily for values older than 3 days.

## Devices

### Z-Wave

The OZW logfile was growing rapidly with it's default configuration. To lower the logging level, I have edited the `options.xml` file in the config folder as per [the instructions in the OZW Wiki](https://github.com/OpenZWave/open-zwave/wiki/Config-Options):

```xml
  <Option name="SaveLogLevel" value="6" />
```
## Backups

I create backups with the [Home Assistant Google Drive Backup addon](https://github.com/sabeechen/hassio-google-drive-backup).

## Credits 🙏

- [Frenck's yamllint action](https://github.com/frenck/action-yamllint)
- [Frenck's home assistant configuration checker](https://github.com/frenck/action-home-assistant)

## Contributions

If you have suggestions or improvements, please submit an issue or pull request.
