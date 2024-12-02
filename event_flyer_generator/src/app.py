from flask import Flask, request, render_template
from flyer_generator import FlyerGenerator
from utils import OpenAIClient

app = Flask(__name__, template_folder='../templates', static_folder='../static')
generator = FlyerGenerator()
ai_client = OpenAIClient()

@app.route('/')
def home():
    return render_template('flyer_preview.html')

@app.route('/generate', methods=['POST'])
def generate():
    event_details = request.form.get('event_details')
    if not event_details:
        return "No event details provided.", 400

    flyer_path = generator.generate_flyer(event_details)
    return render_template('flyer_preview.html', flyer_path=flyer_path)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    event_details = request.form.get('event_details')
    if not event_details:
        return "No event details provided.", 400

    # Generate an image prompt for DALL·E 3
    image_prompt = f"An artistic flyer background for an event: {event_details}"
    generated_image_url = ai_client.generate_image(image_prompt)

    return render_template('flyer_preview.html', image_url=generated_image_url, event_details=event_details)

if __name__ == '__main__':
    app.run(debug=True)
