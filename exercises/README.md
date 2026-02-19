# CivicHacks 2026 — Learning Exercises

**[← Back to Main README](../README.md)**

---

## Overview

This directory contains **four progressive exercises** that teach you how to build civic AI applications from scratch.

**Total workshop time:** 90 minutes

---

## Learning Path

**Exercise 1: Run AI Locally** (15 minutes)
- Learn how to run GPT-class models on your laptop
- Understand tokens, streaming, and cost comparisons
- [Start Exercise 1 →](exercise1/README.md)

**Exercise 2: Connect AI to Civic Data** (30 minutes)
- Learn what RAG (Retrieval Augmented Generation) is
- Connect AI to real civic datasets
- Make AI cite facts instead of guessing
- [Start Exercise 2 →](exercise2/README.md)

**Exercise 3: Build a Web Application** (30 minutes)
- Create shareable interfaces with Gradio
- Build dynamic UIs without JavaScript
- Deploy applications with public URLs
- [Start Exercise 3 →](exercise3/README.md)

**Exercise 4: Apply Your Skills** (20 minutes)
- Quick creative challenge using real civic data
- Use the provided `template.py` to get started fast
- Pick a track and complete a specific task
- Practice for your hackathon project
- [Start Exercise 4 →](exercise4/README.md)

---

## Prerequisites

### Install Ollama

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download the installer from [ollama.com](https://ollama.com)

### Download the AI model

```bash
ollama pull llama3.1
```

This downloads approximately 4.7 GB. Do this before the workshop on reliable wifi.

### Install Python dependencies

```bash
# From the project root
pip install -r requirements.txt
```

---

## Quick Start

```bash
cd exercise1
cat README.md
python local_ai.py
```

---

## Directory Structure

```
exercises/
├── README.md              ← You are here
├── exercise1/
│   ├── README.md
│   └── local_ai.py
├── exercise2/
│   ├── README.md
│   └── civic_rag.py
├── exercise3/
│   ├── README.md
│   └── web_app.py
├── exercise4/
│   ├── README.md
│   └── template.py        ← Ready-to-use template
└── shared/
    └── cost_estimator.py
```

---

## Learning Outcomes

After completing all four exercises, you will be able to:

- Run powerful AI models locally on any laptop
- Connect AI to real data using RAG
- Build shareable web applications with Gradio
- Deploy civic tech projects that run 100% offline
- Understand the economics of local vs. cloud AI

---

## Getting Help

- Check individual exercise README files for detailed instructions
- Review the [main README](../README.md) for additional resources
- Consult the [User Guide](../USER_GUIDE.md) for troubleshooting
- Ask mentors or teammates

---

**Ready to start?** [Begin with Exercise 1 →](exercise1/README.md)
