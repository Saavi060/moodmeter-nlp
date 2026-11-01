import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page configuration
st.set_page_config(
    page_title="MoodMeter",
    page_icon="💜",
    layout="centered"
)

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #FAF8FC;
}
h1 {
    color: #76558F;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: #777777;
    font-size: 17px;
}
</style>
""", unsafe_allow_html=True)

# Application heading
st.title("MoodMeter")
st.markdown(
    '<p class="subtitle">Understanding emotions, one sentence at a time.</p>',
    unsafe_allow_html=True
)

st.divider()

st.subheader("Analyse Your Text")

st.write(
    "Enter a sentence or paragraph below. "
    "MoodMeter will analyse its emotional tone."
)

# Text input
user_text = st.text_area(
    "Enter your text here:",
    placeholder="Example: I am having a wonderful day!",
    height=150
)

# Analysis button
if st.button("Analyse Sentiment", use_container_width=True):

    if user_text.strip():

        # Perform sentiment analysis
        scores = analyzer.polarity_scores(user_text)

        compound = scores["compound"]

        # Classify sentiment
        if compound >= 0.05:
            sentiment = "Positive"
            explanation = "Your text expresses predominantly positive sentiment."
        elif compound <= -0.05:
            sentiment = "Negative"
            explanation = "Your text expresses predominantly negative sentiment."
        else:
            sentiment = "Neutral"
            explanation = "Your text expresses predominantly neutral sentiment."

        # Display results
        st.divider()
        st.subheader("Your Analysis Results")

        st.success(f"Overall Sentiment: {sentiment}")

        st.write(explanation)

        st.subheader("Sentiment Score Breakdown")

        col1, col2, col3 = st.columns(3)

        col1.metric("Positive", f"{scores['pos'] * 100:.1f}%")
        col2.metric("Neutral", f"{scores['neu'] * 100:.1f}%")
        col3.metric("Negative", f"{scores['neg'] * 100:.1f}%")

        st.write("Sentiment Intensity")

        st.progress(
            min(1.0, abs(compound)),
            text=f"Compound score: {compound:.3f}"
        )

        st.caption(
            "Note: Sentiment analysis identifies the emotional tone "
            "of text. It does not determine a person's actual mental state."
        )

    else:
        st.warning("Please enter some text before analysing.")

st.divider()

st.caption("MoodMeter | An NLP Sentiment Analysis Project")
