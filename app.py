import webbrowser as web
from time import sleep
import pyautogui as pg
import os
import google.generativeai as genai
from dotenv import load_dotenv
from InquirerPy import prompt
import glob

pg.FAILSAFE = False

load_dotenv()

def send_whatsapp_message(phone_number, message, wait_time=30):
    try:
        web.open(f"https://web.whatsapp.com/send?phone={phone_number}")
        sleep(wait_time)
        
        pg.hotkey('ctrl', 'a')  # selects the existing text (draft entered previously)
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
        print(f"Message sent successfully to {phone_number}.")
        
        sleep(2)
        
        # closing whatsapp tab
        pg.hotkey('ctrl', 'w')

    except Exception as e:
        print(f"Error occurred: {e}")

def list_txt_files():
    # lists all .txt files except requirements.txt
    txt_files = glob.glob("*.txt")
    txt_files.remove("requirements.txt")
    return txt_files

def choose_file():
    txt_files = list_txt_files()
    if not txt_files:
        print("No .txt files found in the directory.")
        return None
    
    questions = [
        {
            'type': 'list',
            'name': 'file',
            'message': 'Select a file:',
            'choices': txt_files
        }
    ]
    answer = prompt(questions)
    return answer['file']

def send_messages_to_contacts(file_path, wish):
    try:
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        with open(file_path, 'r') as file:
            contacts = file.readlines()
            for contact in contacts: # generate a unique wish for each contact
                response = model.generate_content(f'Please generate a wish with the requirement: {wish}')
                message = response.text.strip() 
                print(f"Generated message:\n{message}\n")
                phone_number = contact.strip()  
                send_whatsapp_message(phone_number, message)
                sleep(5) 
    
    except Exception as e:
        print(f"Error occurred while sending messages: {e}")

file_path = choose_file()
if file_path:
    wish = input("What kind of wish do you want to generate? ")
    send_messages_to_contacts(file_path, wish)
else:
    print("No file selected. Exiting the program.")
