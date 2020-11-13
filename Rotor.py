import string
from misc import *


class Rotor:
    # ring mapping to map input string to an int. For example '01' to 1. Starting from 1
    ring_setting_mapping = dict()
    alphabet = list(string.ascii_uppercase)
    for i in range(1, len(alphabet) + 1):
        ring_setting_mapping[f"{i:02d}"] = i - 1
    letters_to_numbers_mapping = dict()
    for i in range(0, len(alphabet)):
        letters_to_numbers_mapping[alphabet[i]] = i
    del i

    def __init__(self, name, value, notch=None, ringsetting='01'):
        self._name = name
        self.notch = notch
        self._value = value
        self._ringsetting = Rotor.ring_setting_mapping[ringsetting]
        self._core_ring_left_to_right = self._create_core_ring_left_to_right(value)
        self._core_ring_right_to_left = self._create_core_ring_right_to_left(value)
        self._outer_ring = list(string.ascii_uppercase)

    @staticmethod
    def _create_core_ring_right_to_left(value):
        new_dict = {}
        for i in range(0, len(string.ascii_uppercase)):
            new_dict[i] = value[i]
        return new_dict

    @staticmethod
    def _create_core_ring_left_to_right(value):
        new_dict = {}
        for i in range(0, len(value)):
            new_dict[value[i]] = i
        return new_dict

    def encode_right_to_left(self, character):
        new_position = (Rotor.letters_to_numbers_mapping[character]) % 26
        return self._core_ring_right_to_left[new_position]

    def encode_left_to_right(self, character):
        new_position = (Rotor.letters_to_numbers_mapping[character]) % 26
        new_index = self._core_ring_left_to_right[Rotor.alphabet[new_position]]
        return Rotor.alphabet[new_index]

    def encode_right_to_left_test(self, character):
        if isnotupperstring(character, 1):
            raise ValueError('it should be one uppercase character A-Z')
        else:
            return self.encode_right_to_left(character)

    def encode_left_to_right_test(self, character):
        if isnotupperstring(character, 1):
            raise ValueError('it should be one uppercase character A-Z')
        else:
            return self.encode_left_to_right(character)

    def set_ring_setting(self, ring_setting):
        if ring_setting in Rotor.ring_setting_mapping:
            self._ringsetting = Rotor.ring_setting_mapping[ring_setting]
        else:
            raise ValueError('Wrong value for ring setting')


# Helper static class
class RotorBox:
    rotorBeta = Rotor('Beta', 'LEYJVCNIXWPBQMDRTAKZGFUHOS')
    rotorGamma = Rotor('Gamma', 'FSOKANUERHMBTIYCWLQPZXVGJD')
    rotorI = Rotor('rotorI', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', notch='Q')
    rotorII = Rotor('rotorII', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', notch='E')
    rotorIII = Rotor('rotorIII', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', notch='V')
    rotorIV = Rotor('rotorIV', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', notch='J')
    rotorV = Rotor('rotorV', 'VZBRGITYUPSDNHLXAWMJQOFECK', notch='Z')
    reflectorA = Rotor('reflectorA', 'EJMZALYXVBWFCRQUONTSPIKHGD')
    reflectorB = Rotor('reflectorB', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')
    reflectorC = Rotor('reflectorC', 'FVPJIAOYEDRZXWGCTKUQSBNMHL')

    @staticmethod
    def rotor_from_name(name):
        rotors = {'Beta': RotorBox.rotorBeta,
                  'Gamma': RotorBox.rotorGamma,
                  'I': RotorBox.rotorI,
                  'II': RotorBox.rotorII,
                  'III': RotorBox.rotorIII,
                  'IV': RotorBox.rotorIV,
                  'V': RotorBox.rotorV,
                  'A': RotorBox.reflectorA,
                  'B': RotorBox.reflectorB,
                  'C': RotorBox.reflectorC,
                  }
        if name in rotors:
            return rotors[name]
        else:
            raise ValueError("Wrong rotor name!")
