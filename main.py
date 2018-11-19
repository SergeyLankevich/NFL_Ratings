import urllib.request
a = open('input.txt', 'r')

with open('output.txt','w') as f_out:
    for line in a:
        f = urllib.request.urlopen(line)
        s = f.read()
        text = str(s)

        part_name = text.find('player-name')
        name = text[text.find('>', part_name) + 1: text.find('&', part_name)]

        part_rate = text.find('player-totals')
        total = text[text.find('TOTAL</td>'):text.find('</table>', text.find('TOTAL</td>'))]

        table_results = []
        for i in range(10):
            table_results.append((total[total.find('<td>') + 4:total.find('</td>')]).replace(',',''))
            total = total[total.find('</td>') + 4:]
            i += 1
            
        COMP = table_results[0]
        ATT = table_results[1]
        YDS = table_results[3]
        TD = table_results[5]
        _INT = table_results[6]
        ratings = table_results[9]

        print('{:<20}{:<5}{:<10}{:<10}{:<10}{:<10}{:<5}'.format(name, COMP, ATT, YDS, TD, _INT, ratings), file=f_out)



