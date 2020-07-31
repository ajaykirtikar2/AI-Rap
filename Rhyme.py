""" Rhyme
Generate rhyming shakespearean sonnets from a file of 10-syllable phrases.
"""
import re
import pronouncing
import random


class Rhyme():
    # Generate rhyming couplet
    def generate_couplet(rhymes):
        while 1:
            i = random.randrange(len(rhymes.keys()))
            if len(rhymes[i]) >= 1:
                pool = rhymes[i] + [i]
                return random.sample(set(pool), 2)

    # Generate quatrain from two interspliced couplets
    def generate_quatrain(rhymes):
        a = Rhyme.generate_couplet(rhymes)
        b = Rhyme.generate_couplet(rhymes)
        return [a[0], b[0], a[1], b[1]]

    # Generate sonnet from 3 quatrains and a couplet
    def generate_sonnet(rhymes):
        a = Rhyme.generate_quatrain(rhymes)
        b = Rhyme.generate_quatrain(rhymes)
        c = Rhyme.generate_quatrain(rhymes)
        d = Rhyme.generate_couplet(rhymes)
        return a + b + c + d

    # Convert sonnet from index array to string
    def conv_sonnet(indices, line_dict):
        sonnet = ""
        for i in indices:
            sonnet += line_dict[i] + "\n"
        return sonnet