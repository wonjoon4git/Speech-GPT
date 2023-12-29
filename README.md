# Recommended Setup for Mac OS

To successfully run this app, follow these steps:

1. **Obtain OpenAI API Key**: First, ensure you have an API key from OpenAI. If you don't, acquire one from [OpenAI Platform](https://platform.openai.com/api-keys).

2. **Setup Configuration Folder**:
   - Create a folder named `.streamlit`.
   - Inside this folder, create a file named `secrets.toml`.

3. **API Key Configuration**:
   - Open the `secrets.toml` file.
   - Add your OpenAI API key in the following format: `OPENAI_API_KEY = "sk-xxxx-xxxxx-xxxx"`.

4. **Create a Virtual Environment**:
   - Use the command: `python -m venv env`.

5. **Activate the Virtual Environment**:
   - Run: `source env/bin/activate`.

6. **Install Required Packages**:
   - Execute: `pip install -r requirements.txt`.

7. **Run the Main Application**:
   - Start the app with: `streamlit run SpeechGPT.py`.

# About the Chatbot
- **Purpose**: This chatbot is designed to answer questions about President Joe Biden's speech regarding the Russian-Ukraine war.
- **Tools Used**: Langchain, Streamlit  

# Demonstration
![172 27 142 80_8501_](https://github.com/wonjoon4git/Speech-GPT/assets/96000435/55cbc8f0-34cf-4679-b6f8-102f30236350)
