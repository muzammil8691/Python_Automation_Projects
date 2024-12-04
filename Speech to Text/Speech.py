import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Talk")
    # Adjust the recognizer sensitivity to ambient noise
    r.adjust_for_ambient_noise(source)
    
    # Listen for audio and store it in audio_text
    audio_text = r.listen(source)
    print("Recognizing...")
    
    # Recognize the speech using Google Web Speech API
    try:
        text = r.recognize_google(audio_text)
        print("You said: ", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
