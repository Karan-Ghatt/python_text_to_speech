# Python Script for Text To Speech from a provided .txt file
# Final output in .mp3 format

import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()

# path to file
file_path = "aws_notes_2.txt"

# filename of output file
file_name = "current_aws_notes"

# Set reading rate of voice
engine.setProperty("rate", 150)

# Open file and read lines
print("Text To Speech Process Starting...")
with open(file_path, encoding="utf8") as f:
    # This creates a list of sentences from file, delineated at new line
    lines = f.readlines()

    # For each string sentence in generates list, removes new line character
    # also reads out each line

    lst = []

    for i in lines:
        i.strip()
        lst.append(i)

    string = " ".join(lst)

    engine.save_to_file(string, f'{file_name}.mp3')
    engine.runAndWait()  # don't forget to use this line
    print("Process Complete...")
    print(f"File Generated: {file_name}.mp3")


