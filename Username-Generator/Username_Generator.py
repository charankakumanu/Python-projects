import requests
from random import randint
import tkinter as tk
App=tk.Tk()
App.title("UserName Generator")
App.geometry("800x500")
label=tk.Label(App,text="Welcome to UserName Generator!!",font=("Arial",30))
label.pack(pady=20)
def newName():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    response = requests.get(url)
    text = response.text
    words = text.split()
    num = randint(0,len(words)-1)
    return words[num]+str(randint(0,99999))
def onClick():
    label.config(text=newName())
button = tk.Button(App,text="Click to Generate Username",command=onClick)
button.pack()
App.mainloop()
