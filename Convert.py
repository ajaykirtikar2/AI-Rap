from big_phoney import BigPhoney
import os
import re
import pronouncing
import random


class Convert():
    def syllables(input_file, output_file):
            for line in input_file.readlines():
                syllables = phoney.count_syllables(line)
                if syllables == 10 or syllables == 11 or syllables == 12 or syllables == 13 or syllables == 14:
                    output_file.write(line)

    # Generate rhyming couplet
    def generate_couplet(rhymes):
        while 1:
            i = random.randrange(len(rhymes.keys()))
            if len(rhymes[i]) >= 1:
                pool = rhymes[i] + [i]
                return random.sample(set(pool), 2)

    # Generate quatrain from two interspliced couplets
    def generate_quatrain(rhymes):
        a = Convert.generate_couplet(rhymes)
        b = Convert.generate_couplet(rhymes)
        return [a[0], b[0], a[1], b[1]]

    # Generate sonnet from 3 quatrains and a couplet
    def generate_sonnet(rhymes):
        a = Convert.generate_quatrain(rhymes)
        b = Convert.generate_quatrain(rhymes)
        c = Convert.generate_quatrain(rhymes)
        d = Convert.generate_couplet(rhymes)
        return a + b + c + d

    # Convert sonnet from index array to string
    def conv_sonnet(indices, line_dict):
        sonnet = ""
        for i in indices:
            sonnet += line_dict[i] + "\n"
        return sonnet

 
# Initialization
# input and output files
initial = input("Enter the name of the artist (use spaces): ")
name = initial.replace(" ", "_")

input_file = open("trained_output/{}_trained_output.txt".format(name))
output_file = open("syllable/{}_syllable.txt".format(name), "w")

phoney = BigPhoney()

# run method to convert into proper syllables
Convert.syllables(input_file, output_file)
output_file.close()

print("FINISHED SYLLABLES")

# input and outputs

# Get lines from syllable file
syllable_lines = open("syllable/{}_syllable.txt".format(name), "r")
lines = [line.strip() for line in syllable_lines.readlines()]

# Array of final word of each line
final_words = [re.sub(r'[^\w\s]', '', line.split(" ")[-1]) for line in lines]

# Enumerated dictionaries
line_dict = {i:w for i, w in enumerate(lines)}
word_dict = {i:w for i, w in enumerate(final_words)}


# Rhyming indices
# { 0 : [1, 2, 3] } means that line 0 rhymes with lines 1, 2, 3
rhyme_dict = {}

for i, word1 in word_dict.items():
    # Get potential rhymes from pronouncing package
    potential_rhymes = pronouncing.rhymes(word1)
    rhymes = []
    for x, word2 in word_dict.items():
        # Disallow rhyming with self or same word
        if word1 != word2:
            if word2 in potential_rhymes:
                rhymes.append(x)
    rhyme_dict[i] = rhymes

# Write generated sonnets to text file
output_file = open("final_output/{}_.txt".format(name), "w+")
NUM_SEQUENCES = 4
for i in range(NUM_SEQUENCES):
    sonnet = Convert.conv_sonnet(Convert.generate_sonnet(rhyme_dict), line_dict)
    output_file.write(sonnet)
    output_file.write("\n")
output_file.close()


print("FINISHED RHYMES")

