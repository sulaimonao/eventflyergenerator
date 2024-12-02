import os
from dotenv import load_dotenv
from openai import OpenAI, APIError, APITimeoutError, APIConnectionError, BadRequestError, AuthenticationError, PermissionDeniedError, RateLimitError

class OpenAIClient:
    def __init__(self):
        # Load environment variables from the .env file
        env_path = os.path.join(os.path.dirname(__file__), '../.env')
        load_dotenv(env_path)

        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is missing in the environment variables or .env file.")
        
        # Initialize OpenAI
        self.client = OpenAI(api_key=self.api_key)

    def create_chat_completion(self, model, messages, max_tokens=150, temperature=0.7):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"Error interacting with OpenAI API: {e}")

    def generate_image(self, prompt, size="1024x1024"):
        try:
            # Use OpenAI's Image API to generate an image
            response = self.client.images.generate(prompt=prompt, n=1, size=size)
            
            # Access the first image URL using dot notation
            image_url = response.data[0].url
            
            return image_url
        except Exception as e:
            raise RuntimeError(f"Error generating image with OpenAI: {e}")

