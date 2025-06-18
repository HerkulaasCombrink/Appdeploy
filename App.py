import streamlit as st
import spacy

# ----------------------------
# Title and Introduction
# ----------------------------
st.title("English Sentence Glossing with spaCy (Tutorial)")
st.write("""
This app glosses English sentences using a custom dictionary and grammatical information from spaCy.
It tokenizes and tags each word with its part of speech (POS), lemma, and gloss where available.
""")

# ----------------------------
# Load spaCy model
# ----------------------------
# Load the small English model (make sure it's downloaded)
nlp = spacy.load("en_core_web_sm")

# ----------------------------
# Define a mini-glossary
# ----------------------------
# This is a very basic word-to-gloss dictionary.
glossary = {
    "i": "1SG",
    "you": "2SG",
    "he": "3SG.M",
    "she": "3SG.F",
    "it": "3SG.N",
    "we": "1PL",
    "they": "3PL",
    "am": "BE.PRES.1SG",
    "are": "BE.PRES.2PL",
    "is": "BE.PRES.3SG",
    "was": "BE.PAST.1/3SG",
    "were": "BE.PAST.2PL",
    "have": "AUX.PRES",
    "has": "AUX.3SG",
    "go": "GO.PRES",
    "went": "GO.PAST",
    "like": "LIKE.PRES",
    "liked": "LIKE.PAST",
    "a": "INDEF.ART",
    "the": "DEF.ART",
    "dog": "DOG.N",
    "cat": "CAT.N",
    "book": "BOOK.N",
    "read": "READ",
    "reading": "READ.PROG",
    "run": "RUN.PRES",
    "running": "RUN.PROG",
}

# ----------------------------
# Glossing function with spaCy
# ----------------------------
# This function uses spaCy to analyze the sentence,
# and combines the POS, lemma, and gloss into a single display table.
def gloss_with_spacy(sentence):
    doc = nlp(sentence)
    glossed_table = []

    for token in doc:
        word = token.text
        lemma = token.lemma_
        pos = token.pos_
        gloss = glossary.get(word.lower(), f"{lemma}[?]")
        glossed_table.append({
            "Token": word,
            "Lemma": lemma,
            "POS": pos,
            "Gloss": gloss
        })

    return glossed_table

# ----------------------------
# Get user input
# ----------------------------
st.subheader("Enter a sentence to gloss:")
user_input = st.text_input("Type your sentence here", placeholder="e.g., I am reading a book")

# ----------------------------
# Output results
# ----------------------------
if user_input:
    st.markdown("### Gloss Table")
    results = gloss_with_spacy(user_input)
    st.table(results)

    st.markdown("### Notes")
    st.write("""
    - Glosses come from a custom dictionary. Unmatched words are lemmatized and marked with `[?]`.
    - POS tags are from spaCy and follow Universal POS standards.
    - This is a simplified educational example, not a full interlinear glossing tool.
    """)

# ----------------------------
# Educational Footer
# ----------------------------
st.markdown("---")
st.subheader("Extend This App")
st.write("""
To make this more linguistically accurate, you could:
- Follow Leipzig Glossing Rules for full interlinear glossing.
- Add morphological parsing or dependency trees.
- Extend the glossary using real datasets or Universal Dependencies.
""")
