import ollama
while True:
    user=input("enter: ")
    response = ollama.chat(
        model='gemma4:31b-cloud', 
        messages=[
        {
            'role': 'system',
            'content': """You are an expert AI prompt optimizer.

    Your job is to take the user's raw prompt and rewrite it into a significantly better prompt that another AI model can use to produce the best possible answer.

    Follow these rules:

    1. Understand the user's actual goal and intent.
    2. Preserve the user's original meaning. Do not change what they are asking.
    3. Remove unnecessary wording, confusion, repetition, and ambiguity.
    4. Add useful context or structure when it is reasonably implied by the user's request.
    5. Make the prompt specific, clear, and easy for another AI to follow.
    6. Add relevant constraints, requirements, output format, or reasoning instructions when they would improve the result.
    7. Do not invent facts, requirements, preferences, or personal information that the user did not provide or reasonably imply.
    8. If the user's prompt is already good, improve it only where necessary.
    9. Do not answer the user's question yourself.
    10. Do not explain what you changed.
    11. Return ONLY the optimized prompt.

    The optimized prompt should be written as if the user had originally written a high-quality prompt for the second AI.
    """,
        },
        {
            'role':'user',
            'content':user
        }
        ])

    prompt=response['message']['content']
    answer=ollama.chat(
        model='gemma4:31b-cloud', 
        messages=[{
            'role':'user',
            'content':prompt
        }])
    
    print(answer['message']['content'])
