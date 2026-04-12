# ASCOM-Alpaca-smartplug-switch
An implementation of an [ASCOM Alpaca device](https://github.com/ASCOMInitiative/AlpycaDevice/tree/master/device) switch for smartplugs using Alpyca, based on the [switch template](https://github.com/ASCOMInitiative/AlpycaDevice/blob/master/templates/switch.py).

## 1 Setup
To use this Alpaca device with one or more smart plug(s) you need to:
  1. have the corresponding driver in `smartplug_driver/`.
  2. import the module into `switch.py` and add driver into the `supported_devices` dict.
  3. add the smartplug into the `config.toml`

### 1.1 Smartplug Driver
To make this Switch work with your switches you need a python `driver module` for them. 

The current implementation of `switch.py` just uses 2 methods of a `driver module`:
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
### 1.3
- Its important is that the smart plug has the same amount of outlets as it has `[[device.strips.switch]]` entries, as its size is given implicitly by the number of switches specified int the `config.toml`.
- The order of the devices matters as the first device will have `devnum` 0, the 2nd one will have `devnum` 1 etc.
