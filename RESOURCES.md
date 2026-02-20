# CivicHacks 2026 — Resource Cheat Sheet

**Quick-reference for hackathon builders.** Every tool listed here is free and open source (or has a generous free tier). Bookmark this page and come back to it throughout the weekend.

> **New to AI?** Start with the [Quick Start in the README](README.md#quick-start--get-this-running-on-your-laptop) — you'll have a working civic AI app in 10 minutes. Then use this sheet to level up your project.

---

## Table of Contents

1. [Your Starting Stack (What We Demoed)](#your-starting-stack-what-we-demoed)
2. [Local LLMs & Model Runtimes](#local-llms--model-runtimes)
3. [Models to Try](#models-to-try)
4. [RAG Frameworks (Connect AI to Your Data)](#rag-frameworks-connect-ai-to-your-data)
5. [Web UI Frameworks (Build a Demo Fast)](#web-ui-frameworks-build-a-demo-fast)
6. [Vector Databases (For Larger Datasets)](#vector-databases-for-larger-datasets)
7. [Agent Frameworks (Multi-Step AI)](#agent-frameworks-multi-step-ai)
8. [Civic & Open Data Sources](#civic--open-data-sources)
9. [Free Deployment & Hosting](#free-deployment--hosting)
10. [Useful Python Libraries](#useful-python-libraries)
11. [Learning Resources](#learning-resources)
12. [Hackathon Tips](#hackathon-tips)

---

## Your Starting Stack (What We Demoed)

This is the exact stack from the live demo. It's a great starting point — you can build a complete hackathon project without adding anything else.

| Tool | What It Does | URL |
|------|-------------|-----|
| **Ollama** | Run LLMs locally with one command | [ollama.com](https://ollama.com) |
| **Llama 3.1 8B** | Open source LLM (Meta), GPT-4-class quality | `ollama pull llama3.1` |
| **LlamaIndex** | RAG framework — connect AI to your data | [docs.llamaindex.ai](https://docs.llamaindex.ai) |
| **Gradio** | Build web UIs for ML apps in Python | [gradio.app](https://gradio.app) |
| **HuggingFace Embeddings** | Local text embeddings (all-MiniLM-L6-v2) | [huggingface.co](https://huggingface.co) |

**Total cost:** Fractions of a cent in electricity per query. No API keys, no cloud bills, no data leaving your machine.

---

## Local LLMs & Model Runtimes

Run AI models on your own laptop — no internet, no API keys, no cost.

| Tool | Best For | URL |
|------|---------|-----|
| **Ollama** | Easiest setup, great CLI, wide model support | [ollama.com](https://ollama.com) |
| **LM Studio** | GUI-based, good for beginners who prefer a visual interface | [lmstudio.ai](https://lmstudio.ai) |
| **llamafile** | Single-file executables — download one file, run a model | [github.com/Mozilla-Ocho/llamafile](https://github.com/Mozilla-Ocho/llamafile) |
| **vLLM** | High-throughput serving, great for team/server deployments | [docs.vllm.ai](https://docs.vllm.ai) |
| **Jan** | Desktop app for local AI, beginner-friendly | [jan.ai](https://jan.ai) |

---

## Models to Try

All available via `ollama pull <model>`. Experiment with different models to find the best fit for your project.

| Model | Size | Best For | Command |
|-------|------|---------|---------|
| **Llama 3.1 8B** | 4.7 GB | General purpose (our demo default) | `ollama pull llama3.1` |
| **Llama 3.2 3B** | 2.0 GB | Fast responses, lower RAM | `ollama pull llama3.2:3b` |
| **Mistral 7B** | 4.1 GB | Strong general quality, Apache 2.0 license | `ollama pull mistral` |
| **Phi-3 Mini** | 2.2 GB | Smallest model that's still useful | `ollama pull phi3:mini` |
| **DeepSeek-R1 7B** | 4.7 GB | Reasoning and analysis tasks | `ollama pull deepseek-r1:7b` |
| **Qwen 2.5 7B** | 4.7 GB | Strong multilingual support | `ollama pull qwen2.5` |
| **Gemma 2 9B** | 5.4 GB | Google's open model, great quality | `ollama pull gemma2` |
| **CodeLlama 7B** | 3.8 GB | Code generation and analysis | `ollama pull codellama` |

> **Tip:** Start with Llama 3.1 (what we demoed). If your laptop is slow or has less than 8 GB RAM, try Llama 3.2:3b or Phi-3 Mini.

---

## RAG Frameworks (Connect AI to Your Data)

RAG (Retrieval Augmented Generation) is the technique we used in the demo — the AI retrieves relevant data **before** answering, so it cites real facts instead of hallucinating.

| Framework | Best For | URL |
|-----------|---------|-----|
| **LlamaIndex** | Easiest RAG setup, great docs, what we used | [docs.llamaindex.ai](https://docs.llamaindex.ai) |
| **LangChain** | Most popular, huge ecosystem, lots of integrations | [langchain.com](https://langchain.com) |
| **Haystack** | Search-focused RAG, great for document Q&A | [haystack.deepset.ai](https://haystack.deepset.ai) |
| **DSPy** | Programmatic prompting, academic-grade optimization | [dspy.ai](https://dspy.ai) |
| **RAGFlow** | Visual RAG pipeline builder with built-in UI | [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow) |

> **Our recommendation:** Stick with **LlamaIndex** for this hackathon — it's what the demo uses, so you can build on top of the existing code without starting from scratch.

---

## Web UI Frameworks (Build a Demo Fast)

Judges want to see a working demo. These frameworks let you build a polished web interface in Python — no JavaScript needed.

| Framework | Best For | URL |
|-----------|---------|-----|
| **Gradio** | Chat interfaces, ML demos (what we used) | [gradio.app](https://gradio.app) |
| **Streamlit** | Data dashboards, multi-page apps | [streamlit.io](https://streamlit.io) |
| **Chainlit** | Chat-focused apps with auth and history | [chainlit.io](https://chainlit.io) |
| **Panel** | Complex data dashboards and visualizations | [panel.holoviz.org](https://panel.holoviz.org) |
| **Mesop** | Google's new Python web UI framework | [google.github.io/mesop](https://google.github.io/mesop) |
| **NiceGUI** | Full web apps with more UI control | [nicegui.io](https://nicegui.io) |

> **Our recommendation:** Use **Gradio** if you're building a chat/Q&A interface (fork our Step 3 or Step 5 code). Use **Streamlit** if you're building a data exploration dashboard.

---

## Vector Databases (For Larger Datasets)

The demo uses LlamaIndex's in-memory vector store, which works great for small-to-medium datasets. If your project needs persistent storage or handles larger data, consider a dedicated vector database.

| Database | Best For | URL |
|----------|---------|-----|
| **ChromaDB** | Simplest to set up, in-memory or persistent, great for hackathons | [trychroma.com](https://www.trychroma.com) |
| **Faiss** | Fastest local search, Facebook/Meta, pure performance | [github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss) |
| **Weaviate** | Full-featured, hybrid search, great API | [weaviate.io](https://weaviate.io) |
| **Qdrant** | Rust-based, fast, good filtering support | [qdrant.tech](https://qdrant.tech) |
| **Milvus** | Enterprise-grade, handles billions of vectors | [milvus.io](https://milvus.io) |

> **For this hackathon:** You probably don't need a separate vector database. The in-memory store in LlamaIndex handles thousands of documents just fine. Consider ChromaDB only if you need data to persist between app restarts.

---

## Agent Frameworks (Multi-Step AI)

Want your AI to do more than answer questions? Agent frameworks let AI plan and execute multi-step tasks — like researching a topic, analyzing data, and generating a report.

| Framework | Best For | URL |
|-----------|---------|-----|
| **CrewAI** | Multi-agent teams with roles and tasks | [crewai.com](https://crewai.com) |
| **AutoGen** | Microsoft's multi-agent conversation framework | [github.com/microsoft/autogen](https://github.com/microsoft/autogen) |
| **Agno** | Lightweight, fast agent framework | [agno.com](https://agno.com) |
| **Smolagents** | HuggingFace's simple agent library | [huggingface.co/docs/smolagents](https://huggingface.co/docs/smolagents) |
| **Semantic Kernel** | Microsoft, works with Python and .NET | [learn.microsoft.com/semantic-kernel](https://learn.microsoft.com/en-us/semantic-kernel/) |
| **LangGraph** | LangChain's graph-based agent orchestration | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/) |

> **Caution:** Agents are powerful but can be unpredictable. For a hackathon demo, a well-tuned RAG pipeline (like our demo) is often more reliable and impressive than a brittle agent chain. Add agents only if your use case truly needs multi-step reasoning.

---

## Civic & Open Data Sources

Real data for real civic projects. These are the same portals that city planners, journalists, and policy researchers use.

### Boston & Massachusetts

| Source | URL | What You'll Find |
|--------|-----|-----------------|
| **Analyze Boston** | [data.boston.gov](https://data.boston.gov) | 311 requests, permits, crime, property, schools, transportation |
| **MA Open Data** | [mass.gov/open-data](https://mass.gov/open-data) | State-level health, education, criminal justice, environment |
| **MBTA Open Data** | [mbta.com/developers](https://www.mbta.com/developers) | Real-time transit data, schedules, ridership |
| **MA Trial Court** | [mass.gov/orgs/trial-court](https://www.mass.gov/orgs/trial-court) | Court statistics and case data |

### National

| Source | URL | What You'll Find |
|--------|-----|-----------------|
| **Data.gov** | [data.gov](https://data.gov) | 300,000+ federal datasets across all agencies |
| **Census Bureau** | [data.census.gov](https://data.census.gov) | Demographics, income, housing, population by geography |
| **CDC Data** | [data.cdc.gov](https://data.cdc.gov) | Public health data, environmental health |
| **EPA Data** | [epa.gov/data](https://www.epa.gov/data) | Environmental quality, pollution, climate |
| **FBI Crime Data** | [crime-data-explorer.fr.cloud.gov](https://crime-data-explorer.fr.cloud.gov) | National crime statistics |

### Civic Tech Community

| Source | URL | What You'll Find |
|--------|-----|-----------------|
| **Code for America** | [codeforamerica.org](https://codeforamerica.org) | Civic tech projects, open source tools |
| **Civic Commons** | [commons.codeforamerica.org](https://commons.codeforamerica.org) | Reusable civic tech applications |
| **Open Data Network** | [opendatanetwork.com](https://www.opendatanetwork.com) | Search across thousands of open data portals |
| **awesome-civic-tech** | [github.com/codeforamerica/awesome-civic](https://github.com/codeforamerica/civic-tech-patterns) | Curated list of civic tech resources |

---

## Free Deployment & Hosting

Ship your project so judges (and the world) can use it. All of these have free tiers that are more than enough for a hackathon.

| Platform | Best For | Free Tier | URL |
|----------|---------|-----------|-----|
| **Hugging Face Spaces** | Gradio/Streamlit apps | Unlimited public spaces | [huggingface.co/spaces](https://huggingface.co/spaces) |
| **Streamlit Cloud** | Streamlit apps with GitHub integration | 1 free app | [streamlit.io/cloud](https://streamlit.io/cloud) |
| **Render** | Web services, APIs, databases | 750 hours/month | [render.com](https://render.com) |
| **Railway** | Full-stack deployments | $5 credit/month | [railway.app](https://railway.app) |
| **Vercel** | Frontends, serverless functions | Generous free tier | [vercel.com](https://vercel.com) |
| **GitHub Pages** | Static sites, documentation | Unlimited | [pages.github.com](https://pages.github.com) |
| **Replit** | Full dev environment + deployment | Free tier available | [replit.com](https://replit.com) |

> **Note:** Our demo runs Ollama **locally**, which won't work on most cloud platforms. For deployment, you'll need to swap the local LLM for a cloud API (HuggingFace Inference, Groq, Together AI) or use a platform that supports custom containers.

---

## Useful Python Libraries

These are the most common libraries you'll want to `pip install` during the hackathon, organized by what you're trying to do.

### Data Analysis & Visualization

| Library | What It Does | Install |
|---------|-------------|---------|
| **pandas** | Data manipulation and analysis | `pip install pandas` |
| **matplotlib** | Static charts and graphs | `pip install matplotlib` |
| **plotly** | Interactive charts and dashboards | `pip install plotly` |
| **seaborn** | Statistical visualizations | `pip install seaborn` |
| **altair** | Declarative visualization (works great with Streamlit) | `pip install altair` |

### File Parsing

| Library | What It Does | Install |
|---------|-------------|---------|
| **pypdf** | Read and extract text from PDFs | `pip install pypdf` |
| **python-docx** | Read and write Word documents | `pip install python-docx` |
| **openpyxl** | Read and write Excel files | `pip install openpyxl` |
| **beautifulsoup4** | Parse HTML and scrape web pages | `pip install beautifulsoup4` |

### APIs & Web

| Library | What It Does | Install |
|---------|-------------|---------|
| **requests** | Make HTTP requests (API calls, web scraping) | `pip install requests` |
| **fastapi** | Build REST APIs quickly | `pip install fastapi uvicorn` |
| **pydantic** | Data validation and settings management | `pip install pydantic` |
| **httpx** | Modern async HTTP client | `pip install httpx` |

### AI & ML

| Library | What It Does | Install |
|---------|-------------|---------|
| **transformers** | HuggingFace model library | `pip install transformers` |
| **sentence-transformers** | Embeddings and semantic search | `pip install sentence-transformers` |
| **scikit-learn** | Traditional ML algorithms | `pip install scikit-learn` |
| **openai** | OpenAI API client (also works with compatible APIs) | `pip install openai` |

---

## Learning Resources

Get up to speed quickly with these resources. Prioritize the ones marked with a star — they're the most immediately useful for this hackathon.

### RAG & LLM Applications

| Resource | URL |
|----------|-----|
| ⭐ **LlamaIndex Starter Tutorial** | [docs.llamaindex.ai/en/stable/getting_started](https://docs.llamaindex.ai/en/stable/getting_started/) |
| ⭐ **Ollama Model Library** | [ollama.com/library](https://ollama.com/library) |
| **LangChain Tutorials** | [python.langchain.com/docs/tutorials](https://python.langchain.com/docs/tutorials/) |
| **HuggingFace NLP Course** | [huggingface.co/learn/nlp-course](https://huggingface.co/learn/nlp-course) |
| **RAG from Scratch (YouTube)** | Search "RAG from scratch LangChain" on YouTube |

### Model Benchmarks & Comparisons

| Resource | URL |
|----------|-----|
| ⭐ **Artificial Analysis** | [artificialanalysis.ai](https://artificialanalysis.ai) |
| **Open LLM Leaderboard** | [huggingface.co/spaces/open-llm-leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) |
| **LMSYS Chatbot Arena** | [lmarena.ai](https://lmarena.ai) |

### Curated Lists

| Resource | URL |
|----------|-----|
| **awesome-langchain** | [github.com/kyrolabs/awesome-langchain](https://github.com/kyrolabs/awesome-langchain) |
| **awesome-llm-agents** | [github.com/kaushikb11/awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) |
| **AI Templates (Red Hat)** | [aitemplates.io](https://aitemplates.io) |

---

## Hackathon Tips

Advice from people who've built (and judged) a lot of hackathon projects.

### Strategy

- **Start with the demo code.** Fork this repo and modify it — don't start from scratch. You'll have a working app in 10 minutes instead of spending 3 hours on setup.
- **Pick one track, go deep.** A focused project that solves one problem well beats a scattered project that barely works.
- **Demo > Features.** Judges spend 3-5 minutes with your project. One polished feature that works flawlessly is worth more than ten half-finished ones.
- **Tell a story.** Open with the problem, show the data, demo the solution. The best projects make you *feel* the impact.

### Technical

- **Use the `--all` flag** (Step 4/5) to load multiple data files into one index. This lets you do cross-file analysis — "compare the environmental data with the school data" — which is very impressive in demos.
- **Show the cost comparison.** Every query in our demo shows local cost vs. cloud cost. This makes the open source story concrete and memorable.
- **Keep your model small.** Llama 3.2:3b runs 3x faster than Llama 3.1 8B and is "good enough" for most demos. Speed matters more than quality in a live presentation.
- **Pre-load everything.** Run every command once before your demo. The first run downloads models and caches embeddings — you don't want to wait 2 minutes on stage.
- **Git commit early and often.** Losing code at 2am because you forgot to save is the most preventable hackathon disaster.

### Presentation

- **Have a backup.** Take a screenshot or screen recording of your app working. If something breaks during the demo, show the recording.
- **Make the text BIG.** Judges and audiences can't read 12pt font on a projector. Use `Cmd+Plus` in your terminal and browser.
- **Name your project.** "Our CityHack AI assistant" is more memorable than "our demo_step3 modification."

---

## Quick Reference: The Full Demo Stack

```
┌─────────────────────────────────────────────┐
│              Gradio Web UI                  │  ← pip install gradio
│              (Steps 3 & 5)                  │
├─────────────────────────────────────────────┤
│          LlamaIndex RAG Pipeline            │  ← pip install llama-index
│   ┌──────────────┐    ┌──────────────────┐  │
│   │ Vector Index  │    │ HuggingFace      │  │
│   │ (in-memory)   │    │ Embeddings       │  │
│   └──────────────┘    └──────────────────┘  │
├─────────────────────────────────────────────┤
│         Ollama + Llama 3.1                  │  ← ollama pull llama3.1
│         (local LLM inference)               │
├─────────────────────────────────────────────┤
│         Your Data (data/ or userdata/)      │  ← .txt .pdf .csv .docx
└─────────────────────────────────────────────┘
```

**GitHub:** [github.com/holzerjm/civichacks-demo](https://github.com/holzerjm/civichacks-demo) · **License:** Apache 2.0

---

*Built for CivicHacks 2026 at Boston University. Go build something that matters.*
