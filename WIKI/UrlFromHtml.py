import re
from urllib.parse import unquote

def geturlfromhtml(soup):
    url=soup.select("link[rel='canonical']")[0].attrs["href"]
    url=unquote(url)
    return url