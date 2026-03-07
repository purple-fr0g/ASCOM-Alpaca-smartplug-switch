from requests import get
import xml.etree.ElementTree as ET
import re

POWERSWITCHLEN = 4

def switch_power(addr: str, outlet_index: int, to_state: bool) -> None:
    response = get(f"http://{addr}/hidden.htm?M0:O{outlet_index+1}={"ON" if to_state else "OFF"}")

    response.raise_for_status()
    return None

def get_power_status(addr: str) -> list[bool]:
    response = get(f"http://{addr}/hidden.htm")
    response.raise_for_status()
    plugs = list()

    for line in response.iter_lines():
        pattern = r'M0:(O\d)=(On|Off)'
        match = re.match(pattern, line.decode('utf-8'))
        if match:
            status = match.group(2)
            plugs.append(True if status == "On" else False)

    return plugs
