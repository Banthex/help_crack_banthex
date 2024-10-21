import os
import sys
import platform
import subprocess
import urllib.request
import zipfile
import shutil
import webbrowser
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import json

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

        self.custom_path_label = tk.Label(master, text="Custom Installation Path (optional):", bg="black", fg="white")
        self.custom_path_label.pack(pady=5)
        self.custom_path_entry = tk.Entry(master, width=50)
        self.custom_path_entry.pack(pady=5)

        self.version_label = tk.Label(master, text="Select Version to Install:", bg="black", fg="white")
        self.version_label.pack(pady=5)
        self.version_var = tk.StringVar(master)
        self.version_var.set("V1.1_Linux")
        self.version_menu = tk.OptionMenu(master, self.version_var, "V1.1_Linux", "v6.2.3")  # Add more versions as needed
        self.version_menu.pack(pady=5)

        self.asset_name_label = tk.Label(master, text="", bg="black", fg="white")
        self.asset_name_label.pack(pady=5)

        self.version_var.trace("w", self.update_asset_name)

        self.version_menu.bind("<Enter>", self.show_tooltip)
        self.version_menu.bind("<Leave>", self.hide_tooltip)

        self.tooltip = tk.Label(master, text="", bg="yellow", fg="black", bd=1, relief="solid", padx=5, pady=2)
        self.tooltip.pack_forget()

        self.hashcat_version_label = tk.Label(master, text="", bg="black", fg="white")
        self.hashcat_version_label.pack(pady=5)

        self.fetch_versions()
        self.check_hashcat_version()

    def open_register(self):
        webbrowser.open("https://banthex.de/index.php/register/")

    def install(self):
        custom_path = self.custom_path_entry.get()
        if custom_path and not os.path.exists(custom_path):
            os.makedirs(custom_path)

        if platform.system() == "Linux":
            if os.geteuid() != 0:
                messagebox.showerror("Error", "This script must be run with root privileges.")
                return
            self.download_linux_binary(custom_path)
        elif platform.system() == "Windows":
            self.download_binary(custom_path)
        elif platform.system() == "Darwin":
            self.install_hashcat_mac(custom_path)
        else:
            messagebox.showerror("Error", "Unsupported operating system.")

    def download_linux_binary(self, custom_path):
        version = self.version_var.get()
        binary_url = f"https://github.com/Banthex/help_crack_banthex/releases/download/{version}/help_crack_banthex"
        binary_name = "help_crack_banthex"

        # Download the binary
        def progress_callback(count, block_size, total_size):
            percent = int(count * block_size * 100 / total_size)
            self.progress_bar["value"] = percent
            self.progress_bar.update()

        try:
            urllib.request.urlretrieve(binary_url, binary_name, progress_callback)
        except urllib.error.URLError as e:
            messagebox.showerror("Error", f"Failed to download Linux binary: {e}")
            return

        # Move to custom path if specified
        if custom_path:
            shutil.move(binary_name, os.path.join(custom_path, binary_name))
            binary_path = os.path.join(custom_path, binary_name)
        else:
            binary_path = binary_name

        # Make the binary executable
        os.chmod(binary_path, 0o755)

        messagebox.showinfo("Success", "Linux binary downloaded and installed successfully.")
        messagebox.showinfo("Info", "You can run the binary using './help_crack_banthex' from the installation directory.")

    def download_binary(self, custom_path):
        version = self.version_var.get()
        if version == "V1.1_Linux":
            binary_url = "https://github.com/Banthex/help_crack_banthex/releases/download/V1.1_Linux/help_crack_banthex"
        else:
            binary_url = f"https://github.com/Banthex/help_crack_banthex/releases/download/{version}/hashcat-windows.zip"
        binary_name = "help_crack_banthex.zip"

        if os.path.exists(binary_name):
            os.remove(binary_name)

        def progress_callback(count, block_size, total_size):
            percent = int(count * block_size * 100 / total_size)
            self.progress_bar["value"] = percent
            self.progress_bar.update()

        try:
            urllib.request.urlretrieve(binary_url, binary_name, progress_callback)
        except urllib.error.URLError as e:
            messagebox.showerror("Error", f"Failed to download binary: {e}")
            return

        try:
            with zipfile.ZipFile(binary_name, 'r') as zip_ref:
                zip_ref.extractall(custom_path if custom_path else ".")
        except zipfile.BadZipFile as e:
            messagebox.showerror("Error", f"Failed to extract binary: {e}")
            return

        os.remove(binary_name)

        messagebox.showinfo("Success", "Binary downloaded and installed successfully.")
        messagebox.showinfo("Info", "Please register on banthex.de to get community access and only with a registered account will your found handshakes be counted on the leaderboard.")
        webbrowser.open("https://banthex.de/index.php/register/")

    def install_hashcat_mac(self, custom_path):
        version = self.version_var.get()
        if version == "latest":
            hashcat_url = "https://github.com/hashcat/hashcat/archive/refs/tags/latest.tar.gz"
        else:
            hashcat_url = f"https://github.com/hashcat/hashcat/releases/tag/{version}"
        try:
            urllib.request.urlretrieve(hashcat_url, "hashcat.tar.gz")
        except urllib.error.URLError as e:
            messagebox.showerror("Error", f"Failed to download Hashcat: {e}")
            return

        try:
            with tarfile.open("hashcat.tar.gz", "r:gz") as tar:
                tar.extractall()
        except tarfile.TarError as e:
            messagebox.showerror("Error", f"Failed to extract Hashcat: {e}")
            return

        hashcat_dir = f"hashcat-{version}" if version != "latest" else "hashcat-latest"
        os.chdir(hashcat_dir)

        try:
            subprocess.run(["make"], check=True)
            subprocess.run(["sudo", "make", "install"], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"{e}")
            sys.exit(1)

        os.chdir("..")
        shutil.rmtree(hashcat_dir)
        os.remove("hashcat.tar.gz")

        messagebox.showinfo("Success", "Hashcat installed successfully.")

    def update_asset_name(self, *args):
        version = self.version_var.get()
        asset_name = f"Selected Asset: {version}_Linux.zip"
        self.asset_name_label.config(text=asset_name)

    def fetch_versions(self):
        versions = []
        page = 1
        while True:
            response = requests.get(f"https://api.github.com/repos/Banthex/help_crack_banthex/releases?per_page=100&page={page}")
            if response.status_code == 200:
                releases = response.json()
                if not releases:  # No more releases
                    break
                versions.extend(release["tag_name"] for release in releases)
                page += 1
            else:
                messagebox.showerror("Error", f"Failed to fetch versions: {response.status_code}")
                return

        # Update the version menu with all fetched versions
        self.version_menu["menu"].delete(0, "end")
        for version in versions:
            self.version_menu["menu"].add_command(label=version, command=tk._setit(self.version_var, version))
        self.version_var.set(versions[0])  # Set the first version as default

    def show_tooltip(self, event):
        self.tooltip.config(text="Choose a version to download and install.")
        self.tooltip.pack()

    def hide_tooltip(self, event):
        self.tooltip.pack_forget()

    def check_hashcat_version(self):
        try:
            result = subprocess.run(["hashcat", "-V"], capture_output=True, text=True)
            if result.returncode == 0:
                version = result.stdout.strip()
                self.hashcat_version_label.config(text=f"Installed Hashcat Version: {version}")
            else:
                self.hashcat_version_label.config(text="Hashcat is not installed.")
        except FileNotFoundError:
            self.hashcat_version_label.config(text="Hashcat is not installed.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = InstallerGUI(root)
    root.mainloop()
