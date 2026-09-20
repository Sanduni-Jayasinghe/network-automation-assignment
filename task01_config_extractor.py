from openpyxl import Workbook

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

# Write extracted records to an Excel file
def write_to_excel(records, output_file):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Extracted Services"

    # Add column headings
    sheet.append(["Main Interface", "Description", "VRF", "Vendor"])

    # Add each extracted record as a row
    for record in records:
        sheet.append([
            record["Main Interface"],
            record["Description"],
            record["VRF"],
            record["Vendor"]
        ])

    workbook.save(output_file)

# Test the function with both sample configuration files
router_a = read_config("configs/router_a.txt")
router_b = read_config("configs/router_b.txt")

# Extract records from both routers
cisco_records = extract_interfaces(router_a)
huawei_records = extract_interfaces(router_b)

# Combine all records into one list
all_records = cisco_records + huawei_records

print("All extracted records:")
for record in all_records:
    print(record)