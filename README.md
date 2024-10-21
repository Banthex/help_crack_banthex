# 🚀 Public Version of help_crack_banthex

This is a modified version of `help_crack.py` from [WPA-SEC](https://wpa-sec.stanev.org/), enhanced with features for the Banthex community and leaderboard integration. This version allows cracking hashes from [WPA-SEC](https://wpa-sec.stanev.org/). Additionally, found handshakes are tracked on the leaderboard at [Banthex.de](https://banthex.de).

## 📥 Installation

### Automatic Installation

1. Download the installer script: [https://github.com/Banthex/help_crack_banthex/blob/master/installer.py](https://github.com/Banthex/help_crack_banthex/blob/master/installer.py).
2. Execute `pip install tqdm` if necessary.
3. Run `installer.py` to automatically download and install the required dependencies.
4. Run `chmod a+x help_crack_banthex`.
5. Start the program with `./help_crack_banthex`.

### Manual Installation (Currently not functional, as specific parameters in the source code need to be adjusted for your server!)

1. Clone the repository:
   ```shell
   git clone https://github.com/Banthex/help_crack_banthex
   ```
2. Install the required dependencies:
   ```shell
   pip install -r /help_crack_banthex/requirements.txt
   ```
3. Configure your REST API credentials in `help_crack_banthex`.

### Custom Installation Path

You can specify a custom installation path during the installation process. When running the installer script, you will be prompted to enter a custom installation path. If you provide a path, the script will install the necessary files in the specified location. If no path is provided, the default installation path will be used.

### macOS Support

The installer script now includes support for macOS. Follow the same installation steps as mentioned above to install the required dependencies and set up the program on macOS.

### Selecting Version to Install

The installer script now includes an option to select the version of Hashcat to install. When running the installer script, you will be prompted to select the version you want to install. The available options are "latest", "v6.2.3", and "v6.2.2". The script will download and install the selected version.

### Selecting Release Version

The installer script now includes an option to select the release version for `https://github.com/Banthex/help_crack_banthex/releases`. When running the installer script, you will be prompted to select the release version you want to install. The available options are fetched dynamically from the GitHub API. If the fetch fails, a fallback list of versions will be provided. The script will download and install the selected release version.

### Displaying Asset Name

The installer script now includes an option to display the full asset name of the selected version. When running the installer script, the full asset name will be displayed in a label, a tooltip, and a message box. The label will be updated with the full asset name when the user selects a version. The tooltip will be displayed when the user hovers over the version selection dropdown. The message box will be displayed when the user selects a version.

## ✨ Features

- Leaderboard integration with MySQL on [Banthex.de](https://banthex.de).
- Additional modifications to `help_crack_banthex.py` for enhanced functionality.
- Ongoing development and updates by a hobby programmer.

## 🏆 Leaderboard Integration

To participate in the leaderboard and have your found handshakes tracked, please follow these steps:

1. Register for an account on [Banthex.de](https://banthex.de/index.php/register/).
2. Use your registered username when prompted by the `help_crack_banthex.py` script.
3. Your found handshakes will be automatically submitted and tracked on the leaderboard.

ℹ️ Please note: The code may not be optimized and does not necessarily follow best practices, as it is developed by a hobby programmer.

## ℹ️ Additional Information

- This change only adds credits to a leaderboard.
- The script works with the Stanev website.
- The MySQL for hashes is on WPA-SEC, not on Banthex.de. Only the leaderboard is on Banthex.de.

## 🔧 Setting Maximum GPU Temperature

To set the maximum GPU temperature, follow these steps:

1. When prompted, choose whether to disable hardware monitoring.
2. If you choose not to disable hardware monitoring, you will be prompted to enter the maximum GPU temperature (in degrees Celsius).
3. The script will use the `--gpu-temp-abort` option with the value you provide to set the maximum GPU temperature.

Feel free to reach out if you have any questions or need further assistance! 🌟
