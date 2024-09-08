import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Import ttk for themed widgets
import moviepy.editor as mp

class AudioExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Audio Extractor")
        self.root.geometry("400x200")

        self.select_video_button = tk.Button(root, text="Select Video", command=self.select_video, font=("Arial", 12),justify=tk.CENTER,bg='skyblue')
        self.select_video_button.grid(row=0, column=0, padx=20, pady=20)

      

    def select_video(self):
        video_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
        if video_path:
            self.extract_audio(video_path)

    def extract_audio(self, video_path):
        try:
            video = mp.VideoFileClip(video_path)
            audio_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
            if audio_path:
                
                video.audio.write_audiofile(audio_path)
                
                messagebox.showinfo("Success", "Audio extracted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()

# Create an instance of the AudioExtractor class
extractor = AudioExtractor(root)

# Start the GUI
root.mainloop()
