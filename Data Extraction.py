import re
import tkinter as tk
from tkinter import ttk

def extract_time():
    extract_information(r'\b\d{1,2}:\d{2}(?::\d{2})?\s*(?:AM|PM)?\b', "Time")

def extract_postal_codes():
    extract_information(r'\b\d{5}(?:-\d{4})?\b', "Postal Codes")

def extract_hashtags():
    extract_information(r'#\w+', "Hashtags")

def extract_currency():
    extract_information(r'\$\d+(?:\.\d{2})?', "Currency")

def extract_emails():
    extract_information(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', "Emails")

def extract_urls():
    extract_information(r'\bhttps?://\S+\b', "URLs")

def extract_phone_numbers():
    extract_information(r'\b\d{3}-\d{3}-\d{4}\b', "Phone Numbers")

def extract_ip_addresses():
    extract_information(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', "IP Addresses")

def extract_information(pattern, info_type):
    text = text_entry.get("1.0", tk.END)
    matches = re.findall(pattern, text)
    output_text.delete(1.0, tk.END)
    if matches:
        output_text.insert(tk.END, f"Extracted {info_type}:\n")
        for match in matches:
            output_text.insert(tk.END, f"{match}\n")
    else:
        output_text.insert(tk.END, f"No {info_type} found.")

root = tk.Tk()
root.title("Text Information Extractor")

text_label = ttk.Label(root, text="Enter text:")
text_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

text_entry = tk.Text(root, height=10, width=50)
text_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

buttons_frame = ttk.Frame(root)
buttons_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

time_button = ttk.Button(buttons_frame, text="Extract Time", command=extract_time)
time_button.grid(row=0, column=0, padx=5, pady=5)

postal_button = ttk.Button(buttons_frame, text="Extract Postal Codes", command=extract_postal_codes)
postal_button.grid(row=0, column=1, padx=5, pady=5)

hashtag_button = ttk.Button(buttons_frame, text="Extract Hashtags", command=extract_hashtags)
hashtag_button.grid(row=0, column=2, padx=5, pady=5)

currency_button = ttk.Button(buttons_frame, text="Extract Currency", command=extract_currency)
currency_button.grid(row=1, column=0, padx=5, pady=5)

email_button = ttk.Button(buttons_frame, text="Extract Emails", command=extract_emails)
email_button.grid(row=1, column=1, padx=5, pady=5)

url_button = ttk.Button(buttons_frame, text="Extract URLs", command=extract_urls)
url_button.grid(row=1, column=2, padx=5, pady=5)

phone_button = ttk.Button(buttons_frame, text="Extract Phone Numbers", command=extract_phone_numbers)
phone_button.grid(row=2, column=0, padx=5, pady=5)

ip_button = ttk.Button(buttons_frame, text="Extract IP Addresses", command=extract_ip_addresses)
ip_button.grid(row=2, column=1, padx=5, pady=5)

output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

root.mainloop()
