from utils import OpenAIClient

class NLPProcessor:
    def __init__(self):
        self.client = OpenAIClient()

    def process_text(self, text):
        messages = [
            {"role": "system", "content": "You are an assistant that extracts event details from text."},
            {"role": "user", "content": text}
        ]
        
        # Get response from OpenAI
        response = self.client.create_chat_completion(model="gpt-4", messages=messages)
        print(f"OpenAI response: {response}")

        # Parse the response into a structured dictionary
        details = {}
        for line in response.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                # Convert keys to valid variable names (e.g., replace spaces with underscores)
                details[key.strip().lower().replace(' ', '_')] = value.strip()
        return details
