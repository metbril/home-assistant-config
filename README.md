# Metbril's 🤓 Home Assistant Configuration

[![Check configuration][check-badge]][check-log]
[![Mastodon][mastodon-badge]][mastodon-link]

This repository contains my configuration for Home Assistant.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<details>
<summary>Details</summary>

- [Configuration principles](#configuration-principles)
  - [Automations, Scripts & Scenes](#automations-scripts--scenes)
- [HASS.io](#hassio)
  - [Host hardware](#host-hardware)
- [Add-ons](#add-ons)
  - [SSH](#ssh)
  - [Samba](#samba)
  - [Backups](#backups)
- [Custom Components](#custom-components)
  - [HACS](#hacs)
- [Z-Wave](#z-wave)
- [Hardware](#hardware)
  - [Sonos](#sonos)
  - [Neo Coolcam](#neo-coolcam)
- [Dashboards](#dashboards)
  - [Themes](#themes)
  - [Mushroom & Tile cards](#mushroom--tile-cards)
  - [Custom cards](#custom-cards)
- [Tips & Tricks](#tips--tricks)
  - [Tracking your Lovelace UI file](#tracking-your-lovelace-ui-file)
  - [Testing and debugging automations with automation editor](#testing-and-debugging-automations-with-automation-editor)
  - [Limit database growth](#limit-database-growth)
  - [Outside Brightness](#outside-brightness)
- [Maintenance](#maintenance)
- [Credits 🙏](#credits-)
- [Contributions](#contributions)

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Configuration principles

I used to be an avid user of packages. That provided an easy way to keep 
funtionality together, enable or disable it, and share with others. However,
Home Assistant is slowly phasing out YAML configuration and adding more and
more features to the UI. This has pros and cons, but the main advantage is,
that you don't need a real computer, ssh or a Samba connection
to edit the configuration.

The biggest drawback of using the UI is, that editing using the interface 
usually takes more time than editing a text file. But on the other hand, I have
spent a lot of time fixed yaml syntax and formatting errors.

So for now I have decided to move as much configuration as possible to the UI.

### Automations, Scripts & Scenes

Since using the UI editor for automations, scripts and scenes, I have noticed
that I change those a lot. These means that changes are scattered around the
files. Since I want to track changes through git and be able
to revert to old versions, I have again decided to split these files
`automations.yaml`, `scripts.yaml` and `scenes.yaml` into separate files.
I will continue using the files for quick one offs or testing.

## HASS.io

This file contains specific details about my HASS.io installation.

### Host hardware

The system is currently running on Hardkernel Odroid-N2 (like [Home Assistant Blue][blue]).
Previously, I have used a Raspberry Pi 3B and before that a Raspberry Pi 2B.

## Add-ons

I recently switched to [Home Assistant Cloud][cloud] from a self-managed proxy setup.
So I closed the port on my firewall and no longer need the add-ons that made this possible:
Nginx Proxy, Duckdns and Certbot.

### SSH

### Samba

### Backups

I create backups with the [Home Assistant Google Drive Backup addon](https://github.com/sabeechen/hassio-google-drive-backup).

## Custom Components

### HACS

To manage my custom components, I use [HACS](https://hacs.xyz/).

## Z-Wave

I am using Z-Wave. I started using it as a reliable, secure and 2-way alternative to cheap 433 MHz devices (mainly Klik-Aan-Klik-Uit). This was before Philips Hue and Ikea Trådfri became large and mainstream, and thus the Zigbee protocol.

Until the end of 2019 I have been using the standard Hassio [Z-Wave integration](https://www.home-assistant.io/integrations/zwave/), but have migrated to [Zwave2Mqtt](https://github.com/OpenZWave/Zwave2Mqtt) since.

The reason to switch to Zwave2Mqtt was, to de-couple Home Assistant from my Z-Wave network. This should provide me with a healthier and more stable Z-Wave mesh. Using the Z-Wave integration, you will restart your entire network with every restart of Home Assistant, which can lead to unexpected results. And you need to wait minutes for all entities to show up.

Somewhere in 2023, I moved to the [Z-Wave JS integration](https://www.home-assistant.io/integrations/zwave_js/). 

## Hardware

Connected (smart) hardware:

- Sonos speakers
- [LG WebOS TV](https://www.home-assistant.io/integrations/webostv/)

### Sonos

Sonos speakers are added through discovery. This is more convenient than configuring manually.

### Neo Coolcam

Template sensor to fix a bug in some Neo wall plugs.
The applied constant is the equivalent of 0x7FFFFFFF.
Device precision is 2 decimals.
The original sensosr is renamed to "...raw_energy"
The template sensor then gets the old name.

https://community.home-assistant.io/t/energy-consumption-for-neo-coolcam-plug/219844/26

## Dashboards

### Themes

I only use themes from HACS. These are installed in the `themes` folder, but are never uploaded to this repo.

### Mushroom & Tile cards

I really like [Mushroom](https://github.com/piitaya/lovelace-mushroom) and [Tile cards](https://www.home-assistant.io/dashboards/tile/). However, they do not (yet) have the flexibility of the entities card in combination with some custom cards.

### Custom cards

I use several custom cards for displaying a nice and tailored dashboard. Among thise are:

- [Mini Graph Card](https://github.com/kalkih/mini-graph-card)
- [Mini Mediaplayer](https://github.com/kalkih/mini-media-player)
- [Fold Entity Row](https://github.com/thomasloven/lovelace-fold-entity-row)
- [Multiple Entity Row](https://github.com/benct/lovelace-multiple-entity-row)
- [Template Entity Row](https://github.com/thomasloven/lovelace-template-entity-row)

## Tips & Tricks

Editing your configuration

- [Tracking your lovelace UI file](#tracking-your-lovelace-ui-file)
- [Testing and debugging automations with automation editor](#testing-and-debugging-automations-with-automation-editor)

Database

- [Limit database growth](#limit-database-growth)

### Tracking your Lovelace UI file

To start tracking the lovelace UI file `.storage/lovelace`, you need to force-add it to git:

```bash
git add -f .storage/lovelace
```

### Testing and debugging automations with automation editor

Using the automation editor is an easy way to test automations or to create temporary automations for debugging.

To use the automation editor in combination with packages, there needs to be [a separate `automations.yaml` file in the root of the config directory](./automations.yaml), with a least one properly formatted automation. My config has a dummy automation to prevent that the configuration becomes invalid.

### Limit database growth

To limit database growth, I limit [recording](https://home-assistant.io/components/recorder/) as much as possible and purge the database daily for values older than 3 days.

### Outside Brightness

Use a template sensor to calculate outside brightness. This takes into account the sun elevation, cloudiness and radiation.

https://community.home-assistant.io/t/virtual-light-sensor/31975/24
https://en.wikipedia.org/wiki/Solar_irradiance#:~:text=Average%20annual%20solar%20radiation%20arriving,level%20on%20a%20clear%20day.
https://gps-coordinates.org/coordinate-converter.php
max elevation https://www.suncalc.org/#/40.1789,-3.5156,3/2022.09.13/17:15/1/3

## Maintenance

For the maintenance of my configuration, I use these tools:

- Visual Studio Code, with extensions:
  - Home Assistant Config Helper
  - YAML
  - markdownlint
  - UUID Generator
- [yamllint][yamllint]
- [pre-commit][pre-commit]

To use yamllint with pre-commit, execute these commands:

```shell
brew install yamllint
brew install pre-commit
pre-commit install
```

## Credits 🙏

- [Frenck's yamllint action](https://github.com/frenck/action-yamllint)
- [Frenck's home assistant configuration checker](https://github.com/frenck/action-home-assistant)

## Contributions

If you have suggestions or improvements, please submit an issue or pull request.

[check-badge]: https://github.com/metbril/home-assistant-config/workflows/Check%20configuration/badge.svg
[check-log]: https://github.com/metbril/home-assistant-config/actions?query=workflow%3A%22Check+configuration%22
[pre-commit]: https://pre-commit.com/
[yamllint]: https://yamllint.readthedocs.io/en/stable/
[mastodon-badge]: https://img.shields.io/mastodon/follow/109290308537002308?domain=https%3A%2F%2Fbotsin.space&style=flat
[mastodon-link]: https://botsin.space/@DomusSapiens
[blue]: https://www.home-assistant.io/blue
