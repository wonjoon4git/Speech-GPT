from langchain.prompts import ChatPromptTemplate
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import CacheBackedEmbeddings, OpenAIEmbeddings
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.storage import LocalFileStore
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.callbacks.base import BaseCallbackHandler
import streamlit as st

# Custom callback handler class as an event listener in the chat application
class ChatCallbackHandler(BaseCallbackHandler):
    message = ""
    
    # Callback for the start of language model processing
    def on_llm_start(self, *args, **kwargs):
        self.message_box = st.empty() # creates an empty box

    # Callback for the end of language model processing
    def on_llm_end(self, *args, **kwargs):
        save_message(self.message, "ai")
        
    # Callback for each new token generated by the language model
    def on_llm_new_token(self, token, *args, **kwargs):
        self.message += token
        self.message_box.markdown(self.message)

# Creating an instance of ChatOpenAI with specific configurations
llm = ChatOpenAI(
    temperature=0.1,    # Creativity of a model
    streaming=True,     # Enabled Streaming Text Generation
    callbacks=[
        ChatCallbackHandler(), # Using our Custom Callbacks
    ],
)

# Function to embed a file (Speech.pdf in our case) and prepare it for retrieval
# This function will only run when we don't have the embedding of "Speech.pdf."
@st.cache_data(show_spinner="Loading...")
def embed_file():
    file_path = "./.cache/files/Speech.pdf"
    cache_dir = LocalFileStore("./.cache/embeddings/Speech.pdf")
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=300,
        chunk_overlap=50,
    )
    
    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split(text_splitter=splitter)
    embeddings = OpenAIEmbeddings()
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)
    vectorstore = FAISS.from_documents(docs, cached_embeddings)
    retriever = vectorstore.as_retriever()
    return retriever

# Function to save messages in the session state
def save_message(message, role):
    st.session_state["messages"].append({"message": message, "role": role})


# Function to send a message and optionally save it (that is, when the message is a new, most recent message)
def send_message(message, role, save=True):
    with st.chat_message(role):
        st.markdown(message)
    if save:
        save_message(message, role)


# Function to display the history of messages (in session_state)
def display_log():
    for message in st.session_state["messages"]:
        send_message(
            message["message"],
            message["role"],
            save=False # We don't want to create duplicates in session_state
        )

# Function to format documents for display
def format_docs(docs):
    return "\n\n".join(document.page_content for document in docs)



# Creating a prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are going to be asked about about United States' President Joe Biden's Speech on Russian-Ukraine war. 
            Answer the question ONLY using the following context. If you don't know the answer just say you don't know. DO NOT make things up.
            
            Context: {context}
            """
        ),
        ("human", "{question}")
    ]
)


# Configurations for the Streamlit app
st.set_page_config(
    page_title="SpeechGPT",
    page_icon="👾"
)

st.title("SpeechGPT")

st.markdown(
"""     
Use this chatbot to ask questions about President Joe Biden's Speech on Russian-Ukraine war. 
"""
)

# Initializing the messages in the session state if not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = []
    
# Prepare the retriever
retriever = embed_file()

# Displaying the initial AI message and the chat history
send_message("I am ready!", "ai", save=False)
display_log()

# Handling user input and processing it through the chat pipeline
message = st.chat_input("Message SpeechGPT...")
if message:
    send_message(message, "human")
    chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
    )
    with st.chat_message("ai"):
        chain.invoke(message)


