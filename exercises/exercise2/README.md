# Exercise 2: Connect AI to Civic Data (RAG)

## 🎯 Learning Objectives

In this exercise, you'll learn:
- **What RAG (Retrieval Augmented Generation) is** and why it's crucial for real applications
- **How to connect AI to documents** so it can cite real facts, not make things up
- **How to build a searchable knowledge base** from civic data files
- **Why embeddings matter** for finding relevant information

## 🤔 Why This Matters

Generic AI models don't know about YOUR community. They might know general facts about cities, but they can't tell you:
- Which neighborhoods in YOUR city have the worst 311 response times
- What YOUR local school district's achievement gaps look like
- Where environmental hazards exist in YOUR community

**RAG solves this** by letting AI search through real documents before answering. Instead of guessing, the AI:
1. Searches your civic data for relevant facts
2. Reads the most relevant sections
3. Cites specific statistics and findings

This is how you build civic tech that's actually trustworthy.

## 📋 Prerequisites

### 1. Complete Exercise 1

You should already have:
- Ollama installed and running
- The `llama3.1` model downloaded

### 2. Install Python Dependencies

```bash
# From the project root:
pip install -r requirements.txt
```

This installs:
- **llama-index** — RAG framework
- **llama-index-llms-ollama** — Connects LlamaIndex to Ollama
- **llama-index-embeddings-huggingface** — Local embedding model (no API needed!)

### 3. Check the Civic Data Files

Look in the `data/` directory. You'll find four real civic datasets:

| Track | File | What It Contains |
|-------|------|------------------|
| **EcoHack** | `ecohack_boston_environment.txt` | Air quality, heat islands, climate data |
| **CityHack** | `cityhack_boston_311.txt` | 311 service requests, response times |
| **EduHack** | `eduhack_boston_schools.txt` | Achievement gaps, absenteeism, tech access |
| **JusticeHack** | `justicehack_ma_justice.txt` | Incarceration, policing, recidivism data |

These are **synthetic but realistic** — based on real patterns, fabricated for the demo.

## 🚀 Run the Exercise

All platforms (macOS / Linux / Windows):

```bash
cd exercises/exercise2
python civic_rag.py city
```

### Command Options

```bash
# Random question from the city track
python civic_rag.py city

# Specific question number (1-3)
python civic_rag.py city 2

# All three questions for a track
python civic_rag.py eco --all

# Try different tracks
python civic_rag.py eco      # Environment
python civic_rag.py edu      # Education
python civic_rag.py justice  # Criminal justice
```

## 📖 What You'll See

### First Run (Building the Index)

```
🏛️  CivicHacks 2026 — Connecting AI to Civic Data

📂 Track: 🏙️ CityHack
📄 Data: cityhack_boston_311.txt

────────────────────────────────────────────────────────────

📥 Loading civic data...
✓ Loaded 1,247 text chunks from data file

🔍 Building vector search index...
   (This takes ~10 seconds on first run — downloads embedding model)
✓ Index ready

────────────────────────────────────────────────────────────

💬 Query: Which neighborhoods have the longest 311 response
times and what are the equity implications?

────────────────────────────────────────────────────────────

🤖 Response:

Based on the data, **Roxbury, Mattapan, and Dorchester** have
the longest average 311 response times at 8.2, 7.9, and 7.3 days
respectively, compared to 3.1 days in Back Bay and 2.8 days in
Beacon Hill.

The equity implications are significant:

• These neighborhoods are predominantly Black and Latino
  communities with median incomes 60% lower than high-service
  areas

• Residents in these areas are 2.8x more likely to experience
  service delays...

────────────────────────────────────────────────────────────
⏱️  18.4s · 187 tokens · 10 tok/s
⚡ Local: $0.000013 · GPT-4o: $0.0021 (161x more expensive)
────────────────────────────────────────────────────────────
```

Notice how the AI **cites specific neighborhoods and numbers**! It's not guessing — it's reading the data.

## 💡 Understanding RAG

### What Happens Under the Hood

