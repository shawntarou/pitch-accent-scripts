import win32clipboard
import pyperclip

win32clipboard.OpenClipboard()
raw_input = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
pitches = raw_input.split("<svg")[1:]
pitch_list = []

def remove_fluff(fluffy_pitch, fluff):
    return_pitch = fluffy_pitch
    for i in fluff:
        if i in return_pitch:
            return_pitch = return_pitch.removesuffix(i)

    return return_pitch

for pitch in pitches:
    new_pitch = "<li>" + "<svg" + remove_fluff(pitch, ["</ol>", "<li>"])
    pitch_list.append(new_pitch)

# Convert list into dictionary, then back to remove duplicates and keep order
pitch_dict = dict.fromkeys(pitch_list)
return_pitch = list(pitch_dict)

if len(return_pitch) == 1:
    return_pitch = "".join(return_pitch)
    return_pitch = return_pitch.removeprefix("<li>")
    return_pitch = return_pitch.removesuffix("</li>")
else:
    return_pitch = "".join(return_pitch)
    
pyperclip.copy(return_pitch)  # copies to clipboard
# print(return_pitch)