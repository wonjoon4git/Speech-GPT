# Recommended Setup (for Mac OS)

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
![172 27 142 80_8501_](https://github.com/wonjoon4git/Speech-GPT/assets/96000435/d4dcd503-a9bb-4e21-ace9-fa71aa03e295)
![172 27 142 80_8501_ (2)](https://github.com/wonjoon4git/Speech-GPT/assets/96000435/57479be8-4dd8-4fff-b17e-20aa0cb1cb73)
![172 27 142 80_8501_ (3)](https://github.com/wonjoon4git/Speech-GPT/assets/96000435/e9436136-616a-49b5-9e83-a2ef9d7140d1)
![172 27 142 80_8501_ (4)](https://github.com/wonjoon4git/Speech-GPT/assets/96000435/a202b2c1-2fcf-49a3-8bcc-ef4fe0b3554c)


