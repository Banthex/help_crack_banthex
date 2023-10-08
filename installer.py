import os
import sys
import platform
import subprocess
import urllib.request
import zipfile
import tarfile
import shutil
import webbrowser
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class InstallerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Installer")
        master.configure(bg="black")

        self.install_button = tk.Button(master, text="Install", command=self.install, bg="red", fg="white")
        self.install_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, bg="red", fg="white")
        self.quit_button.pack()

        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.info_label = tk.Label(master, text="Please register on banthex.de to get community access and only with a registered account will your found handshakes be counted on the leaderboard.", bg="black", fg="white")
        self.info_label.pack(pady=10)

        self.register_button = tk.Button(master, text="Register", command=self.open_register, bg="red", fg="white")
        self.register_button.pack()

    def open_register(self):
        webbrowser.open("https://banthex.de/index.php/register/")

    def install(self):
        # Check the operating system and perform actions accordingly
        if platform.system() == "Linux":
            # Check if the user is running the script with root privileges
            if os.geteuid() != 0:
                messagebox.showerror("Error", "This script must be run with root privileges.")
                return

            self.install_hashcat()
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
        binary_url = "https://github.com/Banthex/help_crack_banthex/releases/download/V1.0win/hashcat-6.2.3.with.banthex.exe.zip"
        binary_name = "hashcat-6.2.3.with.banthex.exe.zip"

        # Remove old binary file if it exists
        if os.path.exists(binary_name):
            os.remove(binary_name)

        # Download the binary with progress bar
        def progress_callback(count, block_size, total_size):
            percent = int(count * block_size * 100 / total_size)
            self.progress_bar["value"] = percent
            self.progress_bar.update()

        try:
            urllib.request.urlretrieve(binary_url, binary_name, progress_callback)
        except urllib.error.URLError as e:
            messagebox.showerror("Error", f"{e}")
            sys.exit(1)

        # Extract the binary
        with zipfile.ZipFile(binary_name, 'r') as zip_ref:
            zip_ref.extractall()

        # Remove the zip file
        os.remove(binary_name)

        messagebox.showinfo("Success", "Binary downloaded and installed successfully.")

        messagebox.showinfo("Info", "Please register on banthex.de to get community access and only with a registered account will your found handshakes be counted on the leaderboard.")
        webbrowser.open("https://banthex.de/index.php/register/")

root = tk.Tk()
gui = InstallerGUI(root)
root.mainloop()
