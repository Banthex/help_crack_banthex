import os
import sys
import platform
import subprocess
import urllib.request
import zipfile
import shutil
import tarfile
import webbrowser
from tqdm import tqdm


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
        binary_url = "https://github.com/Banthex/help_crack_banthex/releases/download/V1.0win/hashcat-6.2.3.with.banthex.exe.zip"
        binary_name = "hashcat-6.2.3.with.banthex.exe.zip"

    # Remove old binary file if it exists
    if os.path.exists(binary_name):
        os.remove(binary_name)

    # Download the binary with progress bar
    with tqdm(unit="B", unit_scale=True, unit_divisor=1024, miniters=1, desc="Downloading Binary") as progress_bar:
        def report(block_num, block_size, total_size):
            progress_bar.total = total_size
            progress_bar.update(block_num * block_size - progress_bar.n)

        urllib.request.urlretrieve(binary_url, binary_name, report)

    if platform.system() == "Windows":
        # Extract the ZIP file
        with zipfile.ZipFile(binary_name, 'r') as zip_ref:
            zip_ref.extractall()

        # Run the executable inside the extracted folder
        extracted_folder = None
        for file in os.listdir():
            if file.lower().startswith("hashcat-6.2.3") and os.path.isdir(file):
                extracted_folder = file
                break

        if extracted_folder is not None:
            os.chdir(extracted_folder)
            executable_name = "help_crack_banthex.exe"  # Update the executable name accordingly

            # Print the contents of the extracted folder
            print("Extracted folder contents:")
            for file in os.listdir():
                print(file)

            try:
                subprocess.run([executable_name], check=True)
            except FileNotFoundError:
                print(f"Error: The file '{executable_name}' does not exist in the extracted folder.")
        else:
            print("Error: Could not find the extracted folder.")

    print("Binary downloaded and executed successfully.")
    print("Please register on banthex.de to get community access, and only with a registered account will your found handshakes be counted on the leaderboard.")
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
