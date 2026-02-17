#def defines a function named reverse_string.
#text: str means the parameter text is expected to be a string (this is a type hint).
#-> str means the function will return a string (also a type hint).

def reverse_string(textToReverse: str) -> str:
    reversedText = ""
    for ch in textToReverse:
        reversedText = ch + reversedText
    return reversedText


#__name__ is a special built-in variable that Python sets for every module (every .py file).
#"__main__" is a special name Python uses for the program’s entry point (the file you run directly).
#"__main__" means: “this file is currently the main script being executed.”
if __name__ == "__main__":
    sample = "Palindrome Check can be performed here."
    print("Input:", sample)
    print("Output:", reverse_string(sample))