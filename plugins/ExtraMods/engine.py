import openai

async def ai(query):
    openai.api_key = "sk-proj-5GJKXkmInN6EvexxnztIT3BlbkFJTk5Wjtc0JIe2HCCScaQk" #Your openai api key
    response = openai.Completion.create(engine="gpt-3.5-turbo", prompt=query, max_tokens=100, n=1, stop=None, temperature=0.9, timeout=5)
    return response.choices[0].text.strip()
     
async def ask_ai(client, m, message):
    try:
        question = message.text.split(" ", 1)[1]
        # Generate response using OpenAI API
        response = await ai(question)
        # Send response back to user
        await m.edit(f"{response}")
    except Exception as e:
        # Handle other errors
        error_message = f"An error occurred: {e}"
        await m.edit(error_message)
