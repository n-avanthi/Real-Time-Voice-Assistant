# Real-Time Voice Assistant using Python

This project is a real-time voice assistant implemented in Python. It utilizes speech recognition and text-to-speech conversion to interact with users through voice commands.

## Features

- Speech recognition: The assistant can understand spoken commands from the user.
- Text-to-speech: The assistant responds to the user's commands with synthesized speech.
- Real-time interaction: The assistant provides immediate responses to user queries.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/n-avanthi/Real-Time-Voice-Assistant.git
    ```

2. Navigate to the project directory:

    ```bash
    cd real-time-voice-assistant
    ```

3. Create and update the `.env` file:

    ```bash
    GEMINI_API_KEY="Your-Gemini-API-key"
    ```

## Usage

1. Run the main Python script:

    ```bash
    python voice_assistant.py
    ```

2. Once the program is running, the voice assistant will listen for commands. Speak clearly and wait for the assistant to respond.

3. You can interact with the voice assistant using various commands such as:
   - "What colors are in a rainbow?"
   - "Tell me a joke."
   - "What is the capital of Canada?"
     
   Under the `output` folder, a sample demo image is present.
4. The keyword 'exit' can be used to exit out of a conversation 

## Acknowledgments

- This project utilizes the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library for speech recognition.
- Text-to-speech functionality is powered by the [gTTS](https://pypi.org/project/gTTS/) library.
- The project also integrates Gemini API for responding to user prompts.
