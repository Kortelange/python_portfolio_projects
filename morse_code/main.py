TEXT_TO_MORSE_DICT = {
    " ": " ",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--"
}


def text_to_morse(text: str) -> str:
    """Translates a string to morse code"""
    return " ".join([TEXT_TO_MORSE_DICT[letter] for letter in text.lower()])


if __name__ == "__main__":
    text_to_translate = input("Please provide your input to translate to Morse code:\n")
    morse_code = text_to_morse(text_to_translate)
    print(f"{text_to_translate} translates to {morse_code}\n")
    save = input("Would you like to save the file(y/n)?")
    if save == "y":
        title = input("Please provide a filename (no input gives the default name 'morse_code.txt)")
        if title == "":
            title = "morse_code.txt"
        with open(title, "w") as f:
            f.write(f"Text: {text_to_translate}\nMorse Code: {morse_code}")
