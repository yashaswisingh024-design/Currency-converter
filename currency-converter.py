import tkinter as tk
from tkinter import ttk, messagebox

# Exchange Rates (Base: INR)
rates = {
    "INR": 1,
    "USD": 0.012,
    "EUR": 0.011,
    "GBP": 0.0095,
    "JPY": 1.8,
    "AUD": 0.018,
    "CAD": 0.016
}

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        if amount <= 0:
            messagebox.showerror("Error", "Enter a positive amount")
            return

        # Convert to INR
        amount_in_inr = amount / rates[from_curr]

        # Convert to target currency
        converted_amount = amount_in_inr * rates[to_curr]

        result_label.config(
            text=f"{amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

def swap_currency():
    from_val = from_currency.get()
    to_val = to_currency.get()
    from_currency.set(to_val)
    to_currency.set(from_val)

def clear_fields():
    entry_amount.delete(0, tk.END)
    result_label.config(text="")

# Main Window
window = tk.Tk()
window.title("Currency Converter 💱")
window.geometry("420x350")
window.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10), padding=5)

# Title
title_label = ttk.Label(window, text="💱 Currency Converter", font=("Segoe UI", 16, "bold"))
title_label.pack(pady=10)

# Amount Entry
ttk.Label(window, text="Enter Amount:").pack(pady=5)
entry_amount = ttk.Entry(window, font=("Segoe UI", 11), justify="center")
entry_amount.pack(pady=5)

# Frame for dropdowns
frame = ttk.Frame(window)
frame.pack(pady=10)

# From Currency
from_currency = tk.StringVar(value="INR")
ttk.Label(frame, text="From").grid(row=0, column=0, padx=15)
from_menu = ttk.Combobox(frame, textvariable=from_currency, values=list(rates.keys()), state="readonly", width=10)
from_menu.grid(row=1, column=0, padx=15)

# To Currency
to_currency = tk.StringVar(value="USD")
ttk.Label(frame, text="To").grid(row=0, column=1, padx=15)
to_menu = ttk.Combobox(frame, textvariable=to_currency, values=list(rates.keys()), state="readonly", width=10)
to_menu.grid(row=1, column=1, padx=15)

# Buttons Frame
btn_frame = ttk.Frame(window)
btn_frame.pack(pady=10)

swap_btn = ttk.Button(btn_frame, text="🔄 Swap", command=swap_currency)
swap_btn.grid(row=0, column=0, padx=5)

convert_btn = ttk.Button(btn_frame, text="Convert", command=convert_currency)
convert_btn.grid(row=0, column=1, padx=5)

clear_btn = ttk.Button(btn_frame, text="Clear", command=clear_fields)
clear_btn.grid(row=0, column=2, padx=5)

# Result Label
result_label = ttk.Label(window, text="", font=("Segoe UI", 12, "bold"), foreground="green")
result_label.pack(pady=15)

# Run App
window.mainloop()
       
