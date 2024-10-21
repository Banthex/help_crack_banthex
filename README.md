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
