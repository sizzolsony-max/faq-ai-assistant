import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

st.title("🤖 FAQ Assistant - AI Powered Help Center")

# Sample FAQ dataset
data = {
    "question": [
        "How can I reset my password?",
        "How do I track my order?",
        "Can I return a product?",
        "What payment methods do you accept?",
        "How do I contact customer support?"
    ],
    "answer": [
        "Click on 'Forgot Password' on the login page and follow the instructions.",
        "Go to the Orders section and click on Track Order.",
        "Yes, you can return a product within 30 days of delivery.",
        "We accept credit/debit cards, UPI, and net banking payments.",
        "You can reach customer support via email or toll-free number."
    ]
}

df = pd.DataFrame(data)

# Convert questions into TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["question"])

st.write("Ask a question related to shopping or customer support:")

user_query = st.text_input("Your question:")

if st.button("Get Answer"):
    if user_query.strip() == "":
        st.warning("Please type a question.")
    else:
        # Transform the user query to the same TF-IDF space
        query_vector = vectorizer.transform([user_query])

        # Compute cosine similarity between the query and all FAQ questions
        similarity = cosine_similarity(query_vector, tfidf_matrix).flatten()

        # Find the index of the best matching question
        best_match_index = similarity.argmax()

        best_question = df.iloc[best_match_index]["question"]
        best_answer = df.iloc[best_match_index]["answer"]

        st.subheader("Best Match:")
        st.write(best_question)

        st.subheader("Answer:")
        st.write(best_answer)
