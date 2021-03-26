import urllib.request
fhand=urllib.request.urlopen('http://data.pre4.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
