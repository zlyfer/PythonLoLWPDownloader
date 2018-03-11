# If modules not found use following in console:
# pip install requests
# pip install os

import requests
import os

def user_exit():
    input("Press any key to exit.")
    exit()

def download(filename):
    if os.path.exists('Wallpaper/%s.jpg' % filename):
        return (['Skip'])
    file = open('Wallpaper/' + filename + '.jpg', 'wb')
    link = 'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'
    image = requests.get(link + filename + '.jpg').content
    file.write(image)
    file.close()
    if os.path.exists('Wallpaper/%s.jpg' % filename):
        filesize = os.path.getsize('Wallpaper/%s.jpg' % filename)
        if filesize < 500:
            os.remove('Wallpaper/%s.jpg' % filename)
            return (['End'])
        return (['Success', filesize // 1000])
    else:
        return (['Error'])

if not os.path.exists('champions.ini'):
    print ("'champions.ini' couldn't be loaded.")
    user_exit()
else:
    print ("Loading 'champions.ini'.")
    file = open('champions.ini', 'r')
    content = file.readlines()
    file.close()
    global champions
    champions = []
    champions_string = ""
    for entry in content:
        entry = entry.replace('\n', '')
        champions.append(entry)
        champions_string += entry + " "
    print ("'champions.ini' loaded.")
    print ("\nChampions: %s\n" % champions_string)

if not os.path.exists('Wallpaper'):
    print ("Creating folder 'Wallpaper'.")
    os.mkdir('Wallpaper')
    if not os.path.exists('Wallpaper'):
        print ("Failed creating folder 'Wallpaper'.")
        user_exit()
    else:
        print ("Folder 'Wallpaper' created.")

newchamp = False
file = open('champions.ini', 'a')
while newchamp != '':
    newchamp = input('Type champion name to add new champions, or just press Enter to start downloading: ')
    if newchamp != '':
        file.write('%s\n' % newchamp)
        champions.append(newchamp)
file.close()

for champ in champions:
    print ("\n%s:" % champ)
    for skin in range(100):
        msg = download(champ + "_%s" % skin)
        if msg[0] == "End":
            break
        elif msg[0] == "Success":
            print ("- Added: Skin %s, filesize: %s KB." % (skin, msg[1]))
        elif msg[0] == "Skip":
            print ("- Skipped: Skin %s, already exists." % skin)

print ("\nDone.")
user_exit()