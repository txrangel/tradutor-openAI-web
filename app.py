from flask import Flask
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key      = os.getenv("OPENAI_API_KEY")
openai.Model.list()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Seu aplicativo Flask está funcionando corretamente!'

@app.route('/traduzir', methods=['POST'])
def traduzir():
    if request.method == 'POST':
        texto  = request.json['texto']
        idioma = request.json['idioma']
        
        response            = openai.Completion.create(
            model               = "text-davinci-003",
            prompt              = "Traduza esse texto: '{texto}', para esse idioma: '{idioma}'",
            temperature         = 0.5,
            max_tokens          = 500,
            n                   = 1.0,
            stop                = None
        )
        
        traducao = response.choices[0].text.strip()
        
        return jsonify({'traducao': traducao})


if __name__ == '__main__':
    app.run()
