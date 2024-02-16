from transformers import pipeline

def gpt_2_neo(prompt: str):
    # Load pipeline
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
    
    # Generate answer
    answer = generator(prompt, do_sample=True, max_length=400, temperature=0.9, truncation=True)

    # Streamline answer
    return answer[0]["generated_text"]

if __name__ == "__main__":
    answer = gpt_2_neo("What is the differenece between Lockeed Martin and Boeing?")
    print(answer)