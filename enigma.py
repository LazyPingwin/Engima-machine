from Plugboard import *
from Rotor import *
from misc import *


class Enigma:
    max_number_of_rotors = 4

    def __init__(self, _plugboard, settings=None):
        # initializing empty list for storing rotors
        self.rotors = []
        self._settings = settings
        self._plugboard = _plugboard

    def __check_rotors(self):
        if len(self.rotors) < 3:
            print("Add more rotors. Should be 3 or 4")
            return

    def __traverse_rotors(self, character, direction='right_to_left'):
        prev_rot_pos = 0
        rotor_position = 0
        if direction == 'right_to_left':
            traverse_direction = range(len(self.rotors) - 1)
        else:
            traverse_direction = reversed(range(len(self.rotors)))
        for i in traverse_direction:
            rotor_position = self.rotors[i][1]
            input_character_position = (Rotor.letters_to_numbers_mapping[
                                            character] + rotor_position - prev_rot_pos) % 26
            input_character_position = (input_character_position - self.rotors[i][0]._ringsetting) % 26
            input_character = Rotor.alphabet[input_character_position]
            if direction == 'right_to_left':
                character = self.rotors[i][0].encode_right_to_left(input_character)
            else:
                character = self.rotors[i][0].encode_left_to_right(input_character)
            output_character_position = Rotor.letters_to_numbers_mapping[character]
            output_character_position = (output_character_position + self.rotors[i][0]._ringsetting) % 26
            character = Rotor.alphabet[output_character_position]
            prev_rot_pos = self.rotors[i][1]
        final_position = (Rotor.letters_to_numbers_mapping[character] - rotor_position) % 26
        character = Rotor.alphabet[final_position]
        return character
        # rotates rotors from right to left
        # the fourth rotor never rotates

    def __rotate(self):
        # rotate first
        first_notch = self.rotors[0][0].notch == Rotor.alphabet[self.rotors[0][1]]
        second_notch = self.rotors[1][0].notch == Rotor.alphabet[self.rotors[1][1]]
        self.rotors[0][1] = (self.rotors[0][1] + 1) % 26
        # rotate second
        if first_notch or second_notch:
            self.rotors[1][1] = (self.rotors[1][1] + 1) % 26
        # rotate third
        if second_notch:
            self.rotors[2][1] = (self.rotors[2][1] + 1) % 26

    def encode_character(self, character):
        if isnotupperstring(character, 1):
            raise ValueError('it should be one upper-case character')
        # Check if there is four(including reflector) or more rotors are plugged
        self.__check_rotors()
        character = self._plugboard.encode(character)
        # rotate rotors starting from the rightmost
        self.__rotate()
        # loops over rotors from right to left except for the reflector
        character = self.__traverse_rotors(character)
        # loops over rotors from left to right starting from reflector (it is the last element in the list)
        character = self.__traverse_rotors(character, "left_to_right")
        character = self._plugboard.encode(character)
        # print("Output character  %s" % character)
        return character

    def encode_string(self, input_string):
        return "".join([self.encode_character(char) for char in input_string])

    def add_rotor(self, rotor, initial_position='A'):
        if type(rotor) != Rotor:
            raise TypeError("the argument has to be of Rotor type")
        if len(self.rotors) > Enigma.max_number_of_rotors:
            print("Max numbers of rotors achieved")
            return
        # every rotor inside Enigma is a list of two elements
        # 0 - object rotor itself
        # 1 - rotor position inside the machine
        self.rotors.append([rotor, Rotor.letters_to_numbers_mapping[initial_position]])


