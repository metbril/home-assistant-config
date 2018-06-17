# Home Kit

The main documentation can be found here: https://www.home-assistant.io/components/homekit

To reset home kit, take these steps:

1. Stop HA
2. Remove file `.homekit.state`
3. Start HA

HA will start after a 1 minute delay. It will then show a persistent notification with the PIN.