import pyttsx3
import PyPDF2
import time

book = open('trip_of_dreams.pdf', 'rb')
reader = PyPDF2.PdfFileReader(book)

# init function to get an speaker instance for the speech synthesis
speaker = pyttsx3.init()
""" RATE"""
rate = speaker.getProperty('rate')  # getting details of current speaking rate
print(rate)  # printing current voice rate
speaker.setProperty('rate', 160)  # setting up new voice rate

"""VOLUME"""
volume = speaker.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
speaker.setProperty('volume', 1)  # setting up volume level  between 0 and 1

"""VOICE"""
# The pyttsx3 module supports two voices first is female
voice = speaker.getProperty('voices')  # getting details of current voice
print('voice')
if (voice == 1):
    print('Female ')
else:
    print('Male ')
# speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

pages = reader.numPages
print('number of pages in the book is:',pages)
for num in range(0,  pages):
    page = reader.getPage(num)
    text = page.extractText()
    # built-in say() function in the pyttsx3 package that convert the text to speech
    speaker.say(text)
    # This function will make the speech audible in the system
    speaker.runAndWait()
    time.sleep(0)


######################################################################
# the measurment after assigning (rate , voice and volume ) and changed from the default
# rate_1 = speaker.getProperty('rate')
# print(rate_1)
######################################################################
