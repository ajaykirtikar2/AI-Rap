import requests
from bs4 import BeautifulSoup

class LyricScrape():

    def lookup(artist,file_output):
        # get artist data
        if len(artist.split()) < 2:
            url = 'https://www.lyrics.com/artist/' + artist.split(' ')[0].lower()
        else:
            url = 'https://www.lyrics.com/artist/' + artist.split(' ')[0].lower()
        for i in range(1, len(artist.split())):
            url = url + '%20' + artist.split(' ')[i].lower()

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')    

        alb = []
        songs = ""
    
        # grab albums
        albums = soup.find_all('h3', {'class': 'artist-album-label'})
        for i in albums:
            alb.append(i.text)
        # grab songs
        songlinks = soup.find_all('td', {'class': 'tal qx'})
        for i in songlinks:
            songs += " " + i.text
        
        base = 'https://www.lyrics.com/'
        lyrics = ""

        # do higher than 300...change based on artist
        iter = 150
        for i in range(iter):
            if songlinks[i].a is None:
                print('pass')
                pass
            else:
                r = requests.get(base + songlinks[i].a.attrs['href'])
                soup = BeautifulSoup(r.text, 'html.parser')
                lyrics += soup.find('pre', {'id': 'lyric-body-text'}).text
                file_output.write(lyrics)
                # console output
                print(i , '/' , iter)
                
    
        file_output.close() 

    # takes the file of unfiltered lyrics FROM unfiltered_data folder
    # removes duplicates and inserts INTO untrained_data folder
    def filter(name):
        lines_seen = set()  # holds lines already seen
        outfile = open('untrained_data/{}_untrained.txt'.format(name), "w")
        infile = open('unfiltered_data/{}_unfiltered.txt'.format(name), "r")

        for line in infile:
            # make sure not a duplicate
            if line not in lines_seen:  
                outfile.write(line)
                lines_seen.add(line)
        file_output.close()

# initialize input
artist = input("Enter the name of the artist (include spaces): ")
artist_ = artist.replace(" ", "_")
file_output = open('unfiltered_data/{}_unfiltered.txt'.format(artist_), "w")

# scrape lyrics from lyrics.com
LyricScrape.lookup(artist,file_output)
# filters lyrics and removes duplicate lines
LyricScrape.filter(artist_)
print("FINISHED")