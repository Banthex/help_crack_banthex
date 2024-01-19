
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
3. Configure your REST API credentials in `help_crack_mod_bots.py`.

✨ Features

- Leaderboard integration with MySQL on [Banthex.de](https://banthex.de).
- Additional modifications to `help_crack.py` for enhanced functionality.
- Ongoing development and updates by a hobby programmer.

    ℹ️ Please note: The code may not be optimized and does not necessarily follow best practices, as it is developed by a hobby programmer.

Feel free to reach out if you have any questions or need further assistance! 🌟
