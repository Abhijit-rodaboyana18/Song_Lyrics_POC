l={}
lyrics={}
with open('lyric_name.txt','r',encoding='utf-8') as f:
    for i in f:
        temp = i[:-1].split(",")
        l[temp[0]] = temp[1]
with open('album_lyrics.txt','r') as m:
    for i in m:
        temp = i[:-1].split(",")
        lyrics[temp[0]] = temp[1]

 

name=input("Enter your name:")
print(f'\nWelcome {name} ,\n')
for j in l.keys():
    print(j,'\n')
def lyrics_gen():
    global lyrics
    global l
    n=[]
    for i in lyrics:
        q=input("Do you want quit the lyrics (YES|NO):")
        if q=='no':
            pass
        if q=='yes':
            break
        select=int(input("Please choose the Song number to get the lyrics : "))
        for g in l.keys():
            n.append(g)
        print(f"\n{'-'*10}{n[select-1]}{'-'*10}\n")
        x=lyrics.get(f'{select}')
        print(x)
        for j in lyrics:
            c=input("\n Do you want to continue - press '*'  or  press 'q' to Quit : ")
            if c=='*':
                Another_song=int(input("\nPlease choose the Song number to get the lyrics :"))
                print(f"\n{'-'*10}{n[Another_song-1]}{'-'*10}\n")
                y=lyrics.get(f'{Another_song}')
                print(y)
            if c=='q' or c == 'Q':
                break
                print()
        break

 

lyrics_gen()

