from tkinter import*
import textwrap

root = Tk()
root.config(bg="light blue")
root.title("Language")
root.geometry("500x300")

label = Label(root, text="Enter Text", font=("Lucida Sans Unicode",20, "bold", "italic"), fg="#5D6D7E", bg="light blue")
label.place(relx=0.5, rely=0.1, anchor=W)

text=Text(root)
text.tag_config("here", background="black")

#language = list(LANGUAGES.value())
#src_lang.set('english')

root.mainloop()