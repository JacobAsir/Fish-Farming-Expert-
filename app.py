import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Fish Farming Expert System",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme with blue accents
st.markdown("""
<style>
    /* Main app background */
    .stApp {
        background-color: #1a1a1a;
    }
    
    /* Chat container styling */
    .chat-container {
        background-color: #2d2d2d;
        border-radius: 10px;
        padding: 20px;
        height: 500px;
        overflow-y: auto;
        border: 1px solid #3d3d3d;
        margin-bottom: 20px;
    }
    
    /* Message styling */
    .user-message {
        background-color: #0084ff;
        color: white;
        padding: 10px 15px;
        border-radius: 18px;
        margin: 5px 0;
        max-width: 70%;
        float: right;
        clear: both;
    }
    
    .assistant-message {
        background-color: #3a3a3a;
        color: #e0e0e0;
        padding: 10px 15px;
        border-radius: 18px;
        margin: 5px 0;
        max-width: 70%;
        float: left;
        clear: both;
    }
    
    /* Title styling */
    h1 {
        color: #ffffff;
        font-weight: 300;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #2d2d2d;
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        background-color: #3a3a3a;
        color: white;
        border: 1px solid #4a4a4a;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #0084ff;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: 500;
    }
    
    .stButton > button:hover {
        background-color: #0066cc;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background-color: #3a3a3a;
        color: white;
    }
    
    /* Scrollbar styling */
    .chat-container::-webkit-scrollbar {
        width: 8px;
    }
    
    .chat-container::-webkit-scrollbar-track {
        background: #2d2d2d;
    }
    
    .chat-container::-webkit-scrollbar-thumb {
        background: #0084ff;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "language" not in st.session_state:
    st.session_state.language = "English"
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history", return_messages=True)
if "previous_language" not in st.session_state:
    st.session_state.previous_language = "English"

# Initialize LangChain components
@st.cache_resource
def init_langchain():
    # Initialize ChatOpenAI with your fine-tuned model
    llm = ChatOpenAI(
        model_name="your model",  # Replace with your fine-tuned model
        temperature=0.4,
        max_tokens=500,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Create prompt template
    prompt_template = """
    You are an expert in fish farming, providing detailed and accurate information on various aspects of fish cultivation, including breeding, feeding, and pond management.
    
    {language_instruction}
    
    Your responses should be precise, detailed, and have a conversational touch. Focus on providing practical advice and scientific information about fish farming.
    
    Chat history: {history}
    
    User question: {message}
    
    If the user asks anything outside of fish farming scope, politely redirect them to fish farming topics.
    """
    
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=['history', 'message', 'language_instruction']
    )
    
    # Create LLM chain
    chain = LLMChain(llm=llm, prompt=PROMPT, verbose=False)
    
    return chain

# Function to get response using LangChain
def get_fish_farming_response(message, language):
    chain = init_langchain()
    
    # Language instruction based on selection
    language_instruction = ""
    if language == "Japanese":
        language_instruction = "Please respond in Japanese language."
    
    # Get conversation history
    history = st.session_state.memory.chat_memory.messages
    
    try:
        # Get response from chain
        response = chain.run(
            history=history,
            message=message,
            language_instruction=language_instruction
        )
        
        # Update memory
        st.session_state.memory.chat_memory.add_user_message(message)
        st.session_state.memory.chat_memory.add_ai_message(response)
        
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Main app layout - Title remains in English
st.title("🐟 Fish Farming Expert System")

# Sidebar for language selection and settings
with st.sidebar:
    # Settings section
    settings_text = "### Settings" if st.session_state.language == "English" else "### 設定"
    st.markdown(settings_text)
    
    language = st.selectbox(
        "Select Language / 言語を選択",
        ["English", "Japanese"],
        index=0 if st.session_state.language == "English" else 1,
        key="language_selector"
    )
    
    # Check if language has changed
    if language != st.session_state.previous_language:
        st.session_state.language = language
        st.session_state.previous_language = language
        # Update the initial message if it exists
        if len(st.session_state.messages) > 0 and st.session_state.messages[0]["role"] == "assistant":
            welcome_message = (
                "Hello! I'm your Fish Farming Expert. I can help you with all aspects of fish farming including breeding techniques, feeding strategies, pond management, water quality control, and disease prevention. What would you like to know about fish farming today?"
                if language == "English"
                else "こんにちは！私は養殖専門家です。魚の繁殖技術、給餌戦略、池の管理、水質管理、病気の予防など、養殖のあらゆる側面についてお手伝いできます。今日は養殖について何をお知りになりたいですか？"
            )
            st.session_state.messages[0]["content"] = welcome_message
    else:
        st.session_state.language = language
    
    st.markdown("---")
    
    # About section
    about_text = "### About" if language == "English" else "### について"
    st.markdown(about_text)
    
    if language == "English":
        st.markdown("""
        This Fish Farming Expert provides guidance on:
        - Fish breeding techniques
        - Feeding strategies
        - Pond management
        - Water quality control
        - Disease prevention
        - Species selection
        - Harvesting methods
        """)
    else:
        st.markdown("""
        この養殖専門家は以下についてガイダンスを提供します：
        - 魚の繁殖技術
        - 給餌戦略
        - 池の管理
        - 水質管理
        - 病気の予防
        - 種の選択
        - 収穫方法
        """)
    
    # Clear chat button
    clear_button_text = "Clear Chat History" if language == "English" else "チャット履歴をクリア"
    if st.button(clear_button_text):
        st.session_state.messages = []
        st.session_state.memory.clear()
        st.rerun()

# Main chat interface
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    # Chat header
    chat_header = "### 💬 Fish Expert Chat" if language == "English" else "### 💬 養殖専門家チャット"
    st.markdown(chat_header)
    
    # Create a container for the chat messages with custom styling
    chat_html = '<div class="chat-container">'
    
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            chat_html += f'<div class="user-message">{message["content"]}</div>'
        else:
            chat_html += f'<div class="assistant-message">{message["content"]}</div>'
    
    chat_html += '<div style="clear: both;"></div></div>'
    
    # Render the chat container
    st.markdown(chat_html, unsafe_allow_html=True)
    
    # Chat input form
    with st.form("chat_form", clear_on_submit=True):
        col_input, col_button = st.columns([5, 1])
        
        with col_input:
            placeholder_text = "Type your question here..." if language == "English" else "ここに質問を入力してください..."
            user_input = st.text_input(
                "Ask about fish farming...",
                placeholder=placeholder_text,
                label_visibility="collapsed"
            )
        
        with col_button:
            submit_button = st.form_submit_button(
                "Send" if language == "English" else "送信", 
                use_container_width=True
            )
    
    # Process user input
    if submit_button and user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get assistant response using LangChain
        spinner_text = "Thinking..." if language == "English" else "考え中..."
        with st.spinner(spinner_text):
            response = get_fish_farming_response(user_input, language)
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to update the chat display
        st.rerun()

# Initial greeting message
if len(st.session_state.messages) == 0:
    welcome_message = (
        "Hello! I'm your Fish Farming Expert. I can help you with all aspects of fish farming including breeding techniques, feeding strategies, pond management, water quality control, and disease prevention. What would you like to know about fish farming today?"
        if language == "English"
        else "こんにちは！私は養殖専門家です。魚の繁殖技術、給餌戦略、池の管理、水質管理、病気の予防など、養殖のあらゆる側面についてお手伝いできます。今日は養殖について何をお知りになりたいですか？"
    )
    st.session_state.messages.append({"role": "assistant", "content": welcome_message})
    st.rerun()
