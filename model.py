from transformers import pipeline

model_name = "facebook/bart-large-cnn"

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def nlp_summarizer(article):
    pred = summarizer(article, do_sample=False)
    return pred[0]["summary_text"]
