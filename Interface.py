import tkinter as tk
from tkinter import filedialog
import os
import subprocess

cables = [
    {
        "name": "HDMI",
        "commonName": "HDMI Cable",
        "officialName": "HDMI (High-Definition Multi-Media Interface) cable",
        "uses": "Used to transmit high-definition audio and video signals between devices such as TVs, monitors, computers, gaming consoles, and a selection of other devices.",
        "originalCreator": "HDMI Licensing Administrator, Inc. (a consortium of companies including Sony, Panasonic, Toshiba, Philips, and others)"
    },
    {
        "name": "ETHERNET",
        "commonName": "Ethernet Cable",
        "officialName": "Ethernet cable (usually categorized by the type of twisted-pair cable used, such as Cat5, Cat6, etc.)",
        "uses": "Ethernet cables are used to connect devices in a local area network (LAN) to enable data transmission between devices, such as computers, routers, switches, and network-attached devices.",
        "originalCreator": "Robert Metcalfe and David Boggs (at Xerox PARC in the 1970s)"
    },
    {
        "name": "USB A",
        "commonName": "USB-A Cable",
        "officialName": "USB (Universal Serial Bus) Type-A cable",
        "uses": "USB-A cables are widely used for connecting various peripherals, such as keyboards, mice, printers, external hard drives, and more, to computers and other devices.",
        "originalCreator": "USB Implementers Forum (USB-IF)"
    },
    {
        "name": "USB C",
        "commonName": "USB-C Cable",
        "officialName": "USB Type-C cable",
        "uses": "USB-C cables are a newer standard of USB cables designed for faster data transfer rates, higher power delivery, and reversible connectors. They are used for charging smartphones, laptops, tablets, and connecting peripherals.",
        "originalCreator": "USB Implementers Forum (USB-IF)"
    },
    {
        "name": "ELECTRICAL",
        "commonName": "Electrical Cable",
        "officialName": "Power cable (various types exist, such as AC power cables, DC power cables, etc.)",
        "uses": "Electrical cables are used to transmit electrical power from a power source (such as a wall outlet) to electrical devices and appliances, providing the necessary energy for operation.",
        "originalCreator": "Electricity has been harnessed and used by humans for various purposes for centuries, so it's challenging to attribute a specific creator."
    },
    {
        "name": "AUDIO",
        "commonName": "Audio Jack",
        "officialName": "3.5mm audio jack (also known as a headphone jack or TRS connector)",
        "uses": "Audio jacks are used for connecting headphones, speakers, microphones, and other audio equipment to devices such as smartphones, tablets, laptops, and audio players.",
        "originalCreator": "The concept of audio connectors dates back to the late 19th century, with various inventors and manufacturers contributing to their development over time. However, the 3.5mm audio jack as we know it today has evolved over the years, and its invention cannot be attributed to a single individual."
    }
]


def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected image:", file_path)
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to GuessImage.py
        #guess_image_script = os.path.join(script_dir, "GuessImage.py")
        guess_image_script = "GuessImage.exe"
        # Call GuessImage.py with the image path as an argument
        #process = subprocess.Popen(["python", guess_image_script, file_path], stdout=subprocess.PIPE,
        process = subprocess.Popen([guess_image_script, file_path], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)
        # Wait for the process to finish
        output, _ = process.communicate()
        output_lines = output.split('\n')
        # Display the output on the screen
        print(output_lines)
        
        found_cables = [cable for cable in cables if cable["name"] == output_lines[0]]

        if found_cables:
            print(f"The string '{output_lines}' is in the list of dictionaries:")
            cable_info_label.config(text=f"Common Name: {found_cables[0]['commonName']}\n"
                                          f"Official Name: {found_cables[0]['officialName']}\n"
                                          f"Uses: {found_cables[0]['uses']}\n"
                                          f"Original Creator: {found_cables[0]['originalCreator']}")
        else:
            print(f"The string '{output_lines}' is not in the list of dictionaries.")
            cable_info_label.config(text="Cable not found")

        # Save the output to a variable
        last_two_lines = '\n'.join(output_lines[-2:]) if len(output_lines) >= 2 else ''
        output_label.config(text=last_two_lines)


# Create the main window
root = tk.Tk()
root.title("Cord Identifier")
root.geometry("800x500")  # Increase the base size of the window

# Create a label for the title
title_label = tk.Label(root, text="Cord Identifier", font=("Arial", 20))
title_label.pack(pady=20)  # Add padding around the title

# Create a button to select an image
select_button = tk.Button(root, text="Select Cord Image", command=select_image)
select_button.pack(pady=20)  # Add padding around the button

# Create a label to display the output
output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack(pady=20)  # Add padding around the output label

# Create a label to display cable information
cable_info_label = tk.Label(root, text="", font=("Arial", 12), justify="left", wraplength=600)
cable_info_label.pack(pady=20)  # Add padding around the cable info label

# Start the GUI event loop
root.mainloop()
