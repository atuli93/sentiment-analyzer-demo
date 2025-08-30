import streamlit as st

st.title("Sentiment Analyzer Demo")
text = st.text_input("Enter text:")

if text:
    positive_words = ["love", "great", "happy", "excellent", "good"]
    negative_words = ["hate", "bad", "sad", "terrible", "awful"]

    if any(word in text.lower() for word in positive_words):
        st.write("Prediction: Positive 😊")
    elif any(word in text.lower() for word in negative_words):
        st.write("Prediction: Negative 😞")
    else:
        st.write("Prediction: Neutral 😐")
