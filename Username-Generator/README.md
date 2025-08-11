# 🖋 Username Generator (Tkinter + Requests)

A simple Python GUI application that generates random usernames using a large online English word list.  
Built with **Tkinter** for the GUI and **Requests** to fetch the word list.

---

## 📌 Features
- Generates a random username with a word + random number.
- Uses a **466k+ English word list** from GitHub.
- Responsive button click for instant username creation.
- Clean and simple Tkinter interface.

---

## 🛠 Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)

---

## 📂 How It Works
1. The program fetches a public **word list** from:
2. Stores the words in a Python list in memory (only downloads once for performance).
3. When the user clicks **"Generate Username"**:
- Picks a random word from the list.
- Appends a random number (0–9999).
- Displays the username in the app.
- <img width="1006" height="653" alt="image" src="https://github.com/user-attachments/assets/cb26c141-0c16-4d43-94d0-8bfd799c3a9d" />
