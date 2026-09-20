# Read a router configuration file
def read_config(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Test the function with both sample configuration files
router_a = read_config("configs/router_a.txt")
router_b = read_config("configs/router_b.txt")

print("Router A configuration:")
print(router_a)

print("\nRouter B configuration:")
print(router_b)