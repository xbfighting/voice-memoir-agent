import openai

openai.api_key = "YOUR_OPENAI_KEY"

def generate_reply(user_input, context=""):
    messages = [
        {"role": "system", "content": "你是一个温柔的引导者，帮助用户回忆他们的人生经历。"},
        {"role": "user", "content": f"我之前说过：{context}"},
        {"role": "user", "content": f"我现在想说：{user_input}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]