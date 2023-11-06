import os
from simple_colors import *
import pywhatkit 
from playsound import playsound
from countryinfo import CountryInfo
from sketchpy import library as lib

print (blue("\t\t\t\tWelcome to Uinque project\n","underlined"))

while True:
    print(red("""Press 1: To send email
                 Press 2: To send sms
                 Press 3: To send Whatsup message
                 Press 4: to open chrome browser
                 Press 5: To send aduio clip
                 Press 6: To oepn notepad
                 Press 7: to open wmplayer
                 Press 8: To exit
                 Press 9: To get inforamtion about India
                 press 10: To get the images"""))
    
    ch = input(green("Enter your choice :"))
    if int(ch) == 1:
       print("email")
    elif int(ch) ==2:
        print("sms")
    elif int(ch) == 3:
        sendmessage= pywhatkit.sendwhatmsg("+919821xxxxxx","Hi how are you",18,33)
        print("sendmessage")
    elif int(ch) == 4:
        print(os.system("chrome"))
    elif int(ch) == 5:
        audioclip = playsound("C:\\Users\\Bhaskar\\Downloads\\TopTen.mp3")
        print("aduioclip")
    elif int(ch) == 6:
        print(os.system("notepad"))
    elif int(ch) == 7:
        print(os.system("wmplayer"))
    elif int(ch) == 8:
        print("exit")
    elif int(ch) == 9:
        country = CountryInfo("India")
        # Here we can get info about our country Inida like total states,geographical information etc.
        data = country.info()
        print(data)
    elif int(ch) == 10:
        image= lib.apj()
        # Here we can get lot of celebrity images.
        image.draw()
        print("image")
        break
    else:
        ("Not supported")


