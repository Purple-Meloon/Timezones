import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

# List of world capitals and their corresponding time zones
capitals = {
    "Kabul": "Asia/Kabul",
    "Tirana": "Europe/Tirane",
    "Algiers": "Africa/Algiers",
    "Andorra la Vella": "Europe/Andorra",
    "Luanda": "Africa/Luanda",
    # Add all other world capitals with their respective timezones here
    "Washington, D.C.": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Berlin": "Europe/Berlin",
    "Ankara": "Europe/Istanbul"
    ""
}

# Function to update the time labels
def update_time():
    for city, timezone in capitals.items():
        tz = pytz.timezone(timezone)
        local_time = datetime.now(tz)
        time_string = local_time.strftime('%Y-%m-%d %H:%M:%S')
        time_labels[city].config(text=time_string)
    root.after(1000, update_time)

# Create the main application window
root = tk.Tk()
root.title("World Capitals Clock")
root.geometry("420x480")
root.configure(bg="#2c3e50")

# Create a Canvas and a Scrollbar to hold all the city labels
canvas = tk.Canvas(root, bg="#2c3e50")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Title label
title_label = tk.Label(root, text="World Capitals Clock", font=("Helvetica", 20, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=10)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create labels for each capital and their time
time_labels = {}
for city in capitals.keys():
    frame = tk.Frame(scrollable_frame, bg="#34495e", bd=2, relief="sunken")
    frame.pack(fill='x', padx=10, pady=5)

    city_label = tk.Label(frame, text=city, font=("Helvetica", 14, "bold"), bg="#34495e", fg="#ecf0f1")
    city_label.pack(side='left', padx=10)

    time_labels[city] = tk.Label(frame, text="", font=("Helvetica", 14), bg="#34495e", fg="#ecf0f1")
    time_labels[city].pack(side='right', padx=10)

# Start the time update loop
update_time()

# Run the application
root.mainloop()
