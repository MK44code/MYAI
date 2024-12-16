
from transformers import pipeline

def text_generation_agent(prompt):
    try:
        generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
        response = generator(prompt, max_length=200, do_sample=True, temperature=0.7)[0]['generated_text']
        return response
    except Exception as e:
        return f"Error: {str(e)}"
