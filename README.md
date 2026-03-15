# 🔊 Gemini AI Text-to-Speech Generator (Python)

This repository contains a **Python script that converts large text files into spoken audio using Google's Gemini AI Text-to-Speech API**.

The script reads a text file, splits it into smaller chunks, sends each chunk to **Google Gemini TTS**, and saves the generated speech as **.wav audio files**.

It is designed to handle **very large text files** without hitting API limits by processing them piece-by-piece.

This makes it useful for:

- Creating **audiobooks**
- Generating **narration for videos**
- Converting **stories or scripts to speech**
- Producing **voiceovers automatically**

---

# 📁 Project Structure

```
PROJECT_FOLDER/
│
├── Main.py                # Main Python script
├── BUGGY_MAIN.txt         # Example text file to convert to speech
│
├── AUDIO_FILES/           # Generated audio files will appear here
│   ├── Buggy_0.wav
│   ├── Buggy_1.wav
│   └── ...
│
└── README.md
```

---

# ⚙️ Requirements

Make sure you install the required library before running the script.

```
pip install google-genai
```

---

# 🔑 Get Your Free Gemini API Key

To use the script you must generate your own API key.

Visit:

https://aistudio.google.com/app/apikey

Steps:

1. Sign in with your Google account
2. Create a new API key
3. Copy the key
4. Paste it into the script

Replace this line in `Main.py`:

```python
client = genai.Client(api_key="ENTER YOUR API-KEY HERE")
```

with your own API key.

---

# ▶️ How the Script Works

The program follows these steps:

### 1️⃣ Read the Text File

The script loads a text file containing the text that will be spoken.

Example:

```python
Txt_File_name = 'BUGGY_MAIN.txt'
```

---

### 2️⃣ Split the Text Into Chunks

Large text is automatically divided into smaller sections.

This prevents API size limits from stopping the program.

Function used:

```
split_text()
```

---

### 3️⃣ Send Text to Gemini TTS

Each chunk is sent to the **Gemini Text-to-Speech model**.

Model used:

```
gemini-2.5-flash-preview-tts
```

Voice used:

```
Puck
```

The prompt tells the AI to read the text with a **warm, friendly, and slightly savage tone**.

---

### 4️⃣ Receive Audio From Gemini

Gemini returns the audio in **PCM format**, which is then converted into a `.wav` file.

---

### 5️⃣ Save the Audio Files

Each chunk is saved individually.

Example output:

```
AUDIO_FILES/
Buggy_0.wav
Buggy_1.wav
Buggy_2.wav
```

---

# 🚀 Running the Program

Simply run the Python script:

```
python Main.py
```

Console output will show the progress:

```
PROGRAMM STARTED SUCCESFULLY

Processing chunk 1/5...
Chunk 1/5 processed and saved as Buggy_0.wav

Processing chunk 2/5...
Chunk 2/5 processed and saved as Buggy_1.wav
...
PROGRAMM ENDED SUCCESFULLY
```

---

# 🧠 Customizing the Script

You can change the **text file input** and **audio file name**.

Example:

```python
Txt_File_name = 'MY_STORY.txt'
SAVE_FILENAME = 'MyAudio'
```

This will produce:

```
AUDIO_FILES/
MyAudio_0.wav
MyAudio_1.wav
```

---

# 🎙️ Changing the Voice

The script currently uses the **Puck voice**.

Inside the configuration:

```python
voice_name="Puck"
```

You can replace it with another available Gemini voice if supported.

---

# ⏱ Rate Limit Protection

The script includes a delay between requests:

```python
time.sleep(10)
```

This helps prevent **API rate limit errors**.

You can adjust this delay depending on your usage.

---

# 📌 Important Notes

- The script saves audio in **WAV format**
- Each text chunk produces **one audio file**
- Large books may generate **many audio files**
- You can later **merge them using audio editing tools**

---

# 👨‍💻 Author

**Peter (Ezee Kits)**

YouTube Channel  
https://www.youtube.com/@Ezee_Kits

Content Focus:

- Python Programming
- Automation
- Machine Learning
- AI Tools
- Technology Tutorials

---

# 📜 License

This project is open source and available for **educational and personal use**.

Please respect Google's API usage policies when using the Gemini API.

---

# ⭐ If You Found This Useful

Consider starring the repository to support the project!

```
⭐ Star the repository
🍴 Fork it
🚀 Build something awesome
```
