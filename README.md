# Photo Converter Offline

Photo Converter Offline is a lightweight and efficient application that allows users to convert images from any format to JPEG, PNG and WEBP formats without requiring an internet connection.

## Features
- Convert images from all popular formats to JPEG, PNG or WEBP
- Batch processing support for converting multiple images at once.
- Maintain image quality without reducing file size.
- Works entirely offline, ensuring privacy and security.

## Installation

### Windows:
1. Have python installed in your system
2. Make a virtual enviornment
3. Install all dependencies


## Usage
1. Run make_key.py
2. Right click on your image/images -> Convert To -> Choose the format
3. The images will be converted right in that directory
4. To remove the key binding, Run remove_key.py

## Build
1. Install pyinstaller library
2. Run ```pyinstaller --onefile --noconsole --name=run_code run_code.py```
3. Run ```pyinstaller --onefile --name=makekey makekey.py```
4. Run ```pyinstaller --onefile --name=remove_key remove_key.py```

## Requirements
- Windows 10 or later / macOS 10.14 or later / Linux (Ubuntu, Fedora, Arch, etc.)
- Minimum 2GB RAM (4GB recommended)
- At least 100MB of free disk space

## Support
For issues and feature requests, please open an issue on the [GitHub repository](#) or contact support via email at `official.himanshudubey@gmail.com`.

## License
This project is licensed under the [MIT License](LICENSE).

