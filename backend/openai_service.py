from openai import OpenAI

client = OpenAI()

def chat_with_openai(message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao acessar ChatGPT: {str(e)}"
