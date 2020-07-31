# AI-Rap
Lyric Classifier using Tensor Flow RNN

@Author: Ajay Kirtikar

Based off of TensorFlow RNN tutorial: https://www.tensorflow.org/tutorials/text/text_generation 

As well as John Fish's python implementation shakespeare_ai: https://github.com/johnafish/shakespeare_ai

-----------------------------------------------------------------------------

Fun Project that takes lyrics from any artist and sends to a RNN, 
which then predicts an output based on character classifications
idea: have AI create its own music lyrics based on real artists

-----------------------------------------------------------------------------

Description:  

Using RNN and tensorflow APIs:

    - grab lyrics from lyrics.com
    - filter the lyrics and remove duplicates
    - upload the lyrics to rap.py in Google Colab
    - download new trained lyrics
    - convert trained lyrics into 10,11,12,13 syllable lines
    - match lines to rhyme with stanza flow

-----------------------------------------------------------------------------

Download project on local machine

You may upload rap.py into Google Colab for better performance

Need latest version of Python

-----------------------------------------------------------------------------

How to run:

Command Line: python LyricScrape.py , follow instructions on command prompt

grab untrained file in untrained_data/ local folder

drag into Google Colab with rap.py

make sure runtime is type GPU!

run rap.py in Google Colab

take resulting 'name'_trained_output from Google Colab

drag into trained_output/ local folder

Command Line: python Convert.py , follow instructions on command prompt

final lyric output will be in final_output/ local folder
