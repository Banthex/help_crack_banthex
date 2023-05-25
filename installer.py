import os
import sys
import platform
import subprocess
import urllib.request
import zipfile
import shutil
import tarfile
import webbrowser

def install_hashcat():
    # Download hashcat
    hashcat_url = "https://github.com/hashcat/hashcat/archive/refs/tags/v6.2.3.tar.gz"
    urllib.request.urlretrieve(hashcat_url, "hashcat.tar.gz")

    # Extract hashcat
    with tarfile.open("hashcat.tar.gz", "r:gz") as tar:
        tar.extractall()

    # Navigate to the hashcat directory
    hashcat_dir = "hashcat-6.2.3"
    os.chdir(hashcat_dir)

    # Run make and sudo make install
    subprocess.run(["make"], check=True)
    subprocess.run(["sudo", "make", "install"], check=True)

    # Return to the main directory
    os.chdir("..")
    print("Hashcat installed successfully.")

def download_binary():
    binary_url = ""
    binary_name = ""
    if platform.system() == "Linux":
        binary_url = "https://github.com/Banthex/help_crack_banthex/releases/download/V1.0/help_crack_banthex"
        binary_name = "help_crack_banthex"
    elif platform.system() == "Windows":
        binary_url = "https://github.com/Banthex/help_crack_banthex/releases/download/V1.0win/help_crack_banthex_win64.zip"
        binary_name = "help_crack_banthex.exe"

    # Remove old binary file if it exists
    if os.path.exists(binary_name):
        os.remove(binary_name)

    # Download the binary
    urllib.request.urlretrieve(binary_url, binary_name)

    if platform.system() == "Linux":
        # Set executable permissions for Linux binary
        os.chmod(binary_name, 0o755)
        print("Set executable permissions for 'help_crack_banthex'.")
        print("Run with './help_crack_banthex'.")

    print("Binary downloaded and installed successfully.")
    print("Please register on banthex.de to get community access and only with a registered account will your found handshakes be counted on the leaderboard.")
    webbrowser.open("https://banthex.de/index.php/register/")

# Main script
if __name__ == "__main__":
    # Check the operating system and perform actions accordingly
    if platform.system() == "Linux":
        install_hashcat()
        download_binary()
    elif platform.system() == "Windows":
        download_binary()
    else:
        print("Unsupported operating system.")
