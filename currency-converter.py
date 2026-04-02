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
            text=f"{round(amount,2)} {from_curr} = {round(converted_amount,2)} {to_curr}"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

def swap_currency():
    from_val = from_currency.get()
    to_val = to_currency.get()
    from_currency.set(to_val)
    to_currency.set(from_val)

# Main Window
window = tk.Tk()
window.title("Currency Converter 💱")
window.geometry("400x300")
window.resizable(False, False)

# Style
style = ttk.Style()
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 10))

# Title
title_label = ttk.Label(window, text="Currency Converter 💱", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Amount Entry
ttk.Label(window, text="Enter Amount:").pack(pady=5)
entry_amount = ttk.Entry(window)
entry_amount.pack(pady=5)

# Frame for dropdowns
frame = ttk.Frame(window)
frame.pack(pady=10)

# From Currency
from_currency = tk.StringVar(value="INR")
ttk.Label(frame, text="From").grid(row=0, column=0, padx=10)
from_menu = ttk.Combobox(frame, textvariable=from_currency, values=list(rates.keys()), state="readonly")
from_menu.grid(row=1, column=0, padx=10)

# To Currency
to_currency = tk.StringVar(value="USD")
ttk.Label(frame, text="To").grid(row=0, column=1, padx=10)
to_menu = ttk.Combobox(frame, textvariable=to_currency, values=list(rates.keys()), state="readonly")
to_menu.grid(row=1, column=1, padx=10)

# Swap Button
swap_btn = ttk.Button(window, text="Swap 🔄", command=swap_currency)
swap_btn.pack(pady=5)

# Convert Button
convert_btn = ttk.Button(window, text="Convert", command=convert_currency)
convert_btn.pack(pady=10)

# Result Label
result_label = ttk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run App
window.mainloop()

