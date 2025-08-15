import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import font

def lighten_color(color, factor=0.1):
    """
    Lightens an RGB color by a given factor.
    """
    return tuple(min(255, int(c + (255 - c) * factor)) for c in color)

def darken_color(color, factor=0.1):
    """
    Darkens an RGB color by a given factor.
    """
    return tuple(max(0, int(c * (1 - factor))) for c in color)

def rgb_to_hex(rgb):
    """
    Converts an RGB tuple to a hexadecimal color code.
    """
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def create_color_label(parent, hex_code, text_color):
    """
    Creates and returns a styled label for a color shade.
    """
    label = tk.Label(parent, text=hex_code, bg=hex_code, fg=text_color,
                     font=("Helvetica", 10, "bold"), relief=tk.RAISED, bd=2,
                     width=15, height=2)
    return label

def choose_color():
    
    color_code = colorchooser.askcolor(title="Choose a color")
    if color_code[0] is None:
        return

    rgb = tuple(map(int, color_code[0]))
    hex_code = rgb_to_hex(rgb)

    
    brightness = (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000
    text_color = 'white' if brightness < 128 else 'black'

    
    color_label.config(text=f"HEX: {hex_code}\nRGB: {rgb}", bg=hex_code, fg=text_color)
    color_label.config(font=font.Font(size=12, weight='bold'))

    
    for widget in shades_frame.winfo_children():
        widget.destroy()

    
    lighter_frame = tk.Frame(shades_frame, bg="#f0f0f0")
    lighter_frame.pack(pady=5, padx=10)
    tk.Label(lighter_frame, text="Lighter Shades", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack()
    lighter_shades_subframe = tk.Frame(lighter_frame, bg="#f0f0f0")
    lighter_shades_subframe.pack()

    
    for i in range(1, 6):
        shade_rgb = lighten_color(rgb, i * 0.15)
        shade_hex = rgb_to_hex(shade_rgb)
        shade_text_color = 'white' if ((shade_rgb[0] * 299 + shade_rgb[1] * 587 + shade_rgb[2] * 114) / 1000) < 128 else 'black'
        create_color_label(lighter_shades_subframe, shade_hex, shade_text_color).pack(side=tk.LEFT, padx=5, pady=5)

    
    darker_frame = tk.Frame(shades_frame, bg="#f0f0f0")
    darker_frame.pack(pady=5, padx=10)
    tk.Label(darker_frame, text="Darker Shades", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack()
    darker_shades_subframe = tk.Frame(darker_frame, bg="#f0f0f0")
    darker_shades_subframe.pack()

    
    for i in range(1, 6):
        shade_rgb = darken_color(rgb, i * 0.15)
        shade_hex = rgb_to_hex(shade_rgb)
        shade_text_color = 'white' if ((shade_rgb[0] * 299 + shade_rgb[1] * 587 + shade_rgb[2] * 114) / 1000) < 128 else 'black'
        create_color_label(darker_shades_subframe, shade_hex, shade_text_color).pack(side=tk.LEFT, padx=5, pady=5)



root = tk.Tk()
root.title("🎨 Color Palette Generator")
root.geometry("800x450")
root.config(bg="#f0f0f0")


title_font = font.Font(family="Helvetica", size=24, weight="bold")
button_font = font.Font(family="Helvetica", size=14, weight="bold")

title_label = tk.Label(root, text="🎨 Color Palette Generator 🎨", font=title_font, bg="#f0f0f0", fg="#333")
title_label.pack(pady=(20, 10))

pick_button = tk.Button(root, text="Pick a Color", command=choose_color, font=button_font, bg="#6a1b9a", fg="white",
                        activebackground="#4a148c", activeforeground="white", relief=tk.RAISED, bd=3)
pick_button.pack(pady=15, ipadx=20, ipady=10)

color_label = tk.Label(root, text="HEX: \nRGB:", font=("Helvetica", 14), bg="white",
                       width=30, height=4, relief=tk.GROOVE, bd=2)
color_label.pack(pady=10)

shades_frame = tk.Frame(root, bg="#f0f0f0")
shades_frame.pack(pady=10)


root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

root.mainloop()