import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Import ttk for themed widgets
import moviepy.editor as mp

class AudioExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Audio Extractor")
        self.root.geometry("400x200")
        
        # Description Label
        self.description_label = ttk.Label(root, text="Select a video file to extract its audio:", font=("Arial", 12))
        self.description_label.pack(pady=10)

        # Select Video Button
        self.select_video_button = ttk.Button(root, text="Select Video", command=self.select_video)
        self.select_video_button.pack(pady=20)
        self.center_window()

    def center_window(self):
        """Centers the window on the screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
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
