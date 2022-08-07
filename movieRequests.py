from ast import Try
from urllib import request
import requests as rq

print("Type in the movie name or link: ")
movie = input()

movieIsLink = False
firstCharsLink = movie[0:3]

if firstCharsLink == "htt" or firstCharsLink == "www":
    movieIsLink = True
    try:
        movieRQ = rq.get(movie)
    except:
        print("Either that is not a link or the link is not working as intended.")
else:
    movieIsLink = False
movieIsLink = movie.startswith(('http', 'www'))
print(movieIsLink, firstCharsLink, movie)

# try:
#     movieRQ = rq.get(movie)
# except:
#     print("Either that is not a link or the link is not working as intended.")
# print("nice.")
