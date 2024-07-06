# Jarvis - Personal Assistant

Jarvis is a personal assistant that can perform various tasks through voice commands, such as sending emails, searching for music, browsing the web, and more. The assistant utilizes several Python libraries to recognize speech, convert text to speech, and interact with web services.

## Features
- **Speech Recognition:** Listens and recognizes voice commands using `speech_recognition`.
- **Text-to-Speech:** Responds with synthesized speech using `pyttsx3`.
- **Email Sending:** Sends emails by fetching contact information from an Excel file.
- **Music Playback:** Searches and plays music from a predefined library.
- **Web Search:** Opens web pages for Google, YouTube, Spotify, and social media.
- **News Fetching:** Retrieves and reads the latest news headlines.

## Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare the Excel File:**
   - Create an `list.xlsx` file in the project directory with columns `Name` and `Email`.

4. **Configure Email Credentials:**
   - Replace `EMAIL_ADDRESS` and `EMAIL_PASSWORD` in the code with your email credentials.

## Usage
1. **Run the Script:**
   ```sh
   python your_script_name.py
   ```

2. **Interact with Jarvis:**
   - Say "Ram" to wake up Jarvis.
   - Give commands such as "send mail to [name]", "play [song]", "google [query]", "search YouTube for [query]", etc.

## Commands
- **Send Email:** "send mail to [name]"
- **Play Music:** "play [song]"
- **Search Spotify:** "search Spotify for [query]"
- **Google Search:** "google [query]"
- **Search YouTube:** "search YouTube for [query]"
- **Open Facebook:** "facebook"
- **Open LinkedIn:** "linkedin"
- **Open Instagram:** "instagram"
- **Open Reels:** "reels"
- **Watch Movies:** "movies"
- **Read News:** "news"

## Requirements
- Python 3.6+
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `webbrowser`
  - `urllib`
  - `requests`
  - `pandas`
  - `smtplib`
  - `email`
  - `openpyxl`

## Acknowledgments

- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [newsapi](https://newsapi.org/)
