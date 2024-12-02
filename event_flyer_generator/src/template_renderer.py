from jinja2 import Environment, FileSystemLoader
from flask import url_for
import os
import imgkit

class TemplateRenderer:
    def __init__(self):
        templates_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))
        self.env = Environment(loader=FileSystemLoader(templates_path))
        self.env.globals['url_for'] = url_for  # Add url_for to the Jinja2 environment globals

        # Configure imgkit with wkhtmltoimage path
        self.imgkit_config = imgkit.config(wkhtmltoimage='/usr/local/bin/wkhtmltoimage')
    
    def render(self, details, image_url=None):
        """
        Renders a flyer with optional DALL·E 3 image.

        :param details: Dictionary with flyer details.
        :param image_url: URL of the AI-generated image (optional).
        :return: Path to the rendered flyer PNG file.
        """
        # Render the template with details and optional image
        template = self.env.get_template('base.html')
        flyer_content = template.render(details=details, image_url=image_url)
        
        # Ensure output folder exists
        output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static/output'))
        os.makedirs(output_folder, exist_ok=True)

        # Save the rendered HTML to the output folder
        flyer_html_path = os.path.join(output_folder, 'flyer.html')
        with open(flyer_html_path, 'w') as f:
            f.write(flyer_content)

        # Use the saved HTML file as input for wkhtmltoimage
        flyer_image_path = os.path.join(output_folder, 'flyer.png')
        imgkit_options = {
            'enable-local-file-access': None,
            'width': 1024,  # Set the width to match the image size
            'height': 0,    # Let the height scale automatically
            'quality': 100  # Ensure maximum quality
        }
        imgkit.from_file(flyer_html_path, flyer_image_path, config=self.imgkit_config, options=imgkit_options)
        
        return flyer_image_path
