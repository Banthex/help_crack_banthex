import subprocess
import threading
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import re
import seaborn as sns
import matplotlib.pyplot as plt

# Function to update the progress value and refresh the progress bar
def update_progress():
    try:
        # Fetch the data from the website with a timeout of 10 seconds
        response = requests.get("https://banthex.de/wpa/?stats", timeout=10)
        data = response.text

        # Parse the HTML data using BeautifulSoup
        soup = BeautifulSoup(data, 'html.parser')

        # Extract the progress bar value from the parsed HTML
        progress_bar_div = soup.find('div', id='progressbar')
        progress_value = float(progress_bar_div.div['style'].split("width: ")[1].split("%;")[0])

        # Update the progress bar value
        progress_bar["value"] = progress_value

        # Update the current keyspace progress value text
        progress_text.set(f"Current Keyspace Progress: {progress_value:.2f}%")

        # Update the status message
        if response.status_code == 200:
            status_text.set("Data successfully fetched. Refresh rate: 5 minutes")
        else:
            status_text.set("Error fetching data. Refresh rate: 5 minutes")

        # Plot the data
        plot_data(data)

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., connection error, timeout)
        status_text.set(f"Error: {str(e)}. Refresh rate: 5 minutes")

    # Schedule the next update after 5 minutes
    root.after(300000, update_progress)


# Function to plot the data
def plot_data(data):
    # Extract the values for plotting
    stats = re.findall(r'([\w\s]+): ([\d.]+)%', data)

    # Separate the data into x and y values
    categories = [stat[0] for stat in stats]
    values = [float(stat[1]) for stat in stats]

    # Create the bar graph using Seaborn
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=values, y=categories, orient="h")
    ax.set_xlabel('Percentage')
    ax.set_ylabel('Category')
    ax.set_title('Statistics')

    # Fix the title for PMKID success rate
    if len(categories) > 0 and categories[0] == 'PMKID success rate':
        ax.set_title('PMKID Success Rate')

    plt.tight_layout()

    # Save the plot as an image
    image_path = "plot.png"
    plt.savefig(image_path)

    # Load the image and display it in the Tkinter window
    img = ImageTk.PhotoImage(Image.open(image_path))
    image_label.configure(image=img)
    image_label.image = img


# Function to run help_crack_banthex.py
def run_help_crack_banthex():
    subprocess.Popen(["python", "help_crack_banthex.py"])


# Create a GUI window
root = tk.Tk()
root.geometry("800x600")
root.title("banthex.de")

# Create and configure the progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
progress_bar.pack(pady=10)

# Create a label for current keyspace progress value text
progress_text = tk.StringVar()
progress_label = tk.Label(root, textvariable=progress_text)
progress_label.pack()

# Create a label for status message
status_text = tk.StringVar()
status_label = tk.Label(root, textvariable=status_text, fg="red")
status_label.pack()

# Create a label for the plot image
image_label = tk.Label(root)
image_label.pack()

# Set initial current keyspace progress value text
progress_text.set("Current Keyspace Progress: 0.00%")

# Set initial status message
status_text.set("")

# Start the initial progress update
update_progress()

# Create a thread to run help_crack_banthex.py
help_crack_thread = threading.Thread(target=run_help_crack_banthex)
help_crack_thread.start()

# Start the GUI main loop
root.mainloop()
