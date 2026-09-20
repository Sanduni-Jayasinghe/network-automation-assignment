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

# Test the function with both sample configuration files
router_a = read_config("configs/router_a.txt")
router_b = read_config("configs/router_b.txt")

# Test vendor detection
print("Router A Vendor:", detect_vendor(router_a))
print("Router B Vendor:", detect_vendor(router_b))