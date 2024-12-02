from nlp_processor import NLPProcessor
from template_renderer import TemplateRenderer

class FlyerGenerator:
    def __init__(self):
        self.nlp_processor = NLPProcessor()
        self.template_renderer = TemplateRenderer()

    def generate_flyer(self, text_input):
        # Debugging log to confirm input
        print(f"Processing text input: {text_input}")
        
        # Process text with NLPProcessor
        details = self.nlp_processor.process_text(text_input)
        print(f"Processed details: {details}")
        
        # Render flyer with TemplateRenderer
        flyer_path = self.template_renderer.render(details)
        print(f"Flyer rendered at: {flyer_path}")
        
        return flyer_path
