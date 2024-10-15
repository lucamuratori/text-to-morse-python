from tkinter import *
from tkinter import messagebox


#dizionario morse
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def str_to_morse():
    message = message_entry.get().upper()
    morse_message = ""
    for _ in message:
        if _ == " ":
            morse_char = "/"
        elif _ not in MORSE_CODE_DICT:
            print(f"The character {_} is not included in the dictionary and will be skipped")
            continue
        else:
            morse_char = MORSE_CODE_DICT[_] + " "
        morse_message += morse_char
    translated_label.config(text=morse_message)
    return


#UI setup
window = Tk()
window.title("Text to Morse translator")
window.config(padx=50, pady=50, background="#eed895", width=300, height=300)


message_label = Label(text="Message:", background="#eed895")
message_label.grid(row=1, column=0)

morse_label = Label(text="Morse message:", background="#eed895")
morse_label.grid(row=2, column=0)

translate_button = Button(text="Translate", width=10, command=str_to_morse)
translate_button.grid(row=3, column=1)

message_entry = Entry(width=30)
message_entry.grid(row=1, column=1)
message_entry.focus()

translated_label = Label(text="", background="#eed895", width=30, font=("Arial", 20, "normal"))
translated_label.grid(row=2, column=1)




window.mainloop()