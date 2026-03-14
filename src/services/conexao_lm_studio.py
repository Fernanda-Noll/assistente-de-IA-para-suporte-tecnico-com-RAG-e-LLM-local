import os
from dotenv import load_dotenv
from openai import OpenAI
from script_prompt_ia import script

load_dotenv()
client = OpenAI(
        base_url=os.getenv("BASE_URL"),
        api_key=os.getenv("API_KEY")
    )

# -> CONEXÃO LM STUDIO
def conexao_com_llama(prompt):
    SYSTEM_PROMPT = script()
    
    response = client.chat.completions.create(
        model="meta-llama-3.1-8b-instruct",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
