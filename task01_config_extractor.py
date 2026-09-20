# Read a router configuration file
def read_config(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Detect the router vendor from the configuration content
def detect_vendor(config):
    if "show running-config" in config:
        return "Cisco"
    elif "display current-configuration" in config:
        return "Huawei"
    else:
        return "Unknown"    

# Extract interface details from the configuration
def extract_interfaces(config):
    interfaces = []
    current_interface = None
    vendor = detect_vendor(config)

    for line in config.splitlines():
        line = line.strip()

        if line.startswith("interface "):
            interface_name = line.split(" ", 1)[1]

            current_interface = {
                "Main Interface": interface_name,
                "Description": "",
                "VRF": "",
                "Vendor": vendor
            }

            interfaces.append(current_interface)

        elif line.startswith("description ") and current_interface is not None:
            current_interface["Description"] = line.split(" ", 1)[1]

        elif line.startswith("vrf forwarding ") and current_interface is not None:
            current_interface["VRF"] = line.split(" ", 2)[2]

        elif line.startswith("ip binding vpn-instance ") and current_interface is not None:
            current_interface["VRF"] = line.split(" ", 3)[3]    

    return interfaces

# Test the function with both sample configuration files
router_a = read_config("configs/router_a.txt")
router_b = read_config("configs/router_b.txt")

# Test vendor detection
print("Cisco interfaces:", extract_interfaces(router_a))
print("Huawei interfaces:", extract_interfaces(router_b))