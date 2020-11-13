from misc import *


class PlugLead:
    def __init__(self, mapping):
        self.checklead(mapping)
        self.mapping = mapping

    def encode(self, character):
        if isnotupperstring(character, 1):
            raise ValueError('it should be one upper-case character')
        if self.mapping[0] == character:
            return self.mapping[1]
        elif self.mapping[1] == character:
            return self.mapping[0]
        else:
            return character

    @staticmethod
    def checklead(mapping):
        if isnotupperstring(mapping, 2):
            raise ValueError('it should be two uppercase characters')


class Plugboard:

    maxplugs = 10

    def __init__(self):
        # I use a dictionary because it is based on HashTable and has O(1) complexity
        self.leads = dict()
        self.leadscounter = 0

    def add(self, pluglead):
        if type(pluglead) is not PlugLead:
            raise TypeError("The method accepts only PlugLead type")
        if self.leadscounter >= Plugboard.maxplugs:
            print("Maximum number(10) of leads reached")
            return
        if pluglead.mapping[0] in self.leads:
            print("This plug lead is already connected")
            return
        # Duplicating objects is a trade-off for fast access by a letter
        self.leads[pluglead.mapping[0]] = pluglead
        self.leads[pluglead.mapping[1]] = pluglead
        self.leadscounter += 1

    def encode(self, character):
        if isnotupperstring(character, 1):
            raise ValueError('it should be one uppercase character A-Z')
        if character in self.leads:
            if self.leads[character].mapping[0] != character:
                return self.leads[character].mapping[0]
            else:
                return self.leads[character].mapping[1]
        else:
            return character
