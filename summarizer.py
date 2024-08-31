from transformers import pipeline

# Load summarization model
summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Ensure the text is not empty or too short for summarization
    if len(text.strip()) == 0:
        return "No text provided for summarization."
    
    # Summarize the text
    summary = summarization_pipeline(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    return summary
