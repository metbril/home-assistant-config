# Z-Wave

I am using Z-Wave. I started using it as a reliable, secure and 2-way alternative to cheap 433 MHz devices (mainly Klik-Aan-Klik-Uit). This was before Philips Hue and Ikea Trådfri became large and mainstream, and thus the Zigbee protocol.

Until the end of 2019 I have been using the standard Hassio [Z-Wave integration](https://www.home-assistant.io/integrations/zwave/), but have migrated to [Zwave2Mqtt](https://github.com/OpenZWave/Zwave2Mqtt) since.

The reason to switch to Zwave2Mqtt is, to de-couple Home Assistant from my Z-Wave network. This should provide me with a healthier and more stable Z-Wave mesh. Using the Z-Wave integration, you will restart your entire network with every restart of Home Assistant, which can lead to unexpected results. And you need to wait minutes for all entities to show up.

## Configuration

I have these components in place:

- [Official Hassio Moquitto Add-on]()
- [Zwave2Mqtt Hassio Community Add-on](https://github.com/hassio-addons/addon-zwave2mqtt)
- Hassio [MQTT integration](https://www.home-assistant.io/integrations/mqtt/), including [discovery](https://www.home-assistant.io/docs/mqtt/discovery/)

There are some good instructions available to set this up:

- 1
- 2

Create a new Home Assistant user `zwave2mqtt` through the Home Assistant UI. This user can be used to login to Mosquitto from the Zwave2Mqtt.

Install the Mosquitto broker add-on. The default configuration is fine. Start the broker.

Install the Open Z-Wave to MQTT addon. The default configuration is fine. Start the addon.

Add a panel to the Home Assistant UI in `configuration.yaml`. This will make it easier to access the web interface. Restart Home Assistant 

```yaml
panel_iframe:
  zwave2mqtt:
    title: Z-Wave to MQTT
    icon: mdi:z-wave
    url: http://hassio.local:8091
```

Open the panel. If asked for a username and password, enter your Home Assistant user.

Follow the instructions in one of the articles.

### Zwave2Mqtt

When using the MQTT integration and automatic discovery, you need to make sure that the MQTT prefix is `homeassistant`.

### Renaming devices and entities

After your Z-Wave devices have been discovered you will end up with unuseful or ugly entity names. Some of these can be edited easily through the UI.

**WARNING**: This paragraph describes how to manually edit files in the `.storage` folder. 
This is hazardous if you don't know what you are doing. 
Always stop Home Assistant first and make a backup of the `.storage` folder before you make any edits. 
DO THIS AT YOUR OWN RISK. I am NOT responsible if you screw up.

Rename displayed name of devices. Through UI.

Repace nodeid's in entitiy names with something more usefil. Can be done trough UI. But easier with search/replace through text file `<config>/.storage/core.entity_registry`. 
Replace all occurences of `.nodeid_18` with `.charging_station`. 
Notice the prepending dot (`.`). 
This will let you rename only sensors and switches. Be careful not to change the unique ID of the entity.

Search and replace is based on the "label" attribute in the JSON message.

entity type | search | replace
--- | --- | ---
sensor | `gas_density` | `voltage`
sensor | `generic` | `current`
sensor | `power` | `energy`
sensor | `power_8` | `power`

Hide sensors:

- `sensor.*_gas_density_17`
- `sensor.*_generic_21`
- `sensor.*_power_1`
- `sensor.*_power_2`
- `sensor.*_power_9`
- `sensor.*_temperature*`
- `sensor.*_water`

## Devices

An overview of the devices I use:

- Neo Coolcam Smart Power Plug
- Neo Coolcam Motion Sensor
- Neo Coolcam Siren
- Fibaro Smart Power Plug
- BeNext Multisensor

* * *

[< back](./)