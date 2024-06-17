import webbrowser as web
from time import sleep
import pyautogui as pg

pg.FAILSAFE = False

def send_whatsapp_message(phone_number, message, wait_time=20):
    try:
        web.open(f"https://web.whatsapp.com/send?phone={phone_number}")
        sleep(wait_time)
        
        pg.hotkey('ctrl', 'a')  # selects the existing text(draft entered previously)
        pg.press('backspace')   # this deletes it

        index = 0
        length = len(message)
        
        while index < length:
            letter = message[index]
            pg.write(letter)
            
            if letter == ":":
                index += 1
                while index < length:
                    letter = message[index]
                    if letter == ":":
                        pg.press("enter")
                        break
                    pg.write(letter)
                    index += 1
            index += 1
        
        pg.press('enter')
        print("Message sent successfully.")
    
    except Exception as e:
        print(f"Error occurred: {e}")

phone_number = "+8594854854" # dummy number for safety :P
message = "HAVE FUN!"

send_whatsapp_message(phone_number, message)
