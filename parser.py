#Aurora Brown, Cameron Henderson, Justin Smilan
import wikipedia
 
MusicGenres = wikipedia.page("Music genres").links
print(len(MusicGenres))
for link in MusicGenres:
    if 'genre' or 'style' not in wikipedia.summary(link, 1):
        MusicGenres.remove(link)
print(len(MusicGenres))
 
"""
for i in MusicGenres:
    print(i)
"""
         
def findLinks(genre):
    if genre not in MusicGenres:
        raise AssertionError()
    ConnectedGenres = []
    links = wikipedia.page(genre).links
    for link in links:
        if link in MusicGenres and link is not genre:
            ConnectedGenres.append(link)
    return {genre: ConnectedGenres}
 
def findAllLinks(): #This takes like 10 minutes to run
    genreDict = {}
    for i in MusicGenres:
        print(i)
        genreDict.update(findLinks(i))
    return genreDict
