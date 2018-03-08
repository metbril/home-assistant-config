# home-assistant-config

This repository contains my configuration for Home Assistant. It is installed on a Raspberry Pi model 2B.

## Database

I have quickly replaced the default sqlite database with MySQL.
The default database was growing rapidly and lead to bad performance.

To limit database growth, I limit recording as much as possible and purge the database for values older than 7 days.

## Devices

### Z-Wave

The OZW logfile was growing rapidly with it's default configuration. To lower the logging level, I have edited the `options.xml` file in the config folder as per [the instructions in the OZW Wiki](https://github.com/OpenZWave/open-zwave/wiki/Config-Options):

```xml
  <Option name="SaveLogLevel" value="6" />
```

## Contributions

If you have suggestions or improvements, please submit an issue or pull request.
