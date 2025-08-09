from rank_bm25 import BM25Okapi
import nltk
nltk.download("punkt")

documents = [
    "Python is a great programming language for beginners.",
    "Artificial intelligence is transforming industries worldwide.",
    "Machine learning enables systems to learn from data.",
    "The capital of France is Paris.",
    "Space exploration has expanded human knowledge about the universe.",
    "Renewable energy sources are key to fighting climate change.",
    "Quantum computing will revolutionize data processing.",
    "Blockchain is the technology behind cryptocurrencies.",
    "5G networks offer faster communication speeds.",
    "Healthy eating is important for a balanced lifestyle."
]

tokenized_docs = [nltk.word_tokenize(doc.lower()) for doc in documents]

bm25 = BM25Okapi(tokenized_docs)

query = input("Enter your statement: ")
tokenized_query = nltk.word_tokenize(query.lower())

scores = bm25.get_scores(tokenized_query)

ranked_results = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)

print("\nTop 3 relevant statements:")
for doc, score in ranked_results[:3]:
    percentage = (score / max(scores)) * 100
    print(f"{percentage:.2f}% - {doc}")
