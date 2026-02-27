# ASCOM-Alpaca-smartplug-switch
An implementation of an ASCOM Alpaca switch for smartplugs using Alpyca, based on the switch template.

Terminology: This Switch is an Alpaca `Device` that controls multiple `smartplugs` which are referenced by the `devnum` and have one or more `outlets` that are referenced by `id`.

## 1 Configuration
To use this Alpaca device with one or more smart plug(s) you need to:
  1. have the corresponding driver in `smartplug_driver/`.
  2. import the module into `switch.py` and add driver into the `supported_devices` dict.
  3. add the smartplug into the `config.toml`

### 1.1 Custom driver
To make this Switch work with your switches you need a `driver` for them. 
The current implementation of `switch.py` just uses 2 methods of the driver:
  1. one that sets a certain outlet to on/off
     `switch_power(addr: str, outlet_index: int, to_state: bool) -> None`
  2. and one that gets all switch states with signature
     `get_power_status(addr: str) -> list[bool]`

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
The order of the devices matters as the first device will have `devnum` 0, the 2nd one will have `devnum` 1 and so forth.
