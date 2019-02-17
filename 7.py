def pl(num):
    if num==1 or num==4 or num==7:
        s=0
    elif num==2 or num==5 or num==8:
        s=2
    else:
        s=4
    return s
from random import randint
list1 = [["  ","|","  ","|","  "],["  ","|","  ","|","  "],["  ","|","  ","|","  "]]
list2 = ["------------"]
error=[]
print ("θεσεις:\n123\n456\n789")
print(' '.join(list1[0])+ "\n" + ' '.join(list2)+ "\n" +' '.join(list1[1])+ "\n" +' '.join(list2)+ "\n" +' '.join(list1[2]))
for i in range(9):
    if i%2 == 0:
        player=int(input("Δωσε θεση"))
        while player in error or player>9 or player<1:
            player = int(input("Δωσε εγκυρη θεση"))
        error.append(player)
        if player==3 or player==6 or player==9:
            list1[int(player/3)-1][pl(player)] = " X "
            print(' '.join(list1[0])+ "\n" + ' '.join(list2)+ "\n" +' '.join(list1[1])+ "\n" +' '.join(list2)+ "\n" +' '.join(list1[2]))
        else:
            list1[int(player/3)][pl(player)] = " X "
            print(' '.join(list1[0])+ "\n" + ' '.join(list2)+ "\n" +' '.join(list1[1])+ "\n" +' '.join(list2)+ "\n" +' '.join(list1[2]))
    else:
        ran=randint(1, 9)
        while ran in error:
            ran=randint(1, 9)
        error.append(ran)
        print ("Ο υπολογιστης επαιξε")
        if ran==3 or ran==6 or ran==9:
            list1[int(ran/3)-1][pl(ran)] = " O "
            print(' '.join(list1[0])+ "\n" + ' '.join(list2)+ "\n" +' '.join(list1[1])+ "\n" +' '.join(list2)+ "\n" +' '.join(list1[2]))
        else:
            list1[int(ran/3)][pl(ran)] = " O "
            print(' '.join(list1[0])+ "\n" + ' '.join(list2)+ "\n" +' '.join(list1[1])+ "\n" +' '.join(list2)+ "\n" +' '.join(list1[2]))
    if i >= 5:
        turn = " X "
        player = "Παιχτης"
        for y in range(2):
            if list1[0][0]==turn and list1[1][2]==turn and list1[2][4]==turn:
                print(player+" κερδισε το γυρο")
                end=input("Πατα enter για να κλεισεις το προγραμμα")    
                quit()
            elif list1[0][4]==turn and list1[1][2]==turn and list1[2][0]==turn:
                print(player+" κερδισε το γυρο")
                end=input("Πατα enter για να κλεισεις το προγραμμα")    
                quit()    
            elif list1[0][0]==turn and list1[1][0]==turn and list1[2][0]==turn:
                print(player+" κερδισε το γυρο")
                end=input("Πατα enter για να κλεισεις το προγραμμα")    
                quit()
            elif list1[0][2]==turn and list1[1][2]==turn and list1[2][2]==turn:
                print(player+" κερδισε το γυρο")
                end=input("Πατα enter για να κλεισεις το προγραμμα")    
                quit()
            elif list1[0][4]==turn and list1[1][4]==turn and list1[2][4]==turn:    
                print(player+" κερδισε το γυρο")
                end=input("Πατα enter για να κλεισεις το προγραμμα")    
                quit()	
            for j in range(3):
                win = 0            
                for z in range(0,5,2):
                    if list1[j][z]==turn: 
                        win += 1
                if win == 3:
                    print(player+" κερδισε το γυρο")
                    end=input("Πατα enter για να κλεισεις το προγραμμα")     
                    quit()
            turn =" O "
            player = "Υπολογιστης"    
end=input("Πατα enter για να κλεισεις το προγραμμα")
