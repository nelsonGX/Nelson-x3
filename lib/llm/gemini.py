import google.generativeai as genai

from lib.load_config import gemini_key

genai.configure(api_key=gemini_key)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

async def generate(history):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
    response = await model.generate_content_async(history)
    print(response)

    return response.text