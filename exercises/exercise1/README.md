# Exercise 1: Run AI Locally on Your Laptop

## 🎯 Learning Objectives

In this exercise, you'll learn:
- **How to run powerful AI models on your own computer** — no cloud, no API key required
- **Why local AI matters** for privacy, cost, and accessibility
- **How to interact with AI using Python** in just a few lines of code
- **What tokens are** and how AI generates responses

## 🤔 Why This Matters

Open source AI changes everything because it means you can:
- **Build for free** — No paying $0.03 per request to cloud APIs
- **Keep data private** — Nothing leaves your laptop
- **Work offline** — Perfect for hackathons with spotty wifi
- **Deploy anywhere** — From Raspberry Pi to cloud servers

This is the foundation for civic tech that's truly accessible to everyone, not just well-funded organizations.

## 📋 Prerequisites

Before starting this exercise:

### 1. Install Ollama

Ollama lets you run large language models locally with simple commands.

**macOS:**
```bash
brew install ollama
# OR download from https://ollama.com
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download the installer from [ollama.com](https://ollama.com)

### 2. Download the AI Model

```bash
# This downloads ~4.7 GB (do this before the hackathon!)
ollama pull llama3.1
```

**What is Llama 3.1?**
- 8 billion parameter model (similar capability to GPT-3.5)
- Built by Meta and released as open source
- Runs on most modern laptops

### 3. Verify It Works

```bash
ollama run llama3.1 "Say hello in 10 words or less"
```

You should see the AI respond! If Ollama isn't running, start it with:
```bash
ollama serve
```

## 🚀 Run the Exercise

All platforms (macOS / Linux / Windows):

```bash
cd exercises/exercise1
python local_ai.py
```

## 📖 What You'll See

The script will:
1. Connect to your local Ollama instance
2. Send a civic-themed prompt asking about open source AI
3. **Stream the response token by token** (you'll watch it think!)
4. Show you:
   - How long it took
   - Tokens per second (speed)
   - **Cost comparison**: Local electricity (~$0.0001) vs. cloud API (~$0.002)

### Sample Output

```
🏛️  CivicHacks 2026 — Open Source AI, Running Locally

📡 Model: llama3.1 (8B) — running on your-laptop
🕐 Time: February 21, 2026 at 10:15:23 AM
🔒 Data: never leaves your-laptop

────────────────────────────────────────────────────────────

💬 Prompt: You are a civic technology advisor. In 3 concise
bullet points, explain why open source AI matters for building
tools that serve communities...

────────────────────────────────────────────────────────────

🤖 Response:

Here are three reasons why open source AI matters:

• **Accessibility**: Open source AI models run locally, meaning
  civic organizations don't need expensive API subscriptions...

• **Privacy**: When you process sensitive community data, keeping
  it local means it never leaves your infrastructure...

• **Customization**: Open source models can be fine-tuned on
  your specific use case...

────────────────────────────────────────────────────────────
⏱️  12.3s · 142 tokens · 11 tok/s
⚡ Local: $0.000009 (0.051 Wh @ 15W) · GPT-4o: $0.0017 (189x more)
────────────────────────────────────────────────────────────

✅ That's it. Local AI. Private. And virtually free.
```

## 💡 Understanding What Happened

### The Code (Simplified)

Here's what the script does under the hood:

```python
import ollama

# Connect to your local Ollama instance
stream = ollama.chat(
    model="llama3.1",
    messages=[{"role": "user", "content": "Your prompt here"}],
    stream=True  # Stream tokens as they're generated
)

# Print each token as it arrives
for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
```

That's it! You just ran a GPT-class AI model on your laptop.

### What Are "Tokens"?

Tokens are chunks of text the AI processes. Roughly:
- 1 token ≈ 0.75 words in English
- "Hello world" = ~2 tokens
- This sentence = ~8-10 tokens

The model reads tokens (your prompt) and generates new tokens (the response) one at a time. That's why you see it "thinking" as it types.

## 🎮 Try It Yourself

Once you've run the default exercise, try customizing it:

### 1. Edit the Prompt

Open `local_ai.py` and find this section (around line 27):

```python
PROMPT = """You are a civic technology advisor. In 3 concise bullet points,
explain why open source AI matters for building tools that serve
communities — especially for students at a hackathon who want to
make a real impact this weekend."""
```

Change it to ask about your hackathon track:
- "How can AI help solve environmental justice issues?"
- "What are the biggest challenges in civic tech right now?"
- "Explain how AI can improve government services in 2 sentences"

### 2. Try a Different Model

Want something faster? Smaller models run quicker on limited hardware:

```bash
# Download a smaller model (3B parameters, very fast)
ollama pull llama3.2:3b

# In local_ai.py, change line 74:
stream = ollama.chat(model="llama3.2:3b", ...)
```

Want better quality? Larger models are smarter:

```bash
# Download a larger model (needs ~16GB RAM)
ollama pull llama3.1:70b

# In local_ai.py:
stream = ollama.chat(model="llama3.1:70b", ...)
```

### 3. Check the Help Menu

```bash
python local_ai.py --help
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Connection refused" | Run `ollama serve` to start Ollama |
| "Model not found" | Run `ollama pull llama3.1` |
| Very slow (< 1 token/sec) | Normal on older CPUs — try `llama3.2:3b` for speed |
| Script errors | Make sure you're in the `exercises/exercise1/` directory |

## ✅ What You Learned

After completing this exercise, you now know:
- ✅ How to run AI models locally using Ollama
- ✅ The cost difference between local AI (fractions of a penny) and cloud APIs (dollars)
- ✅ What tokens are and how AI generates responses
- ✅ How to customize prompts for your use case

## ➡️ Next Steps

**Ready for Exercise 2?**

Now that you can run AI locally, let's make it actually useful by connecting it to real civic data.

👉 Go to `exercises/exercise2/` to learn about **RAG (Retrieval Augmented Generation)** — teaching AI to answer questions about YOUR city's data.

---

**Questions?** Check the main [README.md](../../README.md) or ask a mentor!
