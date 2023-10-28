import bardapi
import subprocess
import base64
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Bard API key
token = 'cAjPLLW__yTWrHFYf9NrWNSPs8DK7zdeNWJXDCZzpdkxY3Bq-1K7aMcy2WJORKOO166LYA.'
preferred_language = 'en'  # Preferred language is set to English
bard = bardapi.core.Bard(token)

# Define a function to interact with the chatbot
def chat_with_bard(prompt, source_language):
  """Chats with Bard."""
  bot_message = bardapi.core.Bard(token).get_answer(prompt)['content']
  return bot_message

# Define a route for the root URL to serve the HTML file
@app.route('/ai')
def index():
  return render_template('index.html')

# Define a route for handling chat requests
@app.route('/chat', methods=['POST'])
def chat():
  data = request.get_json()
  user_message = data['message']
  print(user_message)
  bot_message = chat_with_bard(user_message, source_language=preferred_language)
  print(bot_message)
  return jsonify({'message': bot_message})

@app.route('/image', methods=['POST'])
def process_image():
    try:
        uploaded_file = request.files['image']

        if uploaded_file:
            # Read the image data
            image_data = uploaded_file.read()
            print(image_data)

            # Ask Bard about the content of the image
            response = bard.ask_about_image('What is in the image tell me just the name. Only Name?', image_data)
            bot_message = response['content']
            print(bot_message)
        else:
            bot_message = "No image uploaded."

    except Exception as e:
        bot_message = str(e)

    return jsonify({'message': bot_message})



if __name__ == '__main__':
  go_process = subprocess.Popen(["go", "run", "main.go"])
  app.run(host='localhost', port=8080)
  
