import os
import sys
import winreg as reg
import admin_priv

# Ask for admin privileges
admin_priv.run_as_admin()

# Get paths
#script_path = os.path.abspath("run_code.py")  # Path to your conversion script
#python_exe = sys.executable  # Ensure it's python.exe, not pythonw.exe
python_exe= sys.executable.replace("python.exe", "pythonw.exe")
script_dir = os.path.dirname(os.path.abspath(sys.executable))  # Get the bundled EXE directory
script_path = os.path.join(script_dir, "run_code.exe")
# Image file extensions
image_extensions = [
    ".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".tif",
    ".webp", ".ico", ".jfif", ".svg", ".heic", ".heif", ".raw",
    ".psd", ".ai", ".indd", ".eps",".avif"
]
# image_extensions = [
#     ".jpg", ".jpeg"
# ]

try:
    for ext in image_extensions:
        base_key_path = f"SystemFileAssociations\\{ext}\\shell\\ConvertTo"

        # Create "Convert to" main menu
        base_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, base_key_path)
        reg.SetValueEx(base_key, "MUIVerb", 0, reg.REG_SZ,
                       "Convert to")  # Proper submenu label
        reg.SetValueEx(base_key, "SubCommands", 0, reg.REG_SZ,
                       "")  # Enables sub-menu behavior

        # Create sub-menus
        formats = {
            "toPNG": "png",
            "toJPEG": "jpeg",
            "toWEBP": "webp"
        }

        for sub_key_name, fmt in formats.items():
            sub_key_path = f"{base_key_path}\\shell\\{sub_key_name}"
            sub_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, sub_key_path)
            reg.SetValue(sub_key, "", reg.REG_SZ,
                         sub_key_name.replace('to', 'to '))  # Label

            # Command key
            command_key = reg.CreateKey(sub_key, "command")
            reg.SetValue(command_key, "", reg.REG_SZ,
                         f'"{script_path}" "{fmt}" "%1"')

            reg.CloseKey(sub_key)
            reg.CloseKey(command_key)

        reg.CloseKey(base_key)

    print("Sub-context menu added successfully!")
except Exception as e:
    print(f"Error: {e}")
