#word count in Earl Sweatshirt's new album 'Some Rap Songs'


#Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Urls of all the songs
urlAll = ["https://genius.com/Earl-sweatshirt-shattered-dreams-lyrics",
"https://genius.com/Earl-sweatshirt-red-water-lyrics",
"https://genius.com/Earl-sweatshirt-cold-summers-lyrics",
"https://genius.com/Earl-sweatshirt-nowhere2go-lyrics",
"https://genius.com/Earl-sweatshirt-december-24-lyrics",
"https://genius.com/Earl-sweatshirt-ontheway-lyrics",
"https://genius.com/Earl-sweatshirt-the-mint-lyrics",
"https://genius.com/Earl-sweatshirt-peanut-lyrics",
"https://genius.com/Earl-sweatshirt-playing-possum-lyrics",
"https://genius.com/Earl-sweatshirt-veins-lyrics",
"https://genius.com/Earl-sweatshirt-eclipse-lyrics",
"https://genius.com/Earl-sweatshirt-azucar-lyrics",
"https://genius.com/Earl-sweatshirt-loosie-lyrics",
"https://genius.com/Earl-sweatshirt-the-bends-lyrics",
"https://genius.com/Earl-sweatshirt-riot-lyrics"
]

#get lyrics from the page
def GetLyrics(urlList):
    for url in urlList:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        lyrics = soup.find("div", class_="lyrics").get_text().split()
        yield lyrics

#fix words, remove ", ? !" etc.
def FixWord(word):
    other = ["[Instrumental]","[Verse]","[Refrain]","[Segue]","[Intro]","[Outro]"]
    if word in other:
        return
    word = word.lstrip('"()[],')
    word = word.rstrip('"!?()[],')
    word = word.lower()
    return word

#put words and their use in dictionary
def CountWords(Lyrics):
    Dict = {}
    for song in Lyrics:
        for word in song:
            fixed = FixWord(word)
            if fixed not in Dict:
                Dict[fixed] = 1
            elif fixed in Dict:
                Dict[fixed] = int(Dict[fixed]) + 1
    return Dict

#take dictionary into 2 lists
def Analyze(dict):
    words = []
    usetimes = []
    for key, value in sorted(dict.items(), reverse = True, key=lambda kv: kv[1]):
        words.append(key)
        usetimes.append(value)
    return words, usetimes

#use pandas to show data
def PlotData(word, use):
    usage = pd.DataFrame({
            "word": word,
            "use": use
    })
    print(usage)

#main
def Main():
    AllLyrics = GetLyrics(urlAll)
    Data = CountWords(AllLyrics)
    word, use = Analyze(Data)
    PlotData(word, use)


#running main
Main()
