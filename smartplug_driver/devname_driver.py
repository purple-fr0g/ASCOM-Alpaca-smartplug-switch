from requests import get, HTTPError
import xml.etree.ElementTree as ET

POWERSWITCHLEN = 8
AUTH = "YWRtaW46YWRtaW4=" # 'admin:admin' (b64)

def switch_power(strip_ip: str, outlet_index: int, to_state: bool):
    response = get(
        f"http://{strip_ip}/control_outlet.htm?outlet{outlet_index}=1&op={int(to_state)}&submit=Apply",
        headers={
            "Authorization": f"Basic {AUTH}"
        }
    )

    response.raise_for_status()
    return None

def get_power_status(strip_ip: str):
    response = get(
        f"http://{strip_ip}/control_outlet.htm",
        headers={
            "Authorization": f"Basic {AUTH}"
        }
    )

    response.raise_for_status()
    root = ET.fromstring(response.text)

    plugs = list()
    for i in range(POWERSWITCHLEN):
        plugs.append(root.findall(f"outletStat{i}")[0].text == "on")

    return plugs
