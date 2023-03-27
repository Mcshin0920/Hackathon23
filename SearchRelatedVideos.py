# Description: Search for related videos on YouTube
def findYT(search):
    words = search.split()
    search_link = "http://www.youtube.com/results?search_query=" + '+'.join(words)
    return search_link
