import keyboard
import win32api, win32con
import pyautogui
import time

def twerk_2(duration):
    sec = 5
    print("Twerking and mining in ")
    for t in range(sec, 0, -1):
        print(t)
        time.sleep(0.9)

    for dur in range(int(duration)):
        print(f"{dur}: Twerk and mining..")
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        for t in range(4):
            keyboard.press("left shift")
            time.sleep(0.10)
            keyboard.release("left shift")
            time.sleep(0.3)

    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)




def twerk():
    sec = 5
    flag = True

    while flag == True:
        print("Enter 0 to cancel.. ")
        duration = input("Enter how many twerks: ")
        if duration.isnumeric() == False or int(duration) == 0:
            break
        print("Initializing..")
        time.sleep(1.5)

        print("Enter 0 to cancel.. ")
        choice = input("Enable auto mine? y / n?: ")
        if choice == "y" or choice == "Y":
            twerk_2(duration)
        elif choice == "n" or choice == "N":
            print("Twerking in ")
            for t in range(sec, 0, -1):
                print(t)
                time.sleep(0.9)
            for dur in range(int(duration)):
                print(f"{dur}: Twerking..")
                keyboard.press("left shift")
                time.sleep(0.10)
                keyboard.release("left shift")

                if dur % 5 == 0:
                    time.sleep(4.0)
                else:
                    time.sleep(0.10)
        else:
            break
        flag = False

def mine(duration):
    x, y = 982, 585
    sec = 5
    print("Initializing..")
    print("Make sure you are facing the block you want to mine for a period of time..")
    time.sleep(5.0)
    print("Mining for {duration} seconds in..")
    for t in range(sec, 0, -1):
        print(t)
        time.sleep(0.9)

    print(f"Mining in commence..")
    time.sleep(2.0)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0 )
    time.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def pick_check():
    try:
        img_loc = pyautogui.locateOnScreen('pick2.png', grayscale=False, region= (1150, 600, 200, 200), confidence=0.7)
        # x, y = pyautogui.locatecenterOnScreen('backtogame.png', grayscale=False, confidence=0.80)
        # if x is not None:
        #     if y is not None:
        #         win32api.SetCursorPos((x, y))
        #         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        #         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        if img_loc is not None:
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        try:
            return False
        except pyautogui.raisePyAutoGUIImageNotFoundException:
            return False
def till_the_dirt(duration):
    sec = 5
    x, y = 982, 585

    print("Initializing..")
    print("Make sure you facing the block to till and equiped with hoe..")
    time.sleep(5.0)
    print("Tilling in..")
    for t in range(sec, 0, -1):
        print(t)
        time.sleep(0.9)


    for dur in range(int(duration)):
        print(f"{dur}: Tilling..")
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        time.sleep(0.2)

        keyboard.press_and_release("2")
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.4)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.2)

        keyboard.press_and_release("3")
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        time.sleep(0.2)

        keyboard.press_and_release("1")



def for_berries(duration):
    sec = 5
    x, y = 982, 585

    print("Initializing..")
    print("Make sure your crosshair is in the hitbox of berry..")
    time.sleep(5.0)
    print("Harvesting Berries in..")
    for t in range(sec, 0, -1):
        print(t)
        time.sleep(0.9)


    for dur in range(int(duration)):
            print(f"{dur}: Harvesting..")
            time.sleep(0.2)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            time.sleep(0.2)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

            for t in range(4):
                keyboard.press("left shift")
                time.sleep(0.10)
                keyboard.release("left shift")
                time.sleep(0.3)


def change_tab(tabnum):
    print("Changing tab")
    keyboard.press_and_release(f"{tabnum}")

def move():
    print("Moving..")
    keyboard.press("a")
    time.sleep(0.25)
    keyboard.release("a")

    keyboard.press("d")
    time.sleep(0.25)
    keyboard.release("d")


def menu():

    while keyboard.is_pressed("q") == False:

        print("====================================================")
        print("Enter the number of the thing you want to do.")
        print("====================================================")


        print("""
        1. Mine
        2. Twerk
        3. Move
        4. Harvest Berries
        5. Till a single block
        0. Exit
        """)

        choice = input("Enter here: ")
        if choice.isnumeric():

            if int(choice) == 1:
                print("==========You choose mining=========")
                time.sleep(2.0)
                mine(int(input("Enter duration in seconds: "))) #place the cursor to the block you want to currently mine
            elif int(choice) == 2:
                print("==========You choose Twerking=========")
                twerk()
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                print("Mining stopped")
            elif int(choice) == 3:
                move()
            elif int(choice) == 4:
                print("==========You choose Harvesting berries=========")
                for_berries(int(input("Enter Harvest count: ")))
                print("Harvesting stopped")
            elif int(choice) == 5:
                print("==========You choose Tilling a block=========")
                till_the_dirt(int(input("Enter Tilling count: ")))
            elif int(choice) == 0:
                break
        else:
            pass

        #img = pyautogui.screenshot("sample.png", region=(1150, 600, 200, 200))
        #time.sleep(10.0)





