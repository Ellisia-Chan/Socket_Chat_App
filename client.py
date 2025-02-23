import tkinter as tk

# Color Palette
# Dark to Light
# AA60C8, D69ADE, EABDE6, FFDFEF

# Font
# Helvetica

class ClientGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ElyChat")
        self.geometry("600x600")
        self.configure(bg="#D69ADE")
        
        # Registration - First Window to be shown
        self.registration_window()

        # Mainloop
        self.mainloop()
        
    def registration_window(self):
        # Frame
        self.main_frame = tk.Frame(self, bg="#EABDE6", width=550, height=600)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        self.main_frame.pack_propagate(False)        
        
        # Title
        title = tk.Label(self.main_frame, text="ElyChat", font=("Helvetica", 20, "bold"), bg="#EABDE6")
        title.pack(pady=10, fill="x", anchor="n")
        
        username_frame = tk.Frame(self.main_frame, bg="#ffffff", width=600, height=300)
        username_frame.pack(padx=20, pady=20, fill="both", expand=True, anchor="s")
        username_frame.pack_propagate(False)
        
        # Fields
        username_label = tk.Label(username_frame, text="Username:", font=("Arial", 12), bg="#EABDE6")
        username_entry = tk.Entry(username_frame, font=("Arial", 12), bg="#FFDFEF")
        
        username_label.pack(side='top', fill='x', padx=50, pady=10)
        username_entry.pack(side='top', fill='x', padx=50, pady=10)
        
        # Submit Button
        submit_button = tk.Button(username_frame, text="Submit", font=("Arial", 12), bg="#AA60C8", fg="white")
        
        
if __name__ == "__main__":
    gui = ClientGUI()