if __name__ == "__main__":
    # test1
    plugboard = Plugboard()
    rotor1 = RotorBox.rotor_from_name("I")
    rotor2 = RotorBox.rotor_from_name("II")
    rotor3 = RotorBox.rotor_from_name("III")
    reflector = RotorBox.rotor_from_name("B")
    rotor1.set_ring_setting('01')
    rotor2.set_ring_setting('01')
    rotor3.set_ring_setting('01')
    enigma = Enigma(plugboard)
    enigma.add_rotor(rotor3, 'Z')
    enigma.add_rotor(rotor2, 'A')
    enigma.add_rotor(rotor1, 'A')
    enigma.add_rotor(reflector)
    print(enigma.encode_character('A'))

    # test2
    plugboard = Plugboard()
    rotor1 = RotorBox.rotor_from_name("I")
    rotor2 = RotorBox.rotor_from_name("II")
    rotor3 = RotorBox.rotor_from_name("III")
    reflector = RotorBox.rotor_from_name("B")
    rotor1.set_ring_setting('01')
    rotor2.set_ring_setting('01')
    rotor3.set_ring_setting('01')
    enigma = Enigma(plugboard)
    enigma.add_rotor(rotor3, 'A')
    enigma.add_rotor(rotor2, 'A')
    enigma.add_rotor(rotor1, 'A')
    enigma.add_rotor(reflector)
    print(enigma.encode_character('A'))

    # test3
    plugboard = Plugboard()
    rotor1 = RotorBox.rotor_from_name("I")
    rotor2 = RotorBox.rotor_from_name("II")
    rotor3 = RotorBox.rotor_from_name("III")
    reflector = RotorBox.rotor_from_name("B")
    rotor1.set_ring_setting('01')
    rotor2.set_ring_setting('01')
    rotor3.set_ring_setting('01')
    enigma = Enigma(plugboard)
    enigma.add_rotor(rotor3, 'V')
    enigma.add_rotor(rotor2, 'E')
    enigma.add_rotor(rotor1, 'Q')
    enigma.add_rotor(reflector)
    print(enigma.encode_character('A'))

    # test4
    plugboard = Plugboard()
    rotor1 = RotorBox.rotor_from_name("IV")
    rotor2 = RotorBox.rotor_from_name("V")
    rotor3 = RotorBox.rotor_from_name("Beta")
    reflector = RotorBox.rotor_from_name("B")
    rotor1.set_ring_setting('14')
    rotor2.set_ring_setting('09')
    rotor3.set_ring_setting('24')
    enigma = Enigma(plugboard)
    enigma.add_rotor(rotor3, 'A')
    enigma.add_rotor(rotor2, 'A')
    enigma.add_rotor(rotor1, 'A')
    enigma.add_rotor(reflector)
    print(enigma.encode_character('H'))

    # test5
    plugboard = Plugboard()
    rotor1 = RotorBox.rotor_from_name("I")
    rotor2 = RotorBox.rotor_from_name("II")
    rotor3 = RotorBox.rotor_from_name("III")
    rotor4 = RotorBox.rotor_from_name("IV")
    reflector = RotorBox.rotor_from_name("C")
    rotor1.set_ring_setting('07')
    rotor2.set_ring_setting('11')
    rotor3.set_ring_setting('15')
    rotor4.set_ring_setting('19')
    enigma = Enigma(plugboard)
    enigma.add_rotor(rotor4, 'Z')
    enigma.add_rotor(rotor3, 'V')
    enigma.add_rotor(rotor2, 'E')
    enigma.add_rotor(rotor1, 'Q')
    enigma.add_rotor(reflector)
    print(enigma.encode_character('Z'))

    plugboard = Plugboard()
    plugboard.add(PlugLead("PC"))
    plugboard.add(PlugLead("XZ"))
    plugboard.add(PlugLead("FM"))
    plugboard.add(PlugLead("QA"))
    plugboard.add(PlugLead("ST"))
    plugboard.add(PlugLead("NB"))
    plugboard.add(PlugLead("HY"))
    plugboard.add(PlugLead("OR"))
    plugboard.add(PlugLead("EV"))
    plugboard.add(PlugLead("IU"))

    rotor1 = RotorBox.rotor_from_name("IV")
    rotor2 = RotorBox.rotor_from_name("V")
    rotor3 = RotorBox.rotor_from_name("Beta")
    rotor4 = RotorBox.rotor_from_name("I")
    reflector = RotorBox.rotor_from_name("A")
    rotor1.set_ring_setting('18')
    rotor2.set_ring_setting('24')
    rotor3.set_ring_setting('03')
    rotor4.set_ring_setting('05')
    enigma = Enigma(plugboard)
    enigma.add_rotor(rotor4, 'P')
    enigma.add_rotor(rotor3, 'G')
    enigma.add_rotor(rotor2, 'Z')
    enigma.add_rotor(rotor1, 'E')
    enigma.add_rotor(reflector)
    print(enigma.encode_string('BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI'))

    plugboard1 = Plugboard()
    plugboard1.add(PlugLead("HL"))
    plugboard1.add(PlugLead("MO"))
    plugboard1.add(PlugLead("AJ"))
    plugboard1.add(PlugLead("CX"))
    plugboard1.add(PlugLead("BZ"))
    plugboard1.add(PlugLead("SR"))
    plugboard1.add(PlugLead("NI"))
    plugboard1.add(PlugLead("YW"))
    plugboard1.add(PlugLead("DG"))
    plugboard1.add(PlugLead("PK"))

    rotor1 = RotorBox.rotor_from_name("I")
    rotor2 = RotorBox.rotor_from_name("II")
    rotor3 = RotorBox.rotor_from_name("III")
    reflector = RotorBox.rotor_from_name("B")
    rotor1.set_ring_setting('01')
    rotor2.set_ring_setting('01')
    rotor3.set_ring_setting('01')
    enigma = Enigma(plugboard1)
    enigma.add_rotor(rotor3, 'Z')
    enigma.add_rotor(rotor2, 'A')
    enigma.add_rotor(rotor1, 'A')
    enigma.add_rotor(reflector)
    print(enigma.encode_string('HELLOWORLD'))
