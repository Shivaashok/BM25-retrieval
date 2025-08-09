# BM25.5 - Statement Relevance Search

This is a small Python project that uses the **BM25 ranking algorithm** to find the most relevant statements from a predefined list, based on a user’s input statement.

## Features
- Uses the **rank-bm25** library for BM25Okapi ranking
- Tokenizes text using **NLTK**
- Takes a user statement as input and finds the **top 3 most relevant statements**
- Shows relevance scores as percentages

## Installation

1. **Clone or download** this project.
2. Install dependencies:
   ```bash
   pip install rank-bm25 nltk
   ```
3. Download required NLTK tokenizers:
   ```bash
   python -m nltk.downloader punkt punkt_tab
   ```

## Usage

Run the script:
```bash
python bm2.5.py
```

You will be prompted to enter a statement.  
The script will compare it to a predefined set of statements and output the **top 3 matches** with relevance scores.

## Example
```
Enter your statement: I like programming in Python

Top 3 matches:
1. Python is a popular programming language. (92.4%)
2. I enjoy coding and building applications. (88.7%)
3. Many developers love Python for its simplicity. (86.5%)
```

## How BM25 Works (Simple Explanation)
BM25 is a ranking algorithm commonly used in search engines.  
It works by:
- Tokenizing text into words
- Calculating how often each word appears in each statement (term frequency)
- Adjusting scores based on how common or rare words are (inverse document frequency)
- Returning the statements with the highest similarity scores

Think of it as a smarter search that cares about word importance, not just matching keywords.

## Requirements
- Python 3.7+
- rank-bm25
- nltk

## License
This project is licensed under the MIT License.
