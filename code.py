import os,time,random
os.system('color 7')
os.system('CLS')
delayval = 0.2
space = 500.0
spa = 0
ok = 0
i = 0
a = 0

delayval = float(input("bekleme süresini girin > 0."))
space = int(input("uzunlugu girin | <-> | > "))
spa = space
colors = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
os.system('CLS')

while a < 25:
    while i < (spa/2)+1:
        print("|" + "█"*ok + " "*space + "|"+ "📥")
        space = space - 1
        ok = ok + 1
        if ok >= spa:
            ok = spa
        i = i + 0.5
        time.sleep(delayval/10)
        os.system('CLS')
        os.system('color ' + random.choice(colors))
    a = a + 1
input()
