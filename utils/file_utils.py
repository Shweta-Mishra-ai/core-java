"""File and folder system utilities."""

import os

def create_directory(name: str) -> str:
    """Create a folder safely. Works dynamically across Windows, Linux, and macOS."""
    if not name or not name.strip():
        return "Invalid directory name"
    
    clean_name = name.strip()
    try:
        if not os.path.exists(clean_name):
            os.makedirs(clean_name, exist_ok=True)
            return f"Folder '{clean_name}' created successfully."
        else:
            return f"Folder '{clean_name}' already exists."
    except PermissionError:
        return "Permission denied: Unable to create directory."
    except Exception as ex:
        return f"An error occurred: {str(ex)}"
