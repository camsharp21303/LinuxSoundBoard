import mido
import os
import csv

midi_in = mido.open_input("Akai MPD26 Port 1")

audio_file_extensions = (".mp3", ".wav", ".ogg", ".flac")
audio_files = []
note_maps = {}

with open("maps.csv", "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        if(len(row) == 2):
            key, value = row[0], row[1]
            note_maps[key] = value

def updateAudioFiles():
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(audio_file_extensions):
            audio_files.append(filename)
    for i in range(0, len(audio_files)):
        print("(" + str(i) + ") " + audio_files[i])

    print("(CTRL+C) save and exit")


updateAudioFiles()

try:
    for msg in midi_in:
        if msg.type == "note_on":
            print("Select sound file for note " + str(msg.note) + ": ")
            index = input()
            print("Selected \"" + audio_files[int(index)] + "\" for note " + str(msg.note))
            note_maps[str(msg.note)] = audio_files[int(index)]
except KeyboardInterrupt:
    pass

midi_in.close()

print(note_maps)

with open("maps.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)

    for key, value in note_maps.items():
        csvwriter.writerow([key, value])