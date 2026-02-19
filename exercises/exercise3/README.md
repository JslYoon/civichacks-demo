# Exercise 3: Build a Web Application

## 🎯 Learning Objectives

In this exercise, you'll learn:
- **How to build a web interface** for your AI project (no JavaScript required!)
- **How to use Gradio** to create production-quality UIs in ~40 lines of Python
- **How to make your project shareable** with a public URL
- **How to make interfaces judges will actually use** at hackathons

## 🤔 Why This Matters

Hackathon judges don't lean over your shoulder to watch terminal output. You need a **real, shareable interface**.

This exercise shows you how to turn your weekend project into something that looks and feels like a real product:
- **Polished chat interface** with message history
- **Track selection** to switch between datasets
- **Example questions** to guide users
- **Shareable URL** so anyone can try it

All in **~40 lines of Python**. No React. No JavaScript. No frontend experience needed.

## 📋 Prerequisites

### 1. Complete Exercises 1 & 2

You should already have:
- Ollama running with `llama3.1`
- Python dependencies installed (`pip install -r requirements.txt`)
- Civic data files in the `data/` directory

### 2. Understand What Gradio Is

**Gradio** is a Python library for building web UIs for machine learning.

Think of it as:
- The web framework designed for AI demos
- Used by thousands of projects on Hugging Face Spaces
- Free and open source (Apache 2.0 license)

You describe the UI in Python, and Gradio handles all the HTML/CSS/JavaScript for you.

## 🚀 Run the Exercise

All platforms (macOS / Linux / Windows):

```bash
cd exercises/exercise3
python web_app.py
```

### What Happens

1. The script starts a local web server on port 7860
2. Your browser opens automatically to `http://localhost:7860`
3. You see a **polished chat interface** with:
   - Track selector (switch between EcoHack, CityHack, EduHack, JusticeHack)
   - Dynamic header that updates when you change tracks
   - Example questions that change per track
   - Chat history
   - Cost comparison in each response

### Command Options

```bash
# Default (port 7860)
python web_app.py

# Custom port
python web_app.py --port 8080

# Get a public URL (shareable with anyone)
python web_app.py --share

# See all options
python web_app.py --help
```

## 📖 What You'll See

### The Interface

```
┌─────────────────────────────────────────────────────────┐
│         CivicHacks AI Assistant                         │
│         🏙️ CityHack — Boston 311 Services              │
│                                                          │
│  Track: [Dropdown: EcoHack, CityHack, EduHack, Justice] │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  💬 User: Which neighborhoods have the worst response   │
│           times?                                         │
│                                                          │
│  🤖 AI: Based on the data, Roxbury, Mattapan, and       │
│         Dorchester have the longest average 311 response│
│         times at 8.2, 7.9, and 7.3 days...              │
│         ⏱️ 18.4s · Local: $0.000013 · GPT-4o: $0.0021   │
│                                                          │
├─────────────────────────────────────────────────────────┤
│  Ask anything about the selected track's data...        │
│  [Text Input Field]                          [Ask]      │
│                                                          │
│  Example Questions (click to use):                      │
│  • Which neighborhoods have the longest response times? │
│  • What are the biggest service gaps?                   │
│  • What patterns suggest systemic inequity?             │
└─────────────────────────────────────────────────────────┘

Stack: Ollama + LlamaIndex + Gradio · Running on your-laptop
Privacy: All data processing happens locally
```

### Dynamic Features

**When you switch tracks:**
1. Header updates with new track name and description
2. Example questions change to match the track
3. Chat history clears (new dataset)
4. Index loads (first time per track, then cached)

**In each response:**
- Streaming text (watch it type)
- Timing info (how long it took)
- Cost comparison (local vs cloud)

## 💡 Understanding the Code

### The Minimal Example

Here's what a Gradio app looks like (simplified):

```python
import gradio as gr

# Define your function
def chat(message, history):
    # Your RAG logic here
    response = query_civic_data(message)
    history.append((message, response))
    return history

# Build the UI
with gr.Blocks() as app:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask anything...")
    btn = gr.Button("Ask")

    # Wire up the button
    btn.click(fn=chat, inputs=[msg, chatbot], outputs=[chatbot])

# Launch it
app.launch()
```

That's it! Browser opens, you have a chat interface.

### Key Components in This Exercise

#### 1. Track Selector
```python
track_selector = gr.Dropdown(
    choices=list(TRACKS.keys()),
    value=default_track,
    label="Choose a track"
)
```

#### 2. Dynamic Header
```python
def build_header_html(track_name):
    track = TRACKS[track_name]
    return f"""
    <div class="header">
        <h1>🏛️ CivicHacks AI Assistant</h1>
        <h2>{track_name}</h2>
        <p>{track['description']}</p>
    </div>
    """

header = gr.HTML(build_header_html(default_track))
```

#### 3. Example Questions
```python
examples = gr.Examples(
    examples=EXAMPLE_QUESTIONS[default_track],
    inputs=[question_input]
)
```

#### 4. Index Caching
```python
# Cache indices so switching tracks is instant
index_cache = {}

def build_index(track_name):
    if track_name in index_cache:
        return index_cache[track_name]

    # Build new index
    documents = SimpleDirectoryReader(input_files=[data_file]).load_data()
    index = VectorStoreIndex.from_documents(documents)
    index_cache[track_name] = index
    return index
```

## 🎮 Try It Yourself

### 1. Customize the Theme

In `web_app.py`, find the theme setup (around line 300):

```python
theme = gr.themes.Soft(
    primary_hue="red",      # Red Hat themed
    secondary_hue="slate"
)
```

Try different colors:
```python
theme = gr.themes.Soft(primary_hue="blue", secondary_hue="slate")  # Blue
theme = gr.themes.Soft(primary_hue="green", secondary_hue="slate")  # Green
theme = gr.themes.Soft(primary_hue="purple", secondary_hue="slate")  # Purple
```

Or try different themes:
```python
theme = gr.themes.Default()
theme = gr.themes.Glass()
theme = gr.themes.Monochrome()
```

### 2. Add Your Own Track

Edit the `TRACKS` dictionary (around line 50):

```python
TRACKS = {
    "🌿 EcoHack — Boston Environment": "ecohack_boston_environment.txt",
    "🏙️ CityHack — Boston 311": "cityhack_boston_311.txt",
    "📚 EduHack — Boston Schools": "eduhack_boston_schools.txt",
    "⚖️ JusticeHack — MA Criminal Justice": "justicehack_ma_justice.txt",
    # Add your own:
    "🏥 HealthHack — Local Hospitals": "healthhack_hospitals.txt",
}
```

And add example questions (around line 60):

```python
EXAMPLE_QUESTIONS = {
    # ... existing tracks ...
    "🏥 HealthHack — Local Hospitals": [
        "What are the average ER wait times?",
        "Which hospitals have the best outcomes?",
        "What health disparities exist?"
    ],
}
```

### 3. Make It Public

```bash
# Get a temporary public URL (lasts ~72 hours)
python web_app.py --share
```

Gradio creates a URL like `https://abc123.gradio.live` that anyone can access. Perfect for:
- Showing judges your project
- Demoing to remote teammates
- Getting feedback from users

### 4. Deploy for Free

**Option A: Hugging Face Spaces**
1. Create account at [huggingface.co](https://huggingface.co)
2. Create a new Space (select "Gradio" SDK)
3. Upload your code
4. **Note:** You'll need to swap Ollama for a cloud-hosted model (Ollama runs locally)

**Option B: Keep it Local**
Just run `python web_app.py` whenever you want to demo. No deployment needed!

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Browser doesn't open | Manually go to `http://localhost:7860` |
| Port already in use | Use `--port 8080` to change ports |
| Slow first load per track | Normal — building index. Cached after first use |
| Need specific browser | See below for environment variable setup |

**Set specific browser:**

macOS/Linux:
```bash
BROWSER=chrome python web_app.py
```

Windows CMD:
```bash
set BROWSER=chrome
python web_app.py
```

Windows PowerShell:
```bash
$env:BROWSER="chrome"
python web_app.py
```

## 🎯 UI Features to Notice

### Dynamic Updates
- **Header** changes when you switch tracks
- **Example questions** update to match the selected dataset
- **Chat clears** when you switch tracks (new context)

### Cost Transparency
Every response shows:
```
⏱️ 18.4s · Local: $0.000013 · GPT-4o: $0.0021
```

This educates users about the economics of local vs. cloud AI.

### Red Hat Theming
- Primary color: Red (`#CC0000`)
- Clean, professional layout
- Avatar icon in chat
- Footer with stack info

## ✅ What You Learned

After completing this exercise, you now know:
- ✅ How to build web UIs with Gradio in ~40 lines of Python
- ✅ How to create dynamic interfaces that update based on user input
- ✅ How to cache indices for instant switching between datasets
- ✅ How to make your hackathon project shareable with `--share`
- ✅ How to deploy AI applications without writing JavaScript

## ➡️ Next Steps

**Ready for Exercise 4?**

You've learned the building blocks. Now it's time to **build something your own**.

👉 Go to `exercises/exercise4/` for the **final challenge** — a do-it-yourself project where you apply everything you've learned.

---

**Questions?** Check the main [README.md](../../README.md) or ask a mentor!
