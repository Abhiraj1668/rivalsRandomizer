import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk  # Make sure to: pip install pillow
import random
import os

# --- 1. THE DATABASE (49 Characters: Up to Season 7) ---

# 35% Weight: Aesthetically Pleasing
go_look_good = [
    "Invisible Woman", "Magik", "Luna Snow", "Black Cat", "White Fox", 
    "Mantis", "Psylocke", "Hela", "Scarlet Witch", "Storm", "Loki", "Phoenix"
]

# 35% Weight: Fun Mechanical Kits
go_have_fun = [
    "Winter Soldier", "Deadpool", "Gambit", "Squirrel Girl",
    "Adam Warlock", "Star-Lord","Moon Knight", "Namor"
]

# 15% Weight: Solid Fundamentals / Will Gladly Play
play_tier_1 = [
    "Mister Fantastic", "Peni Parker", "Iron Man", "The Punisher",
    "Elsa Bloodstone", "Rocket Raccoon", "Ultron"
]

# 10% Weight: Acceptable / Situational
play_tier_2 = [
    "Groot", "Cloak & Dagger", "Hawkeye",
    "Rogue", "Captain America", "Venom", "Daredevil",
    "Jeff the Land Shark", "Wolverine", "Emma Frost"
]

# 5% Weight: The Hard Counters / Override
play_tier_3 = [
    "Iron Fist", "The Thing", "Blade", "Spider-Man", "Thor", 
    "Hulk", "Magneto", "Doctor Strange", "Human Torch", 
    "Black Panther", "Angela"
]

categories = [go_look_good, go_have_fun, play_tier_1, play_tier_2, play_tier_3]
weights = [35, 35, 15, 10, 5]

class RivalsRandomizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Marvel Rivals: Shoshin Protocol")
        self.geometry("500x550")
        self.configure(bg="#1e1e2e")
        
        # Fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.hero_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.tier_font = font.Font(family="Helvetica", size=12, slant="italic")

        # UI Elements
        self.header = tk.Label(self, text="Awaiting Input...", font=self.title_font, bg="#1e1e2e", fg="#cdd6f4")
        self.header.pack(pady=20)

        self.image_label = tk.Label(self, bg="#1e1e2e")
        self.image_label.pack(pady=10)

        self.hero_name_label = tk.Label(self, text="Press the button to roll.", font=self.hero_font, bg="#1e1e2e", fg="#a6e3a1")
        self.hero_name_label.pack(pady=5)

        self.tier_label = tk.Label(self, text="", font=self.tier_font, bg="#1e1e2e", fg="#bac2de")
        self.tier_label.pack(pady=5)

        self.roll_button = tk.Button(self, text="Execute Roll", font=("Helvetica", 14, "bold"), 
                                     bg="#89b4fa", fg="#11111b", command=self.roll_character, 
                                     activebackground="#b4befe", padx=20, pady=10)
        self.roll_button.pack(pady=30)

    def roll_character(self):
        # 1. Pick the Tier based on weights
        selected_tier = random.choices(categories, weights=weights, k=1)[0]
        
        # 2. Pick a random hero from that Tier
        hero = random.choice(selected_tier)
        
        # 3. Determine Tier Name for display
        tier_name = ""
        if hero in go_look_good: tier_name = "Category: Aesthetically Pleasing (35%)"
        elif hero in go_have_fun: tier_name = "Category: Fun Mechanical Kit (35%)"
        elif hero in play_tier_1: tier_name = "Category: Solid Fundamentals (15%)"
        elif hero in play_tier_2: tier_name = "Category: Acceptable / Situational (10%)"
        elif hero in play_tier_3: tier_name = "Category: Hard Counter / Override (5%)"

        # 4. Update UI
        self.header.config(text="Your Hero Is:")
        self.hero_name_label.config(text=hero)
        self.tier_label.config(text=tier_name)
        
        # 5. Load Image (If it exists)
        self.load_image(hero)

    def load_image(self, hero_name):
        # Create an 'images' folder in the same directory as this script.
        # Name your images exactly like the hero names (e.g., "Invisible Woman.png")
        image_path = f"images/{hero_name}.png"
        
        try:
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img = img.resize((250, 250), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=photo)
                self.image_label.image = photo 
            else:
                self.image_label.config(image='', text="[ Image Not Found ]\nAdd " + hero_name + ".png to /images folder", fg="#f38ba8")
        except Exception as e:
            self.image_label.config(image='', text="Error loading image", fg="#f38ba8")

if __name__ == "__main__":
    # Ensure images directory exists
    if not os.path.exists("images"):
        os.makedirs("images")
        
    app = RivalsRandomizer()
    app.mainloop()