"""
text_insights.py
----------------
A small command-line tool that reads a text file and reports:
  - total words and unique words
  - the most frequent words (ignoring common stop words)
  - average word and sentence length

Usage:
    python text_insights.py sample.txt
    python text_insights.py sample.txt --top 5
"""

import argparse
import re
from collections import Counter

# A short stop-word list keeps the "top words" output meaningful.
STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "for",
    "is", "are", "was", "were", "be", "it", "this", "that", "with", "as",
    "at", "by", "from", "i", "you", "he", "she", "we", "they", "his", "her",
}


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def words(text: str):
    """Lowercased word tokens, letters and apostrophes only."""
    return re.findall(r"[a-zA-Z']+", text.lower())


def sentences(text: str):
    """Rough sentence split on ., ! and ?."""
    parts = re.split(r"[.!?]+", text)
    return [p.strip() for p in parts if p.strip()]


def analyse(text: str, top: int = 10) -> dict:
    tokens = words(text)
    sents = sentences(text)
    content = [w for w in tokens if w not in STOP_WORDS]

    return {
        "total_words": len(tokens),
        "unique_words": len(set(tokens)),
        "sentences": len(sents),
        "avg_word_len": round(sum(len(w) for w in tokens) / max(len(tokens), 1), 2),
        "avg_sentence_len": round(len(tokens) / max(len(sents), 1), 2),
        "top_words": Counter(content).most_common(top),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Quick text insights.")
    parser.add_argument("file", help="path to a .txt file")
    parser.add_argument("--top", type=int, default=10, help="how many top words to show")
    args = parser.parse_args()

    report = analyse(read_text(args.file), top=args.top)

    print(f"Total words      : {report['total_words']}")
    print(f"Unique words     : {report['unique_words']}")
    print(f"Sentences        : {report['sentences']}")
    print(f"Avg word length  : {report['avg_word_len']}")
    print(f"Avg sentence len : {report['avg_sentence_len']} words")
    print("\nMost frequent words:")
    for word, count in report["top_words"]:
        print(f"  {word:<14} {count}")


if __name__ == "__main__":
    main()
