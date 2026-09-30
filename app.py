import os
from dotenv import load_dotenv
from src.assistant import JARVISAssistant

load_dotenv()


def main():
    assistant = JARVISAssistant()
    assistant.start()


if __name__ == "__main__":
    main()
