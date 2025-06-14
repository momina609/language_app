
# AI-Powered Language Learning App (Enhanced Version)
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import random
import spacy
from datetime import datetime

nlp = spacy.load("en_core_web_sm")

DATA_FILE = "language_data.json"

# ----------------- Storage -----------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"progress": {}, "lessons": [], "quizzes": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ----------------- GUI App -----------------
class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌍 AI Language Learning Hub - Spanish Edition")
        self.root.geometry("700x500")
        self.root.config(bg="#f0f8ff")

        self.data = load_data()
        self.current_lesson = 0

        self.build_gui()

    def build_gui(self):
        tk.Label(self.root, text="📚 Learn Spanish with AI", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#1f4e79").pack(pady=10)

        tk.Button(self.root, text="📖 Start Lesson", command=self.start_lesson, width=25, height=2, bg="#cce5ff").pack(pady=10)
        tk.Button(self.root, text="📝 Take a Quiz", command=self.take_quiz, width=25, height=2, bg="#d1f0d1").pack(pady=10)
        tk.Button(self.root, text="🏆 View Achievements", command=self.show_achievements, width=25, height=2, bg="#fff3cd").pack(pady=10)
        tk.Button(self.root, text="👥 Community (Coming Soon)", state="disabled", width=25, height=2, bg="#e2e3e5").pack(pady=10)

    def start_lesson(self):
        lessons = [
            ("Greetings", "Hello = Hola\nGoodbye = Adiós\nPlease = Por favor\nThank you = Gracias\nExcuse me = Perdón"),
            ("Numbers", "One = Uno\nTwo = Dos\nThree = Tres\nFour = Cuatro\nFive = Cinco"),
            ("Days", "Monday = Lunes\nTuesday = Martes\nWednesday = Miércoles\nThursday = Jueves\nFriday = Viernes"),
            ("Colors", "Red = Rojo\nBlue = Azul\nGreen = Verde\nYellow = Amarillo\nBlack = Negro"),
            ("Common Phrases", "How are you? = ¿Cómo estás?\nI am fine = Estoy bien\nWhat's your name? = ¿Cómo te llamas?\nNice to meet you = Mucho gusto"),
        ]
        if self.current_lesson >= len(lessons):
            messagebox.showinfo("Done", "🎉 All lessons completed!")
            return
        title, content = lessons[self.current_lesson]
        messagebox.showinfo(f"Lesson: {title}", content)
        self.data['progress'][title] = True
        self.current_lesson += 1
        save_data(self.data)

    def take_quiz(self):
        quizzes = {
            "Hello": "Hola",
            "Two": "Dos",
            "Monday": "Lunes",
            "Green": "Verde",
            "Nice to meet you": "Mucho gusto"
        }
        score = 0
        for q, correct in random.sample(list(quizzes.items()), k=3):
            ans = simpledialog.askstring("Quiz", f"Translate '{q}' to Spanish:")
            if ans:
                similarity = nlp(ans.lower()).similarity(nlp(correct.lower()))
                if similarity > 0.75:
                    score += 1
        messagebox.showinfo("Quiz Result", f"🎯 You scored {score}/3")
        self.update_achievement(score)

    def update_achievement(self, score):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.data['progress'][f"quiz_{now}"] = score
        save_data(self.data)

    def show_achievements(self):
        completed = len([k for k in self.data['progress'] if k.startswith("quiz_")])
        level = "Beginner"
        if completed >= 3:
            level = "Intermediate"
        if completed >= 6:
            level = "Advanced"
        messagebox.showinfo("Achievements", f"🏅 Completed quizzes: {completed}\nYour Level: {level}")

# ----------------- Run App -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()



