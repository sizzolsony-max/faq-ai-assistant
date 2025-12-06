# 🤖 FAQ AI Assistant – AI Powered Help Center (Streamlit + NLP)

This is a simple **AI FAQ Assistant web application** built using **Streamlit**, **TF-IDF vectorization**, and **Cosine Similarity**.  
Users can type any question related to shopping or customer support, and the app returns the **most relevant FAQ answer**.

---

## 🚀 Features

✔ Accepts any customer support / shopping related question  
✔ AI model finds the closest matching FAQ using text similarity  
✔ Returns the best-matched question and answer  
✔ Fully runs on the browser using **Streamlit**  
✔ Live deployment available on Streamlit Cloud  

---

## 🧠 How It Works

1. FAQ dataset (questions + answers) is loaded into a Pandas DataFrame  
2. Questions are vectorized using **TF-IDF**  
3. User query is compared with all FAQs using **Cosine Similarity**  
4. The most similar question is selected and its answer is returned  

> This approach is lightweight and fast without requiring a heavy LLM model.

---

## 📂 Project Structure

```
faq-ai-assistant/
│
├─ app.py                # Main Streamlit application
├─ requirements.txt      # List of Python dependencies
└─ .devcontainer (optional)
```

---

## 🛠 Tech Stack

| Category | Technology |
|---------|-------------|
| Programming | Python |
| Web Framework | Streamlit |
| NLP | TF-IDF Vectorizer, Cosine Similarity |
| Libraries | pandas, scikit-learn |

---

## ▶️ How to Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit app:

```bash
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

## 🌐 Live Demo (Deployment)

## 🌐 Live Demo (Deployment)

🔗 Live App: https://faq-ai-assistant-xxxxx.streamlit.app  
🔗 GitHub Repository: https://github.com/YOUR-USERNAME/faq-ai-assistant


---

## 📌 Screenshot (optional)

You can upload a screenshot of your deployed app here later.

---

## 💡 Future Improvements

🔹 Upload FAQ CSV instead of hard-coding  
🔹 Display top 3 similar answers instead of only 1  
🔹 Add speech-to-text input for user queries  
🔹 Add database integration for dynamic FAQs  

---

## 👨‍💻 Author

**Your Name – Software Developer (Python & AI)**  
📩 Portfolio, LinkedIn, Email links can be added here if you want.

---

If you like this project, don't forget to ⭐ star the repository 😊
