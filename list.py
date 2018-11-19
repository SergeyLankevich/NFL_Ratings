import urllib.request


def dataSearch(text):
    reference = text.find('<td><a href=')
    name = text[text.find('"', reference) + 1:text.find('"', reference + 13)]
    link = 'http://www.nfl.com' + str(name)
    print(link, file=f_in)

    while reference != -1:
        reference = text.find('<td><a href=', reference + 1)
        name = text[text.find('"', reference) + 1:text.find('"', reference + 13)]
        link = 'http://www.nfl.com' + str(name)
        if link[-1] == 'e':
            print(link, file=f_in)


with open('input.txt', 'w') as f_in:
    url = 'http://www.nfl.com/players/search?category=position&filter=quarterback&conferenceAbbr=null&playerType=current&conference=ALL'
    f = urllib.request.urlopen(url)
    s = f.read()
    text = str(s)

    dataSearch(text)

    url = 'http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=quarterback&conferenceAbbr=null'
    f = urllib.request.urlopen(url)
    s = f.read()
    text = str(s)

    dataSearch(text)