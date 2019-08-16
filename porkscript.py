import urllib.request, urllib.parse, urllib.error
from datetime import date
today = date.today()
fhand = urllib.request.urlopen('https://www.ams.usda.gov/mnreports/lm_pk640.txt')
newtextfile = 'pork_output/' + str(today) + '.txt'
fho = open(newtextfile, 'w')
for line in fhand:
    fho.write(line.decode())
    pass





fho.close()
fhand.close()
