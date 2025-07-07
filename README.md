# 🐟 Fish Farming Expert System

A sophisticated AI-powered chatbot application designed to provide expert guidance on fish farming and aquaculture practices. Built with Streamlit and powered by OpenAI's fine-tuned language models, this system offers comprehensive advice on breeding, feeding, pond management, and disease prevention.

## 🌟 Features

- **Expert Fish Farming Guidance**: Specialized knowledge in aquaculture practices
- **Multilingual Support**: Available in English and Japanese
- **Fine-tuned AI Model**: Custom-trained on fish farming expertise
- **Interactive Chat Interface**: Modern, responsive UI with dark theme
- **Conversation Memory**: Maintains context throughout the conversation
- **Specialized Topics Coverage**:
  - Fish breeding techniques
  - Feeding strategies and nutrition
  - Pond management and setup
  - Water quality control
  - Disease prevention and treatment
  - Species selection guidance
  - Harvesting methods

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fish-farming-expert.git
   cd fish-farming-expert
   ```

2. **Install dependencies**
   ```bash
   pip install -r require.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

## 🔧 Configuration

### Model Configuration

The application uses a fine-tuned OpenAI model. To use your own fine-tuned model:

1. Update the model name in `app.py`:
   ```python
   llm = ChatOpenAI(
       model_name="your-fine-tuned-model-id",  # Replace with your model ID
       temperature=0.4,
       max_tokens=500,
       openai_api_key=os.getenv("OPENAI_API_KEY")
   )
   ```

### Language Support

The application currently supports:
- English (default)
- Japanese (日本語)

To add more languages, modify the language selection in the sidebar and update the prompt templates accordingly.

## 🤖 Fine-Tuning Process

This project includes a complete fine-tuning pipeline for creating a specialized fish farming expert model.

### Training Data

The fine-tuning dataset (`fish_farming_data.jsonl`) contains 111 carefully curated question-answer pairs covering:
- Pond management and setup
- Water quality parameters (pH, temperature, oxygen)
- Fish species compatibility
- Disease identification and prevention
- Feeding strategies and nutrition
- Predator protection methods
- Intensive vs extensive farming methods

### Fine-Tuning Steps

1. **Data Preparation**: The training data is formatted in JSONL format with system, user, and assistant messages
2. **Model Training**: Use the provided Jupyter notebook (`fine_tuning_for_fish_expertise.ipynb`) to:
   - Upload training data to OpenAI
   - Create a fine-tuning job
   - Monitor training progress
   - Retrieve the fine-tuned model ID

3. **Integration**: Update the model name in the application to use your fine-tuned model

### Running Fine-Tuning

```bash
# Open the Jupyter notebook
jupyter notebook fine_tuning_for_fish_expertise.ipynb
```

Follow the step-by-step process in the notebook to create your own fine-tuned model.

## 📁 Project Structure

```
fish-farming-expert/
├── app.py                              # Main Streamlit application
├── fine_tuning_for_fish_expertise.ipynb # Fine-tuning notebook
├── fish_farming_data.jsonl            # Training dataset
├── require.txt                         # Python dependencies
├── .env                               # Environment variables (create this)
└── README.md                          # Project documentation
```

## 🎨 UI Features

- **Dark Theme**: Professional dark interface with blue accents
- **Responsive Design**: Optimized for different screen sizes
- **Chat Interface**: WhatsApp-style message bubbles
- **Sidebar Controls**: Language selection and settings
- **Conversation History**: Persistent chat memory
- **Clear Chat**: Option to reset conversation

## 🔍 Usage Examples

### Basic Queries
- "What type of pond is best for fish farming?"
- "How do I maintain the pH level in my fish pond?"
- "What is the ideal temperature for farming trout?"

### Advanced Topics
- "Can I farm different species of fish together?"
- "How can I protect my fish from predators?"
- "What are the signs of disease in farmed fish?"

### Japanese Support
- "魚の繁殖技術について教えてください"
- "池の水質管理はどうすればいいですか？"

## 🛠️ Technical Details

### Dependencies

- **Streamlit**: Web application framework
- **LangChain**: LLM integration and conversation management
- **OpenAI**: AI model API
- **python-dotenv**: Environment variable management

### Architecture

- **Frontend**: Streamlit with custom CSS styling
- **Backend**: LangChain for conversation flow
- **AI Model**: Fine-tuned OpenAI GPT model
- **Memory**: ConversationBufferMemory for context retention

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- OpenAI for providing the base language models
- Streamlit team for the excellent web framework
- LangChain for conversation management tools
- Fish farming community for domain expertise


**Made with ❤️ for the aquaculture community**
