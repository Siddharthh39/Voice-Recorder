import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(duration_seconds, filename="out.wav", sample_rate=44100, channels=2):
    try:
        print(f"Recording for {duration_seconds} seconds...")
        recorded_audio = sd.rec(int(duration_seconds * sample_rate), samplerate=sample_rate, channels=channels)
        sd.wait()
        write(filename, sample_rate, recorded_audio)
        print(f"Recording finished. Saved as {filename}")
        messagebox.showinfo("Recording Finished", f"Recording finished. Saved as {filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def start_recording():
    duration_seconds = int(duration_entry.get())
    filename = filename_entry.get().strip() or "out.wav"
    record_audio(duration_seconds, filename)

root = tk.Tk()
root.title("Audio Recorder")

duration_label = tk.Label(root, text="Duration (seconds):")
duration_label.grid(row=0, column=0, padx=10, pady=5)
duration_entry = tk.Entry(root)
duration_entry.grid(row=0, column=1, padx=10, pady=5)

filename_label = tk.Label(root, text="Filename:")
filename_label.grid(row=1, column=0, padx=10, pady=5)
filename_entry = tk.Entry(root)
filename_entry.grid(row=1, column=1, padx=10, pady=5)

record_button = tk.Button(root, text="Record", command=start_recording)
record_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
