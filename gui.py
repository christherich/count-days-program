import tkinter as tk
import countdays
from tkinter import *
import customtkinter


def count_days():
    start_str = start_entry.get()
    end_str = end_entry.get()
    days = countdays.count_days(start_str, end_str)
    result_label.configure(
        text=f"There are {days} days between {start_str} and {end_str}.")


# create the GUI
# root = tk.Tk()
root = customtkinter.CTk()
root.title("Count Days")
root.resizable(width=False, height=False)

start_label = customtkinter.CTkLabel(
    root, text="  Starting date (YYYY-MM-DD):")
start_label.grid(row=0, column=0)
start_entry = customtkinter.CTkEntry(root)
start_entry.grid(row=0, column=1)

end_label = customtkinter.CTkLabel(root, text="   Ending date (YYYY-MM-DD):")
end_label.grid(row=1, column=0)
end_entry = customtkinter.CTkEntry(root)
end_entry.grid(row=1, column=1)

calculate_button = customtkinter.CTkButton(
    root, text="Calculate", command=count_days)
calculate_button.grid(row=2, column=0)

result_label = customtkinter.CTkLabel(root, text="")
result_label.grid(row=2, column=1)

root.mainloop()
