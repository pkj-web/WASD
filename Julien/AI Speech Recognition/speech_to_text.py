
from openai import OpenAI

client = OpenAI(
    api_key = "sk-None-83q6P8hUUmP09JzQUKgVT3BlbkFJXbhMmfVLLZkkuIsRcNPi"
)

audio_file = open("my_audio.m4a", "rb")
transcript = client.audio.translations.create(
    model="whisper-1",
    file=audio_file
)

print(transcript.text)
