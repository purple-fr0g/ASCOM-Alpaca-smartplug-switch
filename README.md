# ASCOM-Alpaca-smartplug-switch
An implementation of an ASCOM Alpaca switch for smartplugs using Alpyca, based on the switch template.

## 1 Configuration
To use this Alpaca device with one or more smart plug(s) you need to:
  1. add the driver into the `smartplug_driver/` folder.
  2. import the driver module into `switch.py` and add the corresponding entry into the `supported_devices` dict.
  3. add the Device into the config.toml

### 1.1 Custom driver
The current implementation just uses 2 methods:
  1. one that sets a certain outlet to on/off
  2. and one that gets all switch states

### 1.2 config.toml specifics
`[network]` controls the address and port of the Alpaca device itself. 
`[server]` sets some server settings (also of the Alpaca device)
`[logging]` sets some logging stuff
`[device]` is where the devices get specified

#### 1.2.1 device setup
For each smart plug there should be an entry like this:
```toml
  [[device.smartplug]]
    name = "name"
    addr = "address:port"
    driver = "driver_name"

        [[device.smartplug.outlet]]
        name = "name"
        description = "description"
```

Its important is that the smart plug has the same amount of outlets as it has `[[device.strips.switch]]` entries as its size is given implicitly by the number of switches specified here.

You can have multiple devices

# 2 Roadmap
The goal is to make the switch 100% conform to the ASCOM Alpaca protocol as enforced by conformu. Right now it has no issues or errors in the regular device test, but still some errors in the conformu `Check Alpaca Protocol` tab.
