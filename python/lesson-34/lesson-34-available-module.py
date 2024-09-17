# Import the sys module
import sys

# List all available modules
available_modules = sys.modules.keys()

# Display the first 10 modules for demonstration
print("Available Modules:")
for module in list(available_modules)[:10]:
    print(module)
