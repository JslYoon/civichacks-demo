"""
Exercise 4 Template — Apply Your Skills

INSTRUCTIONS:
1. Copy this file: cp template.py my_civic_tool.py
2. Choose your track below (uncomment one)
3. Customize the query for your specific task
4. Run it: python my_civic_tool.py
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import platform

# Suppress warnings for cleaner output
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("TQDM_DISABLE", "1")

import logging
logging.getLogger("httpx").setLevel(logging.WARNING)

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Add shared utilities to path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from cost_estimator import format_cost_comparison

# ══════════════════════════════════════════════════════════════
# STEP 1: CHOOSE YOUR TRACK (uncomment ONE)
# ══════════════════════════════════════════════════════════════

# TRACK = "eco"      # EcoHack - Environment & Climate
# TRACK = "city"    # CityHack - Civic Services
# TRACK = "edu"     # EduHack - Education Equity
TRACK = "justice"   # JusticeHack - Criminal Justice Reform

# ══════════════════════════════════════════════════════════════
# STEP 2: SET YOUR CUSTOM QUERY
# ══════════════════════════════════════════════════════════════

# Examples for each track:

# EcoHack:
# QUERY = "Which neighborhoods have the worst air quality and what are the AQI levels?"

# CityHack:
# QUERY = "Compare 311 response times between neighborhoods. Which have the longest and shortest times?"

# EduHack:
# QUERY = "What are the biggest risk factors for student failure, and what interventions does the data suggest?"

# JusticeHack (default):
QUERY = "What racial disparities exist in bail and pretrial detention, and what would be the impact of reform?"

# ══════════════════════════════════════════════════════════════
# STEP 3: CUSTOMIZE YOUR OUTPUT (optional)
# ══════════════════════════════════════════════════════════════

# Change this to customize the header for your report
REPORT_TITLE = "BAIL REFORM ANALYSIS"

# ══════════════════════════════════════════════════════════════
# TRACK CONFIGURATION (you don't need to change this)
# ══════════════════════════════════════════════════════════════

TRACK_CONFIG = {
    "eco": {
        "name": "EcoHack - Environment & Climate",
        "file": "ecohack_boston_environment.txt",
    },
    "city": {
        "name": "CityHack - Civic Services",
        "file": "cityhack_boston_311.txt",
    },
    "edu": {
        "name": "EduHack - Education Equity",
        "file": "eduhack_boston_schools.txt",
    },
    "justice": {
        "name": "JusticeHack - Criminal Justice Reform",
        "file": "justicehack_ma_justice.txt",
    },
}

# ══════════════════════════════════════════════════════════════
# MAIN PROGRAM (you can customize the output formatting)
# ══════════════════════════════════════════════════════════════

def main():
    # Get track configuration
    track = TRACK_CONFIG[TRACK]
    data_dir = Path(__file__).parent.parent.parent / "data"
    data_file = data_dir / track["file"]

    # Print header
    print(f"\n{'='*60}")
    print(f"{REPORT_TITLE}")
    print(f"{'='*60}")
    print(f"\nTrack: {track['name']}")
    print(f"Data: {track['file']}")
    print(f"Host: {platform.node()}")
    print(f"Time: {datetime.now().strftime('%B %d, %Y at %I:%M:%S %p')}")
    print(f"\n{'─'*60}\n")

    # Configure AI
    print("Initializing AI and loading data...")
    Settings.llm = Ollama(model="llama3.1", request_timeout=120.0)
    Settings.embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")

    # Load civic data
    documents = SimpleDirectoryReader(input_files=[str(data_file)]).load_data()
    print(f"✓ Loaded {len(documents)} documents")

    # Build search index
    print("Building search index...")
    index = VectorStoreIndex.from_documents(documents)
    print("✓ Index ready")

    # Create query engine
    query_engine = index.as_query_engine(streaming=True, similarity_top_k=3)

    # Execute query
    print(f"\nQuery: {QUERY}\n")
    print(f"{'─'*60}\n")
    print("Response:\n")

    import time
    start_time = time.time()

    # Stream the response
    response = query_engine.query(QUERY)
    response.print_response_stream()

    elapsed = time.time() - start_time

    # Print footer
    print(f"\n\n{'─'*60}")
    print(f"Completed in {elapsed:.1f} seconds")
    print(f"{'─'*60}\n")

    # STEP 4: ADD YOUR OWN ANALYSIS HERE (optional)
    # You can add follow-up queries or additional processing
    # Example:
    # print("\nFollow-up Analysis:\n")
    # followup = query_engine.query("What specific recommendations emerge from this data?")
    # followup.print_response_stream()

if __name__ == "__main__":
    main()
