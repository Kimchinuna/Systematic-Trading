from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def initialize_vader():
    analyzer = SentimentIntensityAnalyzer()
    return analyzer

def analyze_sentiment_vader(analyzer, texts):
    sentiment_scores = []

    for text in texts:
        sentiment = analyzer.polarity_scores(text)
        sentiment_scores.append(sentiment)

    return sentiment_scores
