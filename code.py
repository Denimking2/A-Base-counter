import tkinter as tk
from tkinter import messagebox


def hex_to_decimal(hex_num):
    return int(hex_num, 16)


def hex_to_octal(hex_num):
    decimal = int(hex_num, 16)
    return oct(decimal)[2:]


def hex_to_binary(hex_num):
    decimal = int(hex_num, 16)
    return bin(decimal)[2:]


def octal_to_decimal(octal_num):
    return int(octal_num, 8)


def octal_to_hex(octal_num):
    decimal = int(octal_num, 8)
    return hex(decimal)[2:]


def octal_to_binary(octal_num):
    decimal = int(octal_num, 8)
    return bin(decimal)[2:]


def binary_to_decimal(binary_num):
    return int(binary_num, 2)


def binary_to_octal(binary_num):
    decimal = int(binary_num, 2)
    return oct(decimal)[2:]


def binary_to_hex(binary_num):
    decimal = int(binary_num, 2)
    return hex(decimal)[2:]


def decimal_to_hex(decimal_num):
    return hex(int(decimal_num))[2:]


def decimal_to_octal(decimal_num):
    return oct(int(decimal_num))[2:]


def decimal_to_binary(decimal_num):
    return bin(int(decimal_num))[2:]

def convert():
    input_value = entry_input.get().strip()
    input_system = combo_input_system.get()
    output_system = combo_output_system.get()

    try:
        if input_system == "Hexadecimal":
            if output_system == "Decimal":
                result = hex_to_decimal(input_value)
            elif output_system == "Octal":
                result = hex_to_octal(input_value)
            elif output_system == "Binary":
                result = hex_to_binary(input_value)

        elif input_system == "Octal":
            if output_system == "Decimal":
                result = octal_to_decimal(input_value)
            elif output_system == "Hexadecimal":
                result = octal_to_hex(input_value)
            elif output_system == "Binary":
                result = octal_to_binary(input_value)

        elif input_system == "Binary":
            if output_system == "Decimal":
                result = binary_to_decimal(input_value)
            elif output_system == "Octal":
                result = binary_to_octal(input_value)
            elif output_system == "Hexadecimal":
                result = binary_to_hex(input_value)

        elif input_system == "Decimal":
            if output_system == "Hexadecimal":
                result = decimal_to_hex(input_value)
            elif output_system == "Octal":
                result = decimal_to_octal(input_value)
            elif output_system == "Binary":
                result = decimal_to_binary(input_value)

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the selected input system.")

root = tk.Tk()
root.title(" DOHB Number Base Converter")
root.geometry("400x450")
root.configure(bg="#263238")

welcome_label = tk.Label(root,
                         text="Welcome to DOHB,\nfreely convert between various number systems",
                         font=("Arial", 14, "italic"), bg="#263238", fg="#0288d1", justify="center")
welcome_label.pack(pady=20)

label_input_system = tk.Label(root, text="Select Input Number   Base", bg="#263238", font=("Arial", 12), fg="#0288d1")
label_input_system.pack(pady=5)
combo_input_system = tk.StringVar()
input_system_menu = tk.OptionMenu(root, combo_input_system, "Hexadecimal", "Octal", "Binary", "Decimal")
input_system_menu.config(bg="#37474f", font=("Arial", 12), fg="#ffffff")
input_system_menu.pack(pady=5)


label_input = tk.Label(root, text="Enter Number:", bg="#263238", font=("Arial", 12), fg="#0288d1")
label_input.pack(pady=5)
entry_input = tk.Entry(root, font=("Arial", 12), fg="#0288d1", bg="#37474f", insertbackground="white")
entry_input.pack(pady=5)

label_output_system = tk.Label(root, text="Select Output System", bg="#263238", font=("Arial", 12), fg="#0288d1")
label_output_system.pack(pady=5)
combo_output_system = tk.StringVar()
output_system_menu = tk.OptionMenu(root, combo_output_system, "Hexadecimal", "Octal", "Binary", "Decimal")
output_system_menu.config(bg="#37474f", font=("Arial", 12), fg="#ffffff")
output_system_menu.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert, font=("Arial", 12), bg="#0288d1", fg="white")
convert_button.pack(pady=20)

label_result = tk.Label(root, text="Result: ", bg="#263238", font=("Arial", 14), fg="#0288d1")
label_result.pack(pady=5)

root.mainloop()