```python
# 1. Configure the AI and embedding model
Settings.llm = Ollama(model="llama3.1")
Settings.embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")

# 2. Load your civic data
documents = SimpleDirectoryReader(input_files=[data_file]).load_data()

# 3. Build a searchable index
index = VectorStoreIndex.from_documents(documents)

# 4. Create a query engine
query_engine = index.as_query_engine(streaming=True, similarity_top_k=3)

# 5. Ask questions!
response = query_engine.query("Which neighborhoods have the longest response times?")
```

That's it! About 15 lines of code to connect AI to real data.

### The RAG Process

When you ask a question, here's what happens:

```
You: "Which neighborhoods have the worst 311 response times?"
  ↓
[Embedding Model converts question to numbers (vector)]
  ↓
[Vector Index finds the 3 most relevant chunks from the data]
  ↓
[AI reads those chunks + your question]
  ↓
AI: "Based on the data, Roxbury (8.2 days), Mattapan (7.9 days)..."
```

### What Are Embeddings?

**Embeddings** are how computers understand meaning:
- Each chunk of text becomes a list of numbers (a "vector")
- Similar concepts have similar vectors
- When you ask about "response times," the system finds chunks with similar meaning

The **HuggingFace embedding model** (`all-MiniLM-L6-v2`):
- Runs locally on your CPU (no API needed)
- Downloads once (~80 MB), then cached forever
- Fast and accurate enough for most use cases

## 🎮 Try It Yourself

### 1. Ask Your Own Questions

Edit `civic_rag.py` and add your own questions to the TRACKS dictionary (around line 60):

```python
TRACKS = {
    "city": {
        "name": "🏙️ CityHack",
        "file": "cityhack_boston_311.txt",
        "queries": [
            "Which neighborhoods have the longest 311 response times?",
            # Add your own question here:
            "What types of complaints are most common?",
        ],
    },
}
```

### 2. Use Your Own Data

Replace a file in the `data/` directory with your own `.txt` file:

```bash
# Add your own civic data
cp ~/my-city-data.txt data/my_data.txt

# Update civic_rag.py to point to it
"file": "my_data.txt"
```

RAG works with:
- `.txt` files (easiest)
- `.pdf` files (install `llama-index-readers-file`)
- `.csv` files (built-in support)
- `.docx` files (built-in support)

### 3. Adjust How Many Chunks It Reads

In `civic_rag.py`, find this line (around line 196):

```python
query_engine = index.as_query_engine(streaming=True, similarity_top_k=3)
```

Change `similarity_top_k`:
- `similarity_top_k=1` — Faster, but might miss context
- `similarity_top_k=5` — Slower, but more comprehensive

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Embedding model downloading..." | Normal on first run — ~80 MB download, then cached |
| Slow index building | First run is slower. Subsequent runs reuse the model |
| AI makes up facts not in data | Increase `similarity_top_k` to give it more context |
| "File not found" | Make sure you're running from `exercises/exercise2/` |

## 🎯 Sample Questions Per Track

### EcoHack
```bash
python civic_rag.py eco
```
- "Which Boston neighborhoods have the worst air quality and why?"
- "What are the biggest environmental justice concerns?"
- "How is climate change threatening Boston's coastline?"

### CityHack
```bash
python civic_rag.py city
```
- "Which neighborhoods have the longest 311 response times?"
- "What are the biggest service gaps for non-English speakers?"
- "What patterns suggest systemic inequity in city services?"

### EduHack
```bash
python civic_rag.py edu
```
- "What are the most significant achievement gaps in Boston schools?"
- "How does transportation affect student attendance?"
- "What technology access barriers exist?"

### JusticeHack
```bash
python civic_rag.py justice
```
- "What racial disparities exist in pretrial detention in Massachusetts?"
- "How effective are reentry programs at reducing recidivism?"
- "What does the data reveal about policing patterns in Boston?"

## ✅ What You Learned

After completing this exercise, you now know:
- ✅ What RAG is and why it's essential for real applications
- ✅ How to connect AI to documents using LlamaIndex
- ✅ What embeddings are and how they enable semantic search
- ✅ How to make AI cite real facts instead of making things up

## ➡️ Next Steps

**Ready for Exercise 3?**

Now that you can query civic data from the terminal, let's make it shareable by building a real web application.

👉 Go to `exercises/exercise3/` to learn how to **build a web interface** that anyone can use.

---

**Questions?** Check the main [README.md](../../README.md) or ask a mentor!
