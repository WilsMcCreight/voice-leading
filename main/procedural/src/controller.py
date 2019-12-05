import random
from composer import ProceduralComposer
from song import Song
from colors import Colors

class Controller:
    def create(self, fast_startup = 0):
        print(f"{Colors.HEADER}Welcome to the generator, are you ready to make music?{Colors.ENDC}")
        self.data = self.get_inputs()
        name = input("Finally, what would you like to title your song? ")
        self.song = Song(self.data, name)

    def compose(self):
        if self.song.data["composition_type"] == "procedural":
            composer = ProceduralComposer()
        else:
            composer = Composer()
        self.song = composer.compose(self.song)
    
    def save(self):
        with open('./outputs/' + self.song.name + '.mid', 'wb') as output_file:
          self.song.mf.writeFile(output_file)
        print(f'{Colors.HEADER}Done! Theoretically your song {Colors.OKBLUE}{self.song.name}{Colors.HEADER} has been saved to the {Colors.OKBLUE}outputs{Colors.HEADER} folder.{Colors.ENDC}')

    def get_inputs(self):
        min_length = 1
        max_length = 50
        min_speed = 50
        max_speed = 150
        random_song = Controller.num_input(f"Would like a custom song ({Colors.OKBLUE}0{Colors.ENDC}) or a randomized song ({Colors.OKBLUE}1{Colors.ENDC})? ", 0, 1)
        if not random_song:
            length = Controller.num_input(f"How many 4/4 measures would you like your song to have?\n(At least {Colors.OKBLUE}{min_length}{Colors.ENDC}, up to {Colors.OKBLUE}50{Colors.ENDC}. Enter {Colors.OKBLUE}-1{Colors.ENDC} for a random choice): ", min_length, max_length)
        if random_song or length == -1:
            length = random.randint(min_length, max_length)
            print(f"{Colors.HEADER}Random selection. Your song will have {Colors.OKBLUE}{length}{Colors.HEADER} measures.{Colors.ENDC}")
        if not random_song:
            speed = Controller.num_input(f"What would you like the tempo of your song to be?\n(From {Colors.OKBLUE}{min_speed}{Colors.ENDC} to {Colors.OKBLUE}{max_speed}{Colors.ENDC}. Enter {Colors.OKBLUE}-1{Colors.ENDC} for a random choice): ", min_speed, max_speed)
        if random_song or speed == -1:
            speed = random.randint(min_speed, max_speed)
            print(f"{Colors.HEADER}Random selection. Your song will have a tempo of {Colors.OKBLUE}{speed}{Colors.HEADER}.{Colors.ENDC}")
        return [length, speed]
    
    @staticmethod
    def num_input(prompt, min, max = 500):
        while True:
            result = input(prompt)
            try:
                result = int(result)
            except ValueError:
                print(f"{Colors.WARNING}Sorry, {Colors.FAIL}the option you gave is either not a number or a float.{Colors.WARNING} Please reenter a valid number.{Colors.ENDC}")
                continue
            if result == -1:
                break
            if result < min:
                print(f"{Colors.WARNING}Sorry, {Colors.FAIL}the option you gave is below the minimum option.{Colors.WARNING} Please reenter a valid number.{Colors.ENDC}")
                continue
            if result > max:
                print(f"{Colors.WARNING}Sorry, {Colors.FAIL}the option you gave is above the minimum option.{Colors.WARNING} Please reenter a valid number.{Colors.ENDC}")
                continue
            break
        return result





