import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from PIL import Image, ImageTk, ImageDraw
import os
import re

class FilenameReviewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dataset_path = ''  # Will be set after directory selection
        self.files = []  # Will be populated after directory selection
        self.correctness_array = []
        self.current_file_index = 0
        self.title("Kikoyu Filename Reviewer")
        self.ask_dataset_path()  # Prompt for dataset path before starting

    def ask_dataset_path(self):
        self.withdraw()  # Hide the main window while the dialog is open
        messagebox.showinfo("Dataset Path", "Please select the dataset folder.")
        self.dataset_path = filedialog.askdirectory(title="Select Dataset Folder")
        if self.dataset_path:  # Proceed only if a path was selected
            self.files = [f for f in os.listdir(self.dataset_path) if f.endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
            self.deiconify()  # Show the main window again
            self.display_initial_info()
        else:
            messagebox.showerror("No Path Selected", "No dataset folder was selected. The application will exit.")
            self.destroy()  # Exit the application



    def init_ui(self):
        self.image_panel = tk.Label(self)
        self.image_panel.pack(pady=10)

        self.label = tk.Label(self, text="", width=50)
        self.label.pack(pady=10)

        # Navigation buttons
        self.prev_button = tk.Button(self, text="Previous", command=self.prev_file)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.yes_button = tk.Button(self, text="Correct", command=self.mark_correct)
        self.yes_button.pack(side=tk.LEFT, padx=20)

        self.no_button = tk.Button(self, text="Incorrect", command=self.mark_incorrect)
        self.no_button.pack(side=tk.RIGHT, padx=20)

        self.skip_button = tk.Button(self, text="Skip", command=self.next_file)
        self.skip_button.pack(side=tk.RIGHT, padx=10)

        self.quit_early = tk.Button(self, text="Quit", command=self.quit)
        self.quit_early.pack(side=tk.BOTTOM, pady=10)


    def display_initial_info(self):
        self.info_text = tk.Label(self, text="Welcome to the Filename Reviewer.\n\n"
                                             "You will be presented with each image in the dataset.\n"
                                             "Please indicate whether the filename is correct or incorrect.\n"
                                             "If incorrect, you will have the opportunity to provide a new name.\n\n"
                                             "Press 'Start Review' to begin.",
                                  justify=tk.LEFT, padx=10, pady=10)
        self.info_text.pack(pady=20)
        
        self.start_button = tk.Button(self, text="Start Review", command=self.prompt_for_starting_image)
        self.start_button.pack(pady=10)

    def prompt_for_starting_image(self):
        self.info_text.destroy()
        self.start_button.destroy()
        
        start_from = simpledialog.askinteger("Start From", 
                                             "Enter the starting image number if you want to start from the beginning, type in 1:",
                                             minvalue=1, maxvalue=len(self.files)) - 1
        self.current_file_index = max(0, start_from)
        
        self.init_ui()
        self.update_display()

    def init_ui(self):
        self.image_panel = tk.Label(self)
        self.image_panel.pack(pady=10)

        self.label = tk.Label(self, text="", width=50)
        self.label.pack(pady=10)

        navigation_frame = tk.Frame(self)
        navigation_frame.pack(pady=10)

        self.prev_button = tk.Button(navigation_frame, text="Previous", command=self.prev_file)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.yes_button = tk.Button(navigation_frame, text="Correct", command=self.mark_correct)
        self.yes_button.pack(side=tk.LEFT, padx=20)

        self.no_button = tk.Button(navigation_frame, text="Incorrect", command=self.mark_incorrect)
        self.no_button.pack(side=tk.RIGHT, padx=20)

        self.skip_button = tk.Button(navigation_frame, text="Skip", command=self.next_file)
        self.skip_button.pack(side=tk.RIGHT, padx=10)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM, pady=10)


    def quit(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?, write down the last image you were on if you wish to continue later with annotation."):
            self.destroy()  # or perform any saving operation before quitting

        
    # Include other necessary methods (update_display, display_image, mark_correct, mark_incorrect, next_file, etc.) here
    def update_display(self):
        if self.current_file_index < len(self.files):
            file_path = os.path.join(self.dataset_path, self.files[self.current_file_index])
            self.display_image(file_path)
            self.label.config(text=f"Reviewing {self.current_file_index + 1}/{len(self.files)}: Is the filename '{self.files[self.current_file_index]}' correct?")
        else:
            messagebox.showinfo("Complete", "Review complete.")
            print("Correctness Array:", self.correctness_array)
            self.destroy()

    def display_image(self, file_path):
        try:
            img = Image.open(file_path)
            img.thumbnail((400, 400))
            imgtk = ImageTk.PhotoImage(image=img)
            self.image_panel.configure(image=imgtk)
            self.image_panel.image = imgtk
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")
            self.next_file()

    def mark_correct(self):
        original_name = self.files[self.current_file_index]
        # Check if the filename ends with _0. If so, replace _0 with _1.
        if original_name.endswith("_0.jpg") or original_name.endswith("_0.jpeg") \
                or original_name.endswith("_0.png") or original_name.endswith("_0.gif") \
                or original_name.endswith("_0.bmp"):
            new_name = re.sub(r'_0(\.\w+)$', r'_1\1', original_name)
        elif not (original_name.endswith("_1.jpg") or original_name.endswith("_1.jpeg") \
                or original_name.endswith("_1.png") or original_name.endsWith("_1.gif") \
                or original_name.endswith("_1.bmp")):
            # For files not previously marked, add _1
            name, extension = os.path.splitext(original_name)
            new_name = f"{name}_1{extension}"
        else:
            # If already marked as _1, no need to rename
            new_name = original_name
        
        # Rename the file if new_name is different from original_name
        if new_name != original_name:
            try:
                os.rename(os.path.join(self.dataset_path, original_name), os.path.join(self.dataset_path, new_name))
                # Update the current filename in the files list to reflect the new name
                self.files[self.current_file_index] = new_name
            except Exception as e:
                messagebox.showerror("Error", f"Failed to rename file: {e}")
        
        # Add a green circle overlay to indicate correctness.
        file_path = os.path.join(self.dataset_path, self.files[self.current_file_index])
        try:
            img = Image.open(file_path)
            draw = ImageDraw.Draw(img)
            draw.ellipse((10, 10, 50, 50), fill="green")
            img.save(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add overlay to image: {e}")
        
        self.correctness_array.append(1)
        self.next_file()




    def mark_incorrect(self):
        original_name = self.files[self.current_file_index]
        match = re.match(r"(\d+)_", original_name)
        if match:
            prefix = match.group(1) + "_"
        else:
            prefix = ""
        
        name, extension = os.path.splitext(original_name)
        new_name_base = simpledialog.askstring("Rename", "Enter the new filename without a number:")
        if new_name_base:
            # Include numeric prefix, new base name, and append _0 before the extension
            new_name = f"{prefix}{new_name_base}_0{extension}"
            
            os.rename(os.path.join(self.dataset_path, original_name), os.path.join(self.dataset_path, new_name))
            
            # Add red circle overlay
            file_path = os.path.join(self.dataset_path, new_name)
            img = Image.open(file_path)
            draw = ImageDraw.Draw(img)
            draw.ellipse((10, 10, 50, 50), fill="red")
            img.save(file_path)
            
            self.correctness_array.append(1)
        self.next_file()

    def prev_file(self):
        if self.current_file_index > 0:
            self.current_file_index -= 1
            self.update_display()
        else:
            messagebox.showinfo("Info", "This is the first file.")

    def next_file(self):
        if self.current_file_index < len(self.files) - 1:
            self.current_file_index += 1
            self.update_display()
        else:
            messagebox.showinfo("Complete", "You have reached the end of the dataset, please select Quit or close the window.")


    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

def start_app():
    app = FilenameReviewer()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()

if __name__ == "__main__":
    start_app()
