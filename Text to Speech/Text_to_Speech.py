#pip install gTTS

from gtts import gTTS

# text = '''
# Hello this is a text to speech converter.
# It uses the gTTS library and a few lines of code to do this. 
# It is super easy.
# '''

text = "میرا نام مزمل ہے اور میں حال ہی میں سوفٹ ویئر انجینئرنگ میں گریجویٹ ہوا ہوں۔"

langauge = 'ur'

myobj = gTTS(text= text, lang= langauge, slow= False, tld="co.in")

myobj.save("text_to_speech2.mp3")
