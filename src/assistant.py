import os
from typing import Optional

import openai
import speech_recognition as sr
import pyttsx3


class JARVISAssistant:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

        openai.api_key = self.api_key
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def listen(self) -> Optional[str]:
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except Exception as exc:
            print(f"Could not understand audio: {exc}")
            return None

    def speak(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()

    def generate_response(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are JARVIS, a helpful AI assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
        )
        return response["choices"][0]["message"]["content"].strip()

    def start(self) -> None:
        self.speak("JARVIS online. How may I assist you?")

        while True:
            command = self.listen()
            if not command:
                self.speak("I did not catch that. Please repeat.")
                continue

            print(f"You: {command}")
            reply = self.generate_response(command)
            print(f"JARVIS: {reply}")
            self.speak(reply)
