import pyautogui as pt
from time import sleep
import win32gui, win32con

sleep(0.1)

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

pt.FAILSAFE = True 

sleep(0.5)

#general loop
while 1:  
    
    # loop 1
    while 1:
        
        # check for 10K
        img_adv_port= pt.locateOnScreen("imgs/dice/adv_port.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
        img_2K= pt.locateOnScreen("imgs/dice/2K.png", grayscale=False, region=(761,371,400,400), confidence=0.94)

        if img_adv_port is not None:
            print("you found adv port")
            
            if img_2K is not None:
                print("you found 10K")
                
                # move to shuffle and click         
                pt.moveTo(1284,745)
                sleep(0.5)
                pt.click(1284,745)
                
                # new screen
                sleep(4)
                
            # click on 1 sqaure
                pt.moveTo(826,702)
                sleep(0.5)
                pt.click(826,702)
                
                #new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698)
                print("i turn 1 sqaure") 
                
                # new screen
                sleep(3)  
                
            # click on 2 sqaure
                pt.moveTo(826,575)
                sleep(0.5)
                pt.click(826,575)
                
                # new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698)
                print("i turn 2 sqaure") 
                
                # new screen
                sleep(3)  
                
            # click on 3 sqaure
                pt.moveTo(826,441)
                sleep(0.5)
                pt.click(826,441) 
                
                #new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698)
                print("i turn 3 sqaure") 
                
                # new screen
                sleep(3)  
                
            # click on 4 sqaure
                pt.moveTo(957,719)
                sleep(0.5)
                pt.click(957,719) 
                
                #new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698)
                print("i turn 4 sqaure") 
                
                # new screen
                sleep(3) 
                
            # click on 5 sqaure
                pt.moveTo(957,596)
                sleep(0.5)
                pt.click(957,596)
                
                #new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698) 
                print("i turn 5 sqaure") 
                
                # new screen
                sleep(3)  
                    
            # click on 6 sqaure
                pt.moveTo(958,441)
                sleep(0.5)
                pt.click(958,441)
                
                # new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698) 
                print("i turn 6 sqaure") 
                
                #new screen
                sleep(3)
                 
            # click on 7 sqaure
                pt.moveTo(1084,707)
                sleep(0.5)
                pt.click(1084,707)
                
                # new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698) 
                print("i turn 7 sqaure") 
                
                #new screen
                sleep(3)
                
            # click on 8 sqaure
                pt.moveTo(1084,567)
                sleep(0.5)
                pt.click(1084,567)
                
                # new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698) 
                print("i turn 8 sqaure") 
                
                #new screen
                sleep(3)
                            
            # click on 9 sqaure
                pt.moveTo(1084,438)
                sleep(0.5)
                pt.click(1084,438)
                
                # new screen
                sleep(2)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698) 
                print("you found 20x 8H")
                
            # post in chat
                pt.moveTo(630,745)
                sleep(0.5)
                pt.click(630,745)
                
                # new screen
                sleep(3)
                
                #share in city chat
                pt.moveTo(1077,698)
                sleep(0.5)
                pt.click(1077,698)
                
                # new screen
                sleep(2)
                
            #click on next shuffle
                pt.moveTo(1282,694)
                sleep(0.5)
                pt.click(1282,694)
                sleep(0.5)
                break
                
        else:
            print("No 10K")
        
        img_2X= pt.locateOnScreen("imgs/dice/2X.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
        if img_2X is not None:
            print("i see 2X")
            
            img_5X= pt.locateOnScreen("imgs/dice/5X.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
            if img_5X is not None:
                print("i see 5X")

                img_15X= pt.locateOnScreen("imgs/dice/15X.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
                if img_5X is not None:
                    print("i see 15X")
                    
                    img_2K= pt.locateOnScreen("imgs/dice/2K.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
                    if img_2K is not None:
                        print("i see 2K")
                        
                    # move to shuffle and click         
                        pt.moveTo(1284,745)
                        sleep(0.5)
                        pt.click(1284,745)
                        
                        # new screen
                        sleep(4)
                        
                    # click on 1 sqaure
                        pt.moveTo(826,702)
                        sleep(0.5)
                        pt.click(826,702)
                        
                        #new screen
                        sleep(2)
                        
                        # click on yes
                        pt.moveTo(956,698) 
                        sleep(0.5)
                        pt.click(956,698)
                        print("i turn 1 sqaure") 
                        
                        # new screen
                        sleep(3)  
                        
                    # click on 2 sqaure
                        pt.moveTo(826,575)
                        sleep(0.5)
                        pt.click(826,575)
                        
                        # new screen
                        sleep(1)
                        
                        # click on yes
                        pt.moveTo(956,698) 
                        sleep(0.5)
                        pt.click(956,698)
                        print("i turn 2 sqaure") 

                        if img_15X is True:
                            print("No 30K")
                            # click next shuffle
                            sleep(1)
                            pt.moveTo(1282,694)
                            sleep(0.5)
                            pt.click(1282,694)
                            
                            # new screen
                            sleep(2)
                            
                            # move to yes
                            pt.moveTo(957,698)
                            sleep(0.5)
                            pt.click(957,698)   
                            break
                        
                        if img_15X is False:
                            print("BINGO")
                            
                        # click on 3 sqaure
                            pt.moveTo(826,441)
                            sleep(0.5)
                            pt.click(826,441) 
                            
                            #new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698)
                            print("i turn 3 sqaure") 
                            
                            # new screen
                            sleep(3)  
                            
                        # click on 4 sqaure
                            pt.moveTo(957,719)
                            sleep(0.5)
                            pt.click(957,719) 
                            
                            #new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698)
                            print("i turn 4 sqaure") 
                            
                            # new screen
                            sleep(3) 
                            
                        # click on 5 sqaure
                            pt.moveTo(957,596)
                            sleep(0.5)
                            pt.click(957,596)
                            
                            #new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("i turn 5 sqaure") 
                            
                            # new screen
                            sleep(3)  
                                
                        # click on 6 sqaure
                            pt.moveTo(958,441)
                            sleep(0.5)
                            pt.click(958,441)
                            
                            # new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("i turn 6 sqaure") 
                            
                            #new screen
                            sleep(3)
                             
                        # click on 7 sqaure
                            pt.moveTo(1084,707)
                            sleep(0.5)
                            pt.click(1084,707)
                            
                            # new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("i turn 7 sqaure") 
                            
                            #new screen
                            sleep(3)
                            
                        # click on 8 sqaure
                            pt.moveTo(1084,567)
                            sleep(0.5)
                            pt.click(1084,567)
                            
                            # new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("i turn 8 sqaure") 
                            
                            #new screen
                            sleep(3)
                                        
                        # click on 9 sqaure
                            pt.moveTo(1084,438)
                            sleep(0.5)
                            pt.click(1084,438)
                            
                            # new screen
                            sleep(2)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("you found 30K")
                            
                        # post in chat
                            pt.moveTo(630,745)
                            sleep(0.5)
                            pt.click(630,745)
                            
                            # new screen
                            sleep(3)
                            
                            #share in city chat
                            pt.moveTo(1077,698)
                            sleep(0.5)
                            pt.click(1077,698)
                            
                            # new screen
                            sleep(2)
                            
                        #click on next shuffle
                            pt.moveTo(1282,694)
                            sleep(0.5)
                            pt.click(1282,694)
                            sleep(0.5)
                            break
        else:
            print("No 30K")
                
        # new screen
        sleep(1)
        
        img_3X= pt.locateOnScreen("imgs/dice/3X.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
        if img_3X is not None:
            print("i see 3X")
            
            img_5X= pt.locateOnScreen("imgs/dice/5X.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
            if img_5X is not None:
                print("i see 5X")

                img_15X= pt.locateOnScreen("imgs/dice/15X.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
                if img_5X is not None:
                    print("i see 15X")
                    
                    img_2K= pt.locateOnScreen("imgs/dice/2K.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
                    if img_2K is not None:
                        print("i see 2K")
                        
                    # move to shuffle and click         
                        pt.moveTo(1284,745)
                        sleep(0.5)
                        pt.click(1284,745)
                        
                        # new screen
                        sleep(4)
                        
                    # click on 1 sqaure
                        pt.moveTo(826,702)
                        sleep(0.5)
                        pt.click(826,702)
                        
                        #new screen
                        sleep(2)
                        
                        # click on yes
                        pt.moveTo(956,698) 
                        sleep(0.5)
                        pt.click(956,698)
                        print("i turn 1 sqaure") 
                        
                        # new screen
                        sleep(3)  
                        
                    # click on 2 sqaure
                        pt.moveTo(826,575)
                        sleep(0.5)
                        pt.click(826,575)
                        
                        # new screen
                        sleep(1)
                        
                        # click on yes
                        pt.moveTo(956,698) 
                        sleep(0.5)
                        pt.click(956,698)
                        print("i turn 2 sqaure") 

                        if img_15X is True:
                            print("No 30K")
                            # click next shuffle
                            sleep(1)
                            pt.moveTo(1282,694)
                            sleep(0.5)
                            pt.click(1282,694)
                            
                            # new screen
                            sleep(2)
                            
                            # move to yes
                            pt.moveTo(957,698)
                            sleep(0.5)
                            pt.click(957,698)   
                            break
                        
                        if img_15X is False:
                            print("BINGO")
                            
                        # click on 3 sqaure
                            pt.moveTo(826,441)
                            sleep(0.5)
                            pt.click(826,441) 
                            
                            #new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698)
                            print("i turn 3 sqaure") 
                            
                            # new screen
                            sleep(3)  
                            
                        # click on 4 sqaure
                            pt.moveTo(957,719)
                            sleep(0.5)
                            pt.click(957,719) 
                            
                            #new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698)
                            print("i turn 4 sqaure") 
                            
                            # new screen
                            sleep(3) 
                            
                        # click on 5 sqaure
                            pt.moveTo(957,596)
                            sleep(0.5)
                            pt.click(957,596)
                            
                            #new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("i turn 5 sqaure") 
                            
                            # new screen
                            sleep(3)  
                                
                        # click on 6 sqaure
                            pt.moveTo(958,441)
                            sleep(0.5)
                            pt.click(958,441)
                            
                            # new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("i turn 6 sqaure") 
                            
                            #new screen
                            sleep(3)
                             
                        # click on 7 sqaure
                            pt.moveTo(1084,707)
                            sleep(0.5)
                            pt.click(1084,707)
                            
                            # new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("i turn 7 sqaure") 
                            
                            #new screen
                            sleep(3)
                            
                        # click on 8 sqaure
                            pt.moveTo(1084,567)
                            sleep(0.5)
                            pt.click(1084,567)
                            
                            # new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("i turn 8 sqaure") 
                            
                            #new screen
                            sleep(3)
                                        
                        # click on 9 sqaure
                            pt.moveTo(1084,438)
                            sleep(0.5)
                            pt.click(1084,438)
                            
                            # new screen
                            sleep(2)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("you found 30K")
                            sleep(1)
                            
                        # post in chat
                            pt.moveTo(630,745)
                            sleep(0.5)
                            pt.click(630,745)
                            
                            # new screen
                            sleep(3)
                            
                            #share in city chat
                            pt.moveTo(1077,698)
                            sleep(0.5)
                            pt.click(1077,698)
                            
                            # new screen
                            sleep(2)
                            
                        #click on next shuffle
                            pt.moveTo(1282,694)
                            sleep(0.5)
                            pt.click(1282,694)
                            sleep(0.5)
                            break
        else:
            print("No 30K")
                
        # new screen
        sleep(1)
        
        img_20X= pt.locateOnScreen("imgs/dice/20X.png", grayscale=False, region=(761,371,400,400), confidence=0.94)
        if img_20X is not None:
            print("i see 20X")
            
            sleep(1)
            
            img_8H= pt.locateOnScreen("imgs/dice/8H.png", grayscale=False, region=(761,371,400,400), confidence=0.82)
            if img_8H is not None:
                print("i see 8H")
                
            # move to shuffle and click         
                pt.moveTo(1284,745)
                sleep(0.5)
                pt.click(1284,745)
                
                # new screen
                sleep(4)
                
            # click on 1 sqaure
                pt.moveTo(826,702)
                sleep(0.5)
                pt.click(826,702)
                
                #new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698)
                print("i turn 1 sqaure") 
                
                # new screen
                sleep(3)  
                
            # click on 2 sqaure
                pt.moveTo(826,575)
                sleep(0.5)
                pt.click(826,575)
                
                # new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698)
                print("i turn 2 sqaure") 
                
                # new screen
                sleep(3)  
                
            # click on 3 sqaure
                pt.moveTo(826,441)
                sleep(0.5)
                pt.click(826,441) 
                
                #new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698)
                print("i turn 3 sqaure") 
                
                # new screen
                sleep(3)  
                
            # click on 4 sqaure
                pt.moveTo(957,719)
                sleep(0.5)
                pt.click(957,719) 
                
                #new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698)
                print("i turn 4 sqaure") 
                
                # new screen
                sleep(3) 
                
            # click on 5 sqaure
                pt.moveTo(957,596)
                sleep(0.5)
                pt.click(957,596)
                
                #new screen
                sleep(1)
                
                # click on yes
                pt.moveTo(956,698) 
                sleep(0.5)
                pt.click(956,698) 
                print("i turn 5 sqaure") 
                
                # new screen
                sleep(3)  
                
                # check for 8H
                img_8H= pt.locateOnScreen("imgs/dice/8H.png", grayscale=False, region=(761,371,400,400), confidence=0.82)
                if img_8H is not None:
                    print("you found 1x 8H")
                    break
                
                if img_8H is None:
                    print("i not see 8H")
                    
                # click on 6 sqaure
                    pt.moveTo(958,441)
                    sleep(0.5)
                    pt.click(958,441)
                    
                    # new screen
                    sleep(1)
                    
                    # click on yes
                    pt.moveTo(956,698) 
                    sleep(0.5)
                    pt.click(956,698) 
                    print("i turn 6 sqaure") 
                    
                    #new screen
                    sleep(3)
                 
                    # check for 8H
                    img_8H= pt.locateOnScreen("imgs/dice/8H.png", grayscale=False, region=(761,371,400,400), confidence=0.82)
                    if img_8H is not None:
                        print("you found 1x 8H")
                        
                    # click next shuffle
                        sleep(1)
                        pt.moveTo(1282,694)
                        sleep(0.5)
                        pt.click(1282,694)
                        
                        # new screen
                        sleep(1)
                        
                    # move to yes
                        pt.moveTo(957,698)
                        sleep(0.5)
                        pt.click(957,698)
                        
                        # new screen
                        sleep(1)    
                        break
                    
                    # check for 8H
                    img_8H= pt.locateOnScreen("imgs/dice/8H.png", grayscale=False, region=(761,371,400,400), confidence=0.82)
                    if img_8H is None:
                        print("i not see 8H")
                        
                    # click on 7 sqaure
                        pt.moveTo(1084,707)
                        sleep(0.5)
                        pt.click(1084,707)
                        
                        # new screen
                        sleep(1)
                        
                        # click on yes
                        pt.moveTo(956,698) 
                        sleep(0.5)
                        pt.click(956,698) 
                        print("i turn 7 sqaure") 
                        
                        #new screen
                        sleep(3)
                        
                        img_8H= pt.locateOnScreen("imgs/dice/8H.png", grayscale=False, region=(761,371,400,400), confidence=0.82)
                        if img_8H is not None:
                            print("your fucked")
                            
                        # click next shuffle
                            sleep(1)
                            pt.moveTo(1282,694)
                            sleep(0.5)
                            pt.click(1282,694)
                            
                            # new screen
                            sleep(1)
                            
                            # move to yes
                            pt.moveTo(957,698)
                            sleep(0.5)
                            pt.click(957,698)
                            
                            # new screen
                            sleep(1)    
                            break
                        
                        # check for 8H    
                        img_8H= pt.locateOnScreen("imgs/dice/8H.png", grayscale=False, region=(761,371,400,400), confidence=0.82)
                        if img_8H is None:
                            print("i not see 8H")
                            
                        # click on 8 sqaure
                            pt.moveTo(1084,567)
                            sleep(0.5)
                            pt.click(1084,567)
                            
                            # new screen
                            sleep(1)
                            
                            # click on yes
                            pt.moveTo(956,698) 
                            sleep(0.5)
                            pt.click(956,698) 
                            print("i turn 8 sqaure") 
                            
                            #new screen
                            sleep(3)
                                    
                            if img_8H is not None:
                                print("you found 20X 8H")
                                
                            # post in chat
                                pt.moveTo(630,745)
                                sleep(0.5)
                                pt.click(630,745)
                                
                                # new screen
                                sleep(3)
                                
                            #share in city chat
                                pt.moveTo(1077,698)
                                sleep(0.5)
                                pt.click(1077,698)
                                
                                # new screen
                                sleep(2)
                                
                            #click on next shuffle
                                pt.moveTo(1282,694)
                                sleep(0.5)
                                pt.click(1282,694)
                                sleep(0.5)
                                break
                            
                            # check for 8H
                            img_8H= pt.locateOnScreen("imgs/dice/8H.png", grayscale=False, region=(761,371,400,400), confidence=0.82)
                            if img_8H is None:
                                print("i not see 8H")
                                
                            # click on 9 sqaure
                                pt.moveTo(1084,438)
                                sleep(0.5)
                                pt.click(1084,438)
                                
                                # new screen
                                sleep(2)
                                
                                # click on yes
                                pt.moveTo(956,698) 
                                sleep(0.5)
                                pt.click(956,698) 
                                print("you found 20x 8H")
                                
                            # post in chat
                                pt.moveTo(630,745)
                                sleep(0.5)
                                pt.click(630,745)
                                
                                # new screen
                                sleep(3)
                                
                            #share in city chat
                                pt.moveTo(1077,698)
                                sleep(0.5)
                                pt.click(1077,698)
                                
                                # new screen
                                sleep(2)
                                
                            #click on next shuffle
                                pt.moveTo(1282,694)
                                sleep(0.5)
                                pt.click(1282,694)
                                sleep(0.5)
                                break  
            
            if img_8H is None:
                print("i not see 8H")
            # click next shuffle
                sleep(1)
                pt.moveTo(1282,694)
                sleep(0.5)
                pt.click(1282,694)
                
                # new screen
                sleep(1)
                
                # move to yes
                pt.moveTo(957,698)
                sleep(0.5)
                pt.click(957,698)
                
                # new screen
                sleep(1)    
            print("i not see 20X")
            
            # click to next shuffle
            sleep(1)
            pt.moveTo(1282,694)
            sleep(0.5)
            pt.click(1282,694)
            
            # new screen
            sleep(0.5)
            
            # move to yes
            pt.moveTo(957,698)
            sleep(0.5)
            pt.click(957,698)
            
            # new screen
            sleep(1)
            break
            
        if img_20X is None:
            print("i not see 20X")
            
            # click to next shuffle
            sleep(1)
            pt.moveTo(1282,694)
            sleep(0.5)
            pt.click(1282,694)
            
            # new screen
            sleep(0.5)
            
            # move to yes
            pt.moveTo(957,698)
            sleep(0.5)
            pt.click(957,698)
            
            # new screen
            sleep(1)
            break


   