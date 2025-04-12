import win32clipboard
import pyperclip
import os

win32clipboard.OpenClipboard()
raw_input = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
pitches = raw_input.split("<svg")
pitch_list = ""

def remove_fluff(fluffy_pitch, fluff):
    return_pitch = fluffy_pitch
    for i in fluff:
        if i in return_pitch:
            return_pitch = return_pitch.removesuffix(i)

    return return_pitch

def print_pitches(pitch_string):
    print(pitch_string)
    print("-----------------------------------------------\n")

def handle_pitch(user_input):
    global first_needs_element

    return_pitch = pitches[int(user_input)]
    return_pitch = remove_fluff(return_pitch, ["</ol>", "<li>", "</li>"])

    if is_a_list:
        return_pitch = "<li>" + "<svg" + return_pitch + "</li>"
    else:
        return_pitch = "<svg" + return_pitch
        first_needs_element = True

    return return_pitch

is_a_list = False
first_needs_element = False

while True:
    if pitch_list != "":
        is_a_list = True

    user_input = input("Which pitch # would you like? (q to quit): ")
    if user_input == "q":
        break

    return_pitch = ""

    if len(user_input) > 1:
        is_a_list = True
        user_input = user_input.split()
        for i in user_input:
            return_pitch += handle_pitch(i)
    else:
        return_pitch += handle_pitch(user_input)

    if is_a_list and first_needs_element:
        pitch_list = "<li>" + pitch_list
        first_needs_element = False

    pitch_list += return_pitch

    pyperclip.copy(pitch_list)  # copies to clipboard
    os.system("cls")  # clears console

    print_pitches(pitch_list)
