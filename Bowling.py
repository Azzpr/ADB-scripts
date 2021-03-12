import os, time
turn = input("Who's turn is it?: ")
if(turn == "me"):
    for i in range(1, 6):
        #Display what round this is
        print('Current round: ', i)
        #if we are on the 5nth bowl
        if(i == 5):
            for i in range(1, 5):
                #show what round im in
                print('Current round: ', i + 5)
                #Posotion the ball
                os.system('adb shell input touchscreen swipe 720 2710 690 2710 400')
                #throw the ball
                time.sleep(1)
                os.system('adb shell input touchscreen swipe 690 2710 690 2810 400')
                os.system('adb shell input touchscreen swipe 690 2850 690 2610 300')
                time.sleep(2)
    
        #Posotion the ball
        os.system('adb shell input touchscreen swipe 720 2710 690 2710 400')
        #throw the ball
        os.system('adb shell input touchscreen swipe 690 2710 690 2810 400')
        os.system('adb shell input touchscreen swipe 690 2850 690 2610 300')
        #take a break, contiune after the opponent has boolwed
        time.sleep(20)

if(turn == "last"):
    for i in range(1, 4):
        #show what round im in
        print('Current round: ', i + 5)
        #Posotion the ball
        os.system('adb shell input touchscreen swipe 720 2710 690 2710 400')
        #throw the ball
        time.sleep(1)
        os.system('adb shell input touchscreen swipe 690 2710 690 2810 400')
        os.system('adb shell input touchscreen swipe 690 2850 690 2610 300')
        time.sleep(7)



