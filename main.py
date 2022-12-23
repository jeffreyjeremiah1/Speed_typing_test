from tkinter import *


word_list = ["game", "car", "house", "information", "regard", "condition", "mathematics", "salt", "foreign", "position",
             "books", "finance", "press", "strategy", "command", "focus", "motivate", "plane", "salary", "error",
             "balance", "issue", "therapy", "identify", "compliment", "colon", "verify", "pandemonium", "flabbergasted",
             "young", "evil", "management", "urgent", "necessary", "pillow", "volume", "definition", "guarantee"]


class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Speed typing test")
        self.geometry("700x700")
        self.config(bg="#C0C0C0")
        self.image = PhotoImage(file="images/background.png")
        self.background_label = Label(image=self.image)
        self.background_label.pack()
        self.time_count = 60
        self.canvas = Canvas(bg="#C0C0C0", width=600, height=500)
        self.canvas.place(x=50, y=50)
        self.create_buttons()
        self.create_entry()
        self.timer()
        self.text_box()

    def text_box(self):
        self.text_screen = Canvas(self.canvas, bg="white", width=500, height=200)
        self.text_screen.place(x=50, y=100)

        self.texts = Message(self.text_screen, text=word_list, width=500,
                             font=("Arial Bold", 20), fg="red", padx=5)
        self.texts.place(x=5, y=10)

    def create_buttons(self):
        self.start = Button(highlightbackground="#C0C0C0", text="start", padx="15", bg="red", fg="blue",
                            command=self.countdown)
        self.start.place(x=450, y=500)
        self.stop = Button(highlightbackground="#C0C0C0", text="reset", padx="15", bg="red", fg="blue",
                           command=self.reset)
        self.stop.place(x=530, y=500)

    def create_entry(self):
        self.entry_box = Entry(self.canvas, highlightbackground="#C0C0C0", textvariable=1)
        self.entry_box.focus()
        self.entry_box.place(x=47, y=350, width=510, height=40)

    def timer(self):
        self.timer_box = Canvas(self.canvas, bg="#ADD8E6", width=600, height=30)
        self.timer_box.place(x=0, y=0)
        self.wpm_label = self.timer_box.create_text((200, 20), text="WPM: ")
        self.wpm_value = Label(self.timer_box, text="0")
        self.wpm_value.place(x=220, y=8)
        self.time_label = self.timer_box.create_text((315, 20), text="Time Left: ")
        self.time_value = Label(self.timer_box, text="60")
        self.time_value.place(x=350, y=8)

    def countdown(self):
        if self.time_count != 0:
            self.after(1000, self.countdown)
            self.time_count -= 1
            self.time_value.configure(text=self.time_count)
        elif self.time_count == 0:
            self.check_words()

    def check_words(self):
        correct_words = []
        self.value = self.entry_box.get().split(" ")
        print(len(self.value))
        for word in word_list:
            if word in self.value:
                correct_words.append(word)
                self.wpm = len(correct_words)
                self.wpm_value.configure(text=self.wpm)

    def reset(self):
        self.time_count = 60
        self.time_value.configure(text=self.time_count)
        self.wpm = 0
        self.wpm_value.configure(text=self.wpm)
        self.entry_box.delete(0, "end")


app = App()
app.mainloop()
