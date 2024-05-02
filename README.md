This is a simple audio recorder application built using Python's Tkinter library for the GUI, sounddevice for audio recording, and scipy.io.wavfile for saving the recorded audio as a WAV file.

Features:
Allows users to specify the duration of the recording in seconds.
Users can enter a custom filename for the recorded audio or use the default filename "out.wav".
Displays a message box with information about the recording status and the filename after the recording is finished.
Handles errors gracefully and displays error messages using message boxes.

Instructions:
Enter the duration of the recording in seconds in the "Duration (seconds)" field.
Optionally, specify a custom filename for the recorded audio in the "Filename" field.
Click the "Record" button to start the recording.
After the recording is finished, a message box will display the recording status and the filename where the audio is saved.

Dependencies:
Python 3.x
Tkinter
sounddevice
scipy
