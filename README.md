# 🔎 LinkedIn Intelligence Search Agent

An AI-powered LinkedIn profile search tool built using **LangChain ReAct agents**, **Groq (Moonshot AI Kimi)**, and **Tavily Search API** — with a clean **Streamlit** frontend.

Search for people, companies, and professionals on LinkedIn using natural filters like city, role, college, and company — no manual browsing required.

---

## 🚀 Demo

> Search for a person by name + role + city:
> **"Sam Altman, CEO, San Francisco"** → Returns the LinkedIn profile with URL, summary, and relevance score.

> Search for a company:
> **"NVIDIA"** → Returns company page + associated employees.

---

## 🧠 How It Works

```
User Input (Streamlit UI)
       ↓
LangChain ReAct Agent (Groq / Kimi Model)
       ↓
  LinkedInSearch Tool
       ↓
Tavily API (Web Search on linkedin.com)
       ↓
Middleware → Filter (score ≥ 0.3) → Format
       ↓
Structured Output → Streamlit Display
```

The agent reasons step-by-step (ReAct pattern):

1. **Think** about what to search
2. **Act** by calling the `LinkedInSearch` tool with a JSON payload
3. **Observe** the results
4. **Answer** with formatted profile information

---

## ✨ Features

- 🔍 **Person Search** — Find individuals by name, city, role, college, or company
- 🏢 **Company Search** — Discover company pages and key people
- 🤖 **AI Agent** — Uses LangChain ReAct pattern for intelligent query construction
- 📊 **Relevance Scoring** — Results filtered and ranked by Tavily relevance score
- 🧹 **Clean Middleware** — Filters low-confidence results (score < 0.3 removed)
- ⚡ **Streamlit UI** — Fast, interactive web interface

---

## 🛠️ Tech Stack

| Layer    | Technology                                         |
| -------- | -------------------------------------------------- |
| LLM      | Groq (Moonshot AI Kimi) (`langchain-groq`) |
| Agent    | LangChain ReAct Agent (`langchain-classic`)       |
| Search   | Tavily Search API                                  |
| Frontend | Streamlit                                          |
| Config   | python-dotenv                                      |

---

## 📁 Project Structure

```
linkedIn-Name-Search/
├── app.py              # Streamlit frontend
├── backend.py          # LangChain agent + Tavily search logic
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/linkedIn-Name-Search.git
cd linkedIn-Name-Search
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Copy `.env.example` to `.env` and fill in your keys:

```bash
cp .env.example .env
```

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

- Get **Groq API key** → [Groq Console](https://console.groq.com/)
- Get **Tavily API key** → [Tavily](https://tavily.com/) (free tier available)

### 5. Run the app

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🧪 Example Searches

| Search Type | Name         | Filters                        | Result                           |
| ----------- | ------------ | ------------------------------ | -------------------------------- |
| Person      | Sam Altman   | Role: CEO, City: San Francisco | LinkedIn profile with URL + bio  |
| Person      | Jensen Huang | Company: NVIDIA                | Top matched profiles & bio       |
| Company     | Tesla        | —                              | Company page + associated people |

---

## 🏗️ Architecture Details

### `Middleware` class

- **`filter_results()`** — Removes results with Tavily relevance score below 0.3
- **`format_profiles()`** — Normalizes raw Tavily results into structured profile dicts

### `LinkedInSearchAgent` class

- **`_search_profiles()`** — Accepts JSON input, builds a LinkedIn-optimized query, calls Tavily, runs middleware
- **`_create_agent()`** — Builds a LangChain ReAct agent with the Groq LLM and `LinkedInSearch` tool
- **`search()`** — Public method called by the Streamlit frontend

---

## 🔒 Privacy Note

This tool only fetches **publicly available** LinkedIn data that is already indexed by search engines. It does **not** bypass LinkedIn's authentication or scrape private profiles.

---

## 📌 Known Limitations

- Results depend on Tavily's search index and may not always include the latest LinkedIn changes
- Company search focuses on `linkedin.com/company` URLs; person search focuses on `linkedin.com/in/`
- Free Tavily API tier has monthly usage limits

---

## 👨‍💻 Author

**Raj Tejani**  
AI Engineer | Langchain | Automation | Voice Agents | FastAPI  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://in.linkedin.com/in/raj-tejani-5946252a4)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).
