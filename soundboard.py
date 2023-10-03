import mido
import csv
from playsound import playsound

midi_in = mido.open_input("Akai MPD26 Port 1")

note_maps = {}

with open("maps.csv", "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        if(len(row) == 2):
            key, value = row[0], row[1]
            note_maps[key] = value

for msg in midi_in:
    if msg.type == "note_on":
        if str(msg.note) in note_maps:
            playsound(note_maps[str(msg.note)])