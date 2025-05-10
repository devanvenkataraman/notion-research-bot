import openai
from config import OPENAI_API_KEY, GPT_MODEL

openai.api_key = OPENAI_API_KEY

def generate_report(topic):
    """
    Calls OpenAI's chat/completions endpoint to generate a research report on the topic.
    Returns the assistant's message content.
    """
    prompt = (
        f"""
        You are an expert research assistant. Write a deep, evidence-based, multi-perspective research report on the following topic. 
        - Use credible sources and cite them inline (e.g., [1], [2]).
        - Cover background, current debates, and future directions.
        - Structure with clear headings and bullet points where helpful.
        - Be concise but thorough, and avoid speculation.
        
        Topic: {topic}
        """
    )
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": "You are a world-class research assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1800,
        temperature=0.7,
    )
    return response["choices"][0]["message"]["content"] 