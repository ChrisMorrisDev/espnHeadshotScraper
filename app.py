from bs4 import BeautifulSoup
import re
import urllib.request
import os
import time


print(os.path)

userInput = input('\n\n\nChoose a League:\n1. Tennis - ATP\n2. Tennis - WTA\n3. Golf\n\n#')
parser = 'lxml'

if userInput == '1':
    link = 'https://www.espn.com/tennis/rankings'
    dir_path = 'Tennis ATP'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

elif userInput == '2':
    link = 'https://www.espn.com/tennis/rankings/_/type/wta'
    dir_path = 'Tennis WTA'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

elif userInput == '3':
    link = 'https://www.espn.com/golf/rankings'
    dir_path = 'Golf'
    if not os.path.exists(dir_path):
            os.makedirs(dir_path)

def get_headshots(link):
    resp = urllib.request.urlopen(link)
    soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

    print('\n\n\nDownloading Headshots\n-------------------------------')
    for link in soup.find_all('a', href=re.compile("player/")):
        try:
            img_resp = urllib.request.urlopen(link['href'])
            soup2 = BeautifulSoup(img_resp, parser, from_encoding=resp.info().get_param('charset'))
            img_format = '.png'
            player_name = soup2.find('h1').string
            name = player_name.replace(" ", "-")
            filename = name + img_format
            cwd = os.getcwd()
            full_filename = os.path.join(dir_path, filename)
        except:
            continue

        try:
            
            for img in soup2.find(class_="main-headshot"):
                time.sleep(10)
                print('Player Name: ' + player_name + '\n' + 'Filename: ' + img['src'].rstrip('&w=350&h=254') + '\n')
                urllib.request.urlretrieve(img['src'].rstrip('&w=350&h=254'), full_filename)
        except:
            continue

get_headshots(link)