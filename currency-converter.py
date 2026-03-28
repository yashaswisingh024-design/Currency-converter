import tkinter as tk
from tkinter import messagebox

# Predefined Exchange Rates (Base: INR)
rates = {
    "INR": 1,
    "USD": 0.012,  # 1 INR = 0.012 USD
    "EUR": 0.011   # 1 INR = 0.011 EUR
}

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        if amount <= 0:
            messagebox.showerror("Error", "Please enter a positive amount")
            return

        # Convert to INR first
        amount_in_inr = amount / rates[from_curr]

        # Convert from INR to target currency
        converted_amount = amount_in_inr * rates[to_curr]

        result_label.config(
            text=f"Converted Amount: {round(converted_amount, 2)} {to_curr}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value")


# GUI Window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("350x250")

# Amount Label and Entry
tk.Label(window, text="Enter Amount:").pack(pady=5)
entry_amount = tk.Entry(window)
entry_amount.pack(pady=5)

# From Currency
tk.Label(window, text="From Currency:").pack(pady=5)
from_currency = tk.StringVar()
from_currency.set("INR")
tk.OptionMenu(window, from_currency, "INR", "USD", "EUR").pack(pady=5)

# To Currency
tk.Label(window, text="To Currency:").pack(pady=5)
to_currency = tk.StringVar()
to_currency.set("USD")
tk.OptionMenu(window, to_currency, "INR", "USD", "EUR").pack(pady=5)

# Convert Button
tk.Button(window, text="Convert", command=convert_currency).pack(pady=10)

# Result Label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()