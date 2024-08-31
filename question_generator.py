from transformers import pipeline

# Load a pre-trained question generation model (this is a placeholder)
# You might need to find a specific model for question generation
question_generation_pipeline = pipeline("text2text-generation", model="valhalla/t5-small-qa-qg-hl")

def generate_questions(text):
    if len(text.strip()) == 0:
        return ["No content provided for question generation."]
    
    # Generate questions from text
    qg_input = "generate questions: " + text
    questions = question_generation_pipeline(qg_input, max_length=64, num_return_sequences=3)

    return [q['generated_text'] for q in questions]
