import winreg as reg
import admin_priv

# Ask for admin privileges
admin_priv.run_as_admin()

def delete_registry_key(root, key_path):
    """ Recursively delete a registry key and all its subkeys. """
    try:
        with reg.OpenKey(root, key_path, 0, reg.KEY_READ | reg.KEY_WRITE) as key:
            while True:
                try:
                    subkey_name = reg.EnumKey(key, 0)  # Get first subkey
                    delete_registry_key(root, f"{key_path}\\{subkey_name}")  # Recursively delete
                except OSError:
                    break  # No more subkeys, exit loop

        reg.DeleteKey(root, key_path)  # Delete the main key after subkeys are removed
        print(f"Deleted: {key_path}")
    except FileNotFoundError:
        pass  # Ignore if not found
    except Exception as e:
        print(f"Error deleting {key_path}: {e}")

# Image file extensions
image_extensions = [
    ".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".tif",
    ".webp", ".ico", ".jfif", ".svg", ".heic", ".heif", ".raw",
    ".psd", ".ai", ".indd", ".eps",".avif"
]

try:
    for ext in image_extensions:
        base_key_path = f"SystemFileAssociations\\{ext}\\Shell\\ConvertTo"
        delete_registry_key(reg.HKEY_CLASSES_ROOT, base_key_path)

    print("Context menu removed successfully!")
except Exception as e:
    print(f"Error: {e}")
