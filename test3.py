import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set the voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change the index to select a different voice

# Text to speech conversion
text = "Hello, world! This is a text to speech example."
engine.say(text)

# Run the speech engine
engine.runAndWait() 