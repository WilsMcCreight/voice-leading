from midiutil.MidiFile import MIDIFile
import random


class Song:

    class Chord:

        def __init__(self, time):
            self.time = time
            # S Range: 60 - 79
            # A Range: 55 - 74
            # T Range: 48 - 67
            # B Range: 41 - 60
            self.possible_chords = [[s, a, t, b] for s in range(60, 79+1) for a in range(55, 74+1) for t in range(48, 67+1) for b in range(41, 60+1)]

        class Note:
            def __init__(self, channel, pitch, time):
                self.pitch = pitch
                self.channel = channel
                self.time = time

        def check_doubling(self):
            pass

        def check_spacing(self):
            pass

        def check_suspensions(self):
            pass

        def check_leaps(self):
            pass

        def check_leading_notes(self):
            pass

        def check_accidentals(self):
            pass

        def check_augmented_and_diminished_intervals(self):
            pass

        def check_parallels(self):
            pass

        def check_passing_sevenths(self):
            pass

        def select_from_remaining(self):
            chosen_chord = self.possible_chords[random.randint(0,len(self.possible_chords) - 1)]
            S = self.Note(0, chosen_chord[0], self.time)
            A = self.Note(1, chosen_chord[1], self.time)
            T = self.Note(2, chosen_chord[2], self.time)
            B = self.Note(3, chosen_chord[3], self.time)
            return {'S':S, 'A':A, 'T':T, 'B':B}

    def __init__(self, parameters, name):
        self.name = name

        self.composition_type = "procedural"
        self.length = parameters[0]
        self.tempo = parameters[1]
        self.record = []
        # "tracks": 4, "time": 0,

        self.mf = MIDIFile(self.length)
        self.mf.addTempo(0, 0, self.tempo)

    def add_chord(self, notes):
        self.mf.addNote(0, notes['S'].channel, notes['S'].pitch, notes['S'].time, 1, 100)
        self.mf.addNote(0, notes['A'].channel, notes['A'].pitch, notes['A'].time, 1, 100)
        self.mf.addNote(0, notes['T'].channel, notes['T'].pitch, notes['T'].time, 1, 100)
        self.mf.addNote(0, notes['B'].channel, notes['B'].pitch, notes['B'].time, 1, 100)

        self.record.append(notes)

    def pick_next_chord(self, time):
        next_chord = self.Chord(time)

        next_chord.check_doubling()
        next_chord.check_spacing()
        next_chord.check_suspensions()
        next_chord.check_leaps()
        next_chord.check_leading_notes()
        next_chord.check_accidentals()
        next_chord.check_augmented_and_diminished_intervals()
        next_chord.check_parallels()
        next_chord.check_passing_sevenths()

        return next_chord.select_from_remaining()

    def compose(self):
        # TODO: Replace the composer class with this
        pass
