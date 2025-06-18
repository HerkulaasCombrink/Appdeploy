import streamlit as st

# ----------------------------
# Title and introduction text
# ----------------------------
st.title("English Sentence Glossing Tutorial")
st.write("""
This simple app demonstrates how to gloss English sentences using a basic rule-based approach.
In linguistics, glossing breaks down a sentence into word-by-word meaning or function.
This version uses a mini-glossary to simulate glossing for demonstration purposes.
""")

# ----------------------------
# Step 1: Define a small glossary
# ----------------------------
# We create a dictionary that maps common English words to their gloss equivalents.
# For example, 'I' becomes '1SG' (first-person singular), and 'am' becomes 'BE.PRES'.
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
    "read": "READ.PRES",
    "reading": "READ.PROG",
    "run": "RUN.PRES",
    "running": "RUN.PROG",
}

# ----------------------------
# Step 2: Glossing function
# ----------------------------
# This function will:
# 1. Convert the sentence to lowercase
# 2. Tokenize it by splitting on spaces
# 3. Replace each word with its gloss if it exists in the glossary
# 4. If a word is not found, keep it as is but flag it with "[?]"
def gloss_sentence(sentence):
    words = sentence.lower().split()
    glossed = []
    for word in words:
        gloss = glossary.get(word, f"{word}[?]")
        glossed.append(gloss)
    return " ".join(glossed)

# ----------------------------
# Step 3: Get user input
# ----------------------------
st.subheader("Enter a sentence to gloss:")
user_input = st.text_input("Type your sentence here", placeholder="e.g., I am reading a book")

# ----------------------------
# Step 4: Display glossed output
# ----------------------------
if user_input:
    st.markdown("### Glossed Output:")
    glossed = gloss_sentence(user_input)
    st.code(glossed, language="text")
    st.write("""
    _Note: Words not found in the mini-glossary are marked with `[?]` for manual checking or expansion._
    """)

# ----------------------------
# Step 5: Educational notes
# ----------------------------
st.markdown("---")
st.subheader("About This App")
st.write("""
This is a simplified version of a glossing system. In professional linguistics,
glosses follow the **Leipzig Glossing Rules** and include morphological and grammatical markers.

To expand this app, consider:
- Adding part-of-speech tagging
- Using spaCy or NLTK for more complex analysis
- Creating glosses for morphologically rich languages
""")
