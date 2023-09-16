import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        status_label.config(text="Status: Playing")
        paused = False
    else:
        pygame.mixer.music.load(selected_file)
        pygame.mixer.music.play()
        status_label.config(text="Status: Playing")

def pause_music():
    global paused
    pygame.mixer.music.pause()
    status_label.config(text="Status: Paused")
    paused = True

def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Status: Stopped")

def set_volume(volume):
    pygame.mixer.music.set_volume(volume)

def choose_file():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])

def change_volume(value):
    volume = float(value) / 100
    set_volume(volume)


# Initialize pygame
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.geometry("375x700")
root.resizable(False,False)
root.title("MP3 Player")
image = tk.PhotoImage(file="./idiot.png")
label = tk.Label(root, image=image)
label.pack()

# Create buttons
select_button = tk.Button(root, text="Select Music", command=choose_file)
play_button = tk.Button(root, text="Play", command=play_music)
pause_button = tk.Button(root, text="Pause", command=pause_music)
stop_button = tk.Button(root, text="Stop", command=stop_music)

# Create a volume slider
volume_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=change_volume)
volume_slider.set(50)  # Set initial volume to 50%

# Create a status label
status_label = tk.Label(root, text="Status: Stopped")

# Position widgets
select_button.pack(pady=10)
play_button.pack(pady=5)
pause_button.pack(pady=5)
stop_button.pack(pady=5)
volume_slider.pack(pady=10)
status_label.pack(pady=5)

# Global variable to track if music is paused
paused = False

# Start the GUI main loop
root.mainloop()
