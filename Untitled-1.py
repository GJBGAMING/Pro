import pyttsx3
import random
import json
import tkinter as tk
from tkinter import messagebox, simpledialog

def load_scores():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_score(score, level):
    scores = load_scores()
    scores.append({"level": level, "score": score})
    with open("data.json", "w") as file:
        json.dump(scores, file)

def generate_random_word():
    word_list = [
        "banana", "elephant", "mountain", "adventure", "butterfly", "chocolate", "umbrella", "dinosaur", "sandwich", "fireworks",
        "ocean", "rainbow", "happiness", "kangaroo", "giraffe", "sunshine", "backpack", "astronaut", "volcano", "pineapple",
        "celebration", "friendship", "champion", "restaurant", "lightning", "carousel", "strawberry", "butterscotch", "chandelier", "mystery"
    ]
    return random.choice(word_list)

def start_spelling_test(level, root):
    engine = pyttsx3.init()
    word_levels = {
        "easy": ["cat", "dog", "fish", "tree", "house"],
        "medium": ["pencil", "giraffe", "sunshine", "banana", "blanket"],
        "hard": ["accommodate", "rhythm", "necessary", "embarrass", "occasionally"]
    }
    words = word_levels[level]
    random.shuffle(words)
    score = 0
    
    for word in words:
        engine.say(word)
        engine.runAndWait()
        answer = simpledialog.askstring("Spelling Test", "Spell the word:")
        if answer and answer.lower() == word.lower():
            score += 1
    
    save_score(score, level)
    messagebox.showinfo("Test Complete", f"You scored {score} out of {len(words)}!")
    main_menu(root)

def show_scores():
    scores = load_scores()
    score_text = "\n".join([f"Level: {s['level']}, Score: {s['score']}" for s in scores])
    messagebox.showinfo("Previous Scores", score_text if score_text else "No scores found.")

def difficulty_menu(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Select Difficulty", font=("Arial", 16, "bold"), fg="white", bg="#222").pack(pady=10)
    
    button_styles = {"bg": "#444", "fg": "white", "font": ("Arial", 12, "bold"), "relief": tk.RAISED, "bd": 5,
                     "padx": 12, "pady": 6, "borderwidth": 3, "highlightthickness": 2, "cursor": "hand2"}
    
    buttons = [
        ("Easy", lambda: start_spelling_test("easy", root)),
        ("Medium", lambda: start_spelling_test("medium", root)),
        ("Hard", lambda: start_spelling_test("hard", root)),
        ("Back", lambda: main_menu(root))
    ]
    
    for text, command in buttons:
        btn = tk.Button(root, text=text, command=command, **button_styles)
        btn.pack(pady=5, ipadx=10, ipady=4)

def main_menu(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Spelling Test Menu", font=("Arial", 16, "bold"), fg="white", bg="#222").pack(pady=10)
    
    button_styles = {"bg": "#444", "fg": "white", "font": ("Arial", 12, "bold"), "relief": tk.RAISED, "bd": 5,
                     "padx": 12, "pady": 6, "borderwidth": 3, "highlightthickness": 2, "cursor": "hand2"}
    
    buttons = [
        ("Start Spelling Test", lambda: difficulty_menu(root)),
        ("Generate Random Word", lambda: messagebox.showinfo("Random Word", generate_random_word())),
        ("View Scores", show_scores),
        ("Exit", root.quit)
    ]
    
    for text, command in buttons:
        btn = tk.Button(root, text=text, command=command, **button_styles)
        btn.pack(pady=5, ipadx=10, ipady=4)

def main():
    root = tk.Tk()
    root.title("Spelling Test App")
    root.geometry("400x300")
    root.configure(bg="#222")
    main_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
