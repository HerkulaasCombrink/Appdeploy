import streamlit as st

# Attempt to load spaCy
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    SPACY_AVAILABLE = True
except Exception as e:
    nlp = None
    SPACY_AVAILABLE = False

# ----------------------------
# Title
# ----------------------------
st.title("English Glossing App (with spaCy fallback)")
st.write("""
This app glosses English sentences using a custom dictionary and, if available, 
enriches them with part-of-speech tags and lemmas from spaCy. If spaCy is unavailable, 
it falls back to a simple rule-based glossing engine.
""")

# ----------------------------
# Mini Glossary
# ----------------------------
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
# Glossing Function
# ----------------------------
def gloss_sentence(sentence):
    if SPACY_AVAILABLE:
        doc = nlp(sentence)
        table = []
        for token in doc:
            word = token.text
            lemma = token.lemma_
            pos = token.pos_
            gloss = glossary.get(word.lower(), f"{lemma}[?]")
            table.append({
                "Token": word,
                "Lemma": lemma,
                "POS": pos,
                "Gloss": gloss
            })
        return table
    else:
        # Basic fallback if spaCy isn't available
        tokens = sentence.split()
        table = []
        for word in tokens:
            gloss = glossary.get(word.lower(), f"{word}[?]")
            table.append({
                "Token": word,
                "Lemma": "-",
                "POS": "-",
                "Gloss": gloss
            })
        return table

# ----------------------------
# Input and Display
# ----------------------------
st.subheader("Enter a sentence:")
user_input = st.text_input("Type a sentence to gloss", placeholder="e.g., I am reading a book")

if user_input:
    st.markdown("### Gloss Table")
    glossed = gloss_sentence(user_input)
    st.table(glossed)

    if not SPACY_AVAILABLE:
        st.warning("spaCy is not available. Using basic rule-based glossing only (no POS or Lemmas).")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.write("Built as an educational demo. Expand the glossary or use full NLP pipelines for advanced glossing.")
