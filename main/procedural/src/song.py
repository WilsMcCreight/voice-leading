from midiutil.MidiFile import MIDIFile


class Song:
    def __init__(self, parameters, name):
        self.song_parameters = parameters
        self.name = name

        self.data = {"composition_type": "procedural", "length": parameters[0], "tracks": 4, "time": 0, "tempo": parameters[1]}

        self.mf = MIDIFile(self.data["length"])
        self.mf.addTempo(self.data["track"], self.data["time"], self.data["tempo"])

    def add_note(self, )
        



