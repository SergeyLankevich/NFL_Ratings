import urllib.request
url = 'http://www.nfl.com/player/derekanderson/2506546/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)

part_name = text.find("player-name")
name = text[text.find('>', part_name)+1:text.find('&', part_name)]
print(name)

part_rate = text.find('player-totals')
statistics = text[text.find('<td>', part_rate) + 4:text.find('</tr>',part_rate)]
pure_stats = str(statistics).replace('/', ' ')
for the_char in pure_stats:
    if the_char.isdigit() is False and the_char != ' ' and the_char != '.':
        pure_stats = pure_stats.replace(the_char, '')
print(pure_stats) # Если профиль игрока полноценный, то должно выводить 16 параметров;
#  из этой длинной строки нам нужно вытащить 1-ый, 2-ой, 4-ый, 6-ой, 7-ой и 10-ый - это сам рейтинг.




