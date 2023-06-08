import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter.scrolledtext as st

def copy_latitude():
    latitude = latitude_result_text.get(1.0, tk.END).strip()
    window.clipboard_clear()
    window.clipboard_append(latitude)

def copy_longitude():
    longitude = longitude_result_text.get(1.0, tk.END).strip()
    window.clipboard_clear()
    window.clipboard_append(longitude)

def calculate_coordinates(event=None):
    try:
        lat_deg = float(entry_boxes[0].get())
        lat_min = float(entry_boxes[1].get() or 0)
        lat_sec = float(entry_boxes[2].get() or 0)
        lon_deg = float(entry_boxes[3].get())
        lon_min = float(entry_boxes[4].get() or 0)
        lon_sec = float(entry_boxes[5].get() or 0)

        lat_deg += lat_min / 60. + lat_sec / 3600.
        lon_deg += lon_min / 60. + lon_sec / 3600.

        latitude_result_text.delete(1.0, tk.END)
        latitude_result_text.insert(tk.END, f"{lat_deg}")

        longitude_result_text.delete(1.0, tk.END)
        longitude_result_text.insert(tk.END, f"{lon_deg}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("Coordinates Calculator")

# Create input entry boxes
labels = ["Latitude (deg):", "Latitude (min):", "Latitude (sec):", "Longitude (deg):", "Longitude (min):", "Longitude (sec):"]
entry_boxes = []
for i, label_text in enumerate(labels):
    label = tk.Label(window, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5)

    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry_boxes.append(entry)

    # Bind Enter key to calculate_coordinates function
    entry.bind("<Return>", calculate_coordinates)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_coordinates)
calculate_button.grid(row=len(entry_boxes), column=0, columnspan=2, padx=10, pady=10)

# Create latitude result text widget
latitude_result_text = st.ScrolledText(window, height=1, width=20)
latitude_result_text.grid(row=len(entry_boxes) + 1, column=0, padx=10, pady=5)

# Create longitude result text widget
longitude_result_text = st.ScrolledText(window, height=1, width=20)
longitude_result_text.grid(row=len(entry_boxes) + 1, column=1, padx=10, pady=5)

# Create copy latitude button
copy_latitude_button = ttk.Button(window, text="Copy Latitude", command=copy_latitude)
copy_latitude_button.grid(row=len(entry_boxes) + 2, column=0, padx=10, pady=5)

# Create copy longitude button
copy_longitude_button = ttk.Button(window, text="Copy Longitude", command=copy_longitude)
copy_longitude_button.grid(row=len(entry_boxes) + 2, column=1, padx=10, pady=5)

# Start the GUI event loop
window.mainloop()
