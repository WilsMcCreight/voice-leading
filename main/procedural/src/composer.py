import random
from midiutil.MidiFile import MIDIFile

class Composer:
    def __init__(self):
        key = random.randint(0, 12)

    def compose(self, song):

        return song

class ProceduralComposer(Composer):
    def __init(self):
        self.time = 0
        self.track = 0

    def compose(self, song):
        for i in range(song.length*4):
            print(f"Adding Chord #{i+1}")
            song.add_chord(song.pick_next_chord(i))
        return song
