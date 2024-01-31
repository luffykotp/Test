import tkinter as tk

root = tk.Tk()

stats = tk.Label(root, text="stats")
firstButton = tk.Button(root, text= "Click me")

frameOne = tk.LabelFrame(root, text = "Log in", padx =  100, pady = 100)
login = tk.Label(frameOne, text = "Your name will go here.")


frameOne.pack()
login.pack()
stats.pack()
firstButton.pack()





root.mainloop()