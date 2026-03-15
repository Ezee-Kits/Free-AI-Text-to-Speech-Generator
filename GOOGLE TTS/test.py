from google import genai
from google.genai import types
import wave
import time
import os







'''
-------------------------------------------------------------------------------
MAKE SURE TO HAVE THE FOLLOWINGS INSTALLED;
pip install google-genai
https://aistudio.google.com/app/apikey  # GET YOUR OWN FREE API KEY HERE
-------------------------------------------------------------------------------

'''

client = genai.Client(api_key="ENTER YOUR API-KEY HERE")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def Audio_SavePath(NAME):
    full_path = os.path.join(BASE_DIR, "AUDIO_FILES")
    os.makedirs(full_path, exist_ok=True)
    return os.path.join(full_path, NAME)



def save_wave(filename, pcm):
    
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(pcm)


def split_text(text, max_size=5000):

    words = text.split()
    chunks = []
    current = []

    for word in words:

        current.append(word)

        if len(" ".join(current)) > max_size:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks


# Read text file
Txt_File_name = 'BUGGY_MAIN.txt' #---> ENTER TEXT FILE NAME HERE
SAVE_FILENAME = 'Buggy'          #---> ENTER NAME TO SAVE THE AUDIO FILE HERE

text_path = os.path.join(BASE_DIR, Txt_File_name)

with open(text_path, "r", encoding="utf-8") as f:
    text_data = f.read()

chunks = split_text(text_data)

file_name = Audio_SavePath(NAME=SAVE_FILENAME)
print('\n PROGRAMM STARTED SUCCESFULLY \n')

for i, chunk in enumerate(chunks):
    print(f"Processing chunk {i+1}/{len(chunks)}...")
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=f"Read aloud in a warm and friendly and savage tone: : {chunk}",
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Puck"
                    )
                )
            )
        )
    )

    audio_data = response.candidates[0].content.parts[0].inline_data.data

    save_wave(f"{file_name}_{i}.wav", audio_data)
    print(f"Chunk {i+1}/{len(chunks)} processed and saved as {file_name}_{i}.wav")
    time.sleep(10)  # Sleep to avoid hitting rate limits
print('\n PROGRAMM ENDED SUCCESFULLY \n')

