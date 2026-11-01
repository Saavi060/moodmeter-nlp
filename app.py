import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page configuration
st.set_page_config(
    page_title="MoodMeter | Sentiment Analysis",
    page_icon="💜",
    layout="centered"
)

# Initialize NLP analyzer
analyzer = SentimentIntensityAnalyzer()

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: #FAF8FC;
}

h1 {
    color: #74528F;
    text-align: center;
    font-size: 42px !important;
}

.subtitle {
    text-align: center;
    color: #777080;
    font-size: 17px;
    margin-bottom: 30px;
}

.section-title {
    color: #74528F;
    font-size: 23px;
    font-weight: bold;
}

.result-box {
    background: #F0E8F7;
    padding: 22px;
    border-radius: 15px;
    text-align: center;
    margin: 15px 0;
}

.footer {
    text-align: center;
    color: #999;
    font-size: 13px;
    padding: 25px;
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

# Introduction
st.markdown(
    '<p class="section-title">Explore the Sentiment Behind Your Words</p>',
    unsafe_allow_html=True
)

st.write(
    "Enter any English sentence or paragraph. "
    "Our NLP system will analyse its emotional tone "
    "and identify its overall sentiment."
)

# Text input
user_text = st.text_area(
    "Your text",
    placeholder="Example: I had an amazing day today. I feel happy and grateful!",
    height=160
)

if user_text.strip():
    st.caption(
        f"Characters: {len(user_text)} | Words: {len(user_text.split())}"
    )

# Analyse button
if st.button("Analyse Sentiment", use_container_width=True):

    if user_text.strip():

        scores = analyzer.polarity_scores(user_text)
        compound = scores["compound"]

        # Sentiment classification
        if compound >= 0.05:
            sentiment = "POSITIVE"
            emoji = "☀️"
            explanation = "The text expresses predominantly positive sentiment."
        elif compound <= -0.05:
            sentiment = "NEGATIVE"
            emoji = "🌧️"
            explanation = "The text expresses predominantly negative sentiment."
        else:
            sentiment = "NEUTRAL"
            emoji = "☁️"
            explanation = "The text expresses predominantly neutral sentiment."

        st.divider()

        st.markdown(
            '<p class="section-title">Your Analysis Results</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="result-box">
                <h1>{emoji}</h1>
                <h2 style="color:#74528F;">{sentiment}</h2>
                <p style="color:#62596A;">{explanation}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Score breakdown
        st.subheader("Sentiment Score Breakdown")

        col1, col2, col3 = st.columns(3)

        col1.metric("Positive", f"{scores['pos'] * 100:.1f}%")
        col2.metric("Neutral", f"{scores['neu'] * 100:.1f}%")
        col3.metric("Negative", f"{scores['neg'] * 100:.1f}%")

        # Visualisation
        st.subheader("Visual Representation")

        chart_data = pd.DataFrame(
            {
                "Sentiment": ["Positive", "Neutral", "Negative"],
                "Score": [
                    scores["pos"],
                    scores["neu"],
                    scores["neg"]
                ]
            }
        )

        st.bar_chart(
            chart_data.set_index("Sentiment")
        )

        st.subheader("Overall Sentiment Intensity")

        st.progress(
            min(1.0, abs(compound)),
            text=f"Compound Score: {compound:.3f}"
        )

        st.info(
            "The compound score ranges from -1 (most negative) "
            "to +1 (most positive)."
        )

        st.caption(
            "Note: Sentiment analysis identifies the emotional tone "
            "of written text. It does not diagnose or determine "
            "a person's actual psychological state."
        )

    else:
        st.warning("Please enter some text before analysing.")

# Footer
st.divider()

st.markdown(
    '<p class="footer">MOODMETER | NLP SENTIMENT ANALYSIS PROJECT</p>',
    unsafe_allow_html=True
)
