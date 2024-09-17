import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")


for i in range(1, 36):
    # Create a new directory
    new_dir = f'lesson-{str(i)}'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print(f"Directory '{new_dir}' created.")
    else:
        print(f"Directory '{new_dir}' already exists.")

# List all files and directories in the current directory
print("Contents of Current Directory:")
for item in os.listdir(current_dir):
    print(item)
