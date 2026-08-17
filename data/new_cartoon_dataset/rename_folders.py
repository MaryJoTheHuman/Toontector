# This program will rename the class folders so that they don't have spaces.
# Make sure this file is in the same directory as the folders you want to rename.
import os
for folder in os.listdir():
    if os.path.isdir(folder) and " " in folder:
        # Replace spaces with underscores
        new_name = folder.replace(" ", "_")
        # Capitalize the first letter after each underscore
        new_name = "_".join(
            word.capitalize()
            for word in new_name.split("_")
        )
        os.rename(folder, new_name)
        print(f"{folder} -> {new_name}")
    # Skips folders that are already formatted
    elif os.path.isdir(folder):
        print(f"Skipping: {folder}")
print("Done!")