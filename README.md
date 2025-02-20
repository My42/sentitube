# SentimentXplorer

SentimentXplorer is a real-time sentiment analysis tool for tweets. It retrieves tweets based on keywords and uses a language model (LLM) to analyze their sentiment (positive, neutral, negative).

## 🚀 Features

- Real-time tweet retrieval via the Twitter/X API
- Sentiment analysis using the OpenAI API (GPT-4) or a local model
- Storage and real-time trend visualization
- Web interface to display results

## 🛠️ Installation

### 1. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Configuration

1. **Create a `.env` file** to store your API keys:

```
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
OPENAI_API_KEY=your_openai_api_key
```

2. **Obtain API keys**:
   - [Twitter Developer Portal](https://developer.twitter.com/)
   - [OpenAI API](https://platform.openai.com/)

## 🚀 Usage

### 1. Start retrieving and analyzing tweets
```bash
python main.py
```

### 2. Launch the web interface (example with Streamlit)
```bash
streamlit run app.py
```

## 📌 Future Improvements
- Support for open-source models like BERT
- Interactive dashboard with more visualizations
- Batch processing optimization

## 📜 License
This project is licensed under the MIT License.
