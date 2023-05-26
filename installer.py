import os
import sys
import platform
import subprocess
import urllib.request
import zipfile
import shutil
import tarfile
import webbrowser
import tkinter as tk
from tkinter import messagebox

class InstallerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Installer")

        self.install_button = tk.Button(master, text="Install", command=self.install)
        self.install_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def install(self):
        # Check if the user is running the script with root privileges
        if os.geteuid() != 0:
            messagebox.showerror("Error", "This script must be run with root privileges.")
            return

        # Check the operating system and perform actions accordingly
        if platform.system() == "Linux":
            self.install_hashcat()
            self.download_binary()
        elif platform.system() == "Windows":
            self.download_binary()
        else:
            messagebox.showerror("Error", "Unsupported operating system.")

    def install_hashcat(self):
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
        try:
            subprocess.run(["make"], check=True)
            subprocess.run(["sudo", "make", "install"], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"{e}")
            sys.exit(1)

        # Return to the main directory
        os.chdir("..")

        # Remove hashcat directory and archive
        shutil.rmtree(hashcat_dir)
        os.remove("hashcat.tar.gz")

        messagebox.showinfo("Success", "Hashcat installed successfully.")

    def download_binary(self):
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
        try:
            urllib.request.urlretrieve(binary_url, binary_name)
        except urllib.error.URLError as e:
            messagebox.showerror("Error", f"{e}")
            sys.exit(1)

        if platform.system() == "Linux":
            # Set executable permissions for Linux binary
            os.chmod(binary_name, 0o755)
            messagebox.showinfo("Success", "Set executable permissions for 'help_crack_banthex'.\nRun with './help_crack_banthex'.")
        else:
            messagebox.showinfo("Success", "Binary downloaded and installed successfully.")

        messagebox.showinfo("Info", "Please register on banthex.de to get community access and only with a registered account will your found handshakes be counted on the leaderboard.")
        webbrowser.open("https://banthex.de/index.php/register/")

root = tk.Tk()
gui = InstallerGUI(root)
root.mainloop()
