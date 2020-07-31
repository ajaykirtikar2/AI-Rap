#given an input file, will write to an output file 10-13 syllable lines

from big_phoney import BigPhoney
import os
#import LyricScrape

class Syllable(object):
    # writes lines of 10,11,12,13, or 14 syllables to an output file
    # input: file of unsorted lyrics
    # output: file of sorted lyrics based on syllable count
    def syllables(self,input_file, output_file):
        for line in input_file.readlines():
            syllables = phoney.count_syllables(line)
            if syllables == 8 or syllables == 9 or syllables == 10 or syllables == 11 or syllables == 12 or syllables == 13 or syllables == 14:
                output_file.write(line)
