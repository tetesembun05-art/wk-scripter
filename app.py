from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import random
import os

app = Flask(__name__)

# CORS untuk SEMUA origin (CodePen, localhost, dll)
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route('/')
def home():
    return "Warung Komedi API is running!"

@app.route('/generate', methods=['POST', 'OPTIONS'])
def generate():
    # Handle preflight OPTIONS
    if request.method == 'OPTIONS':
        return '', 200
    
    data = request.json or {}
    tema = data.get('tema', 'general')
    season = data.get('season', '1')
    
    script_id = f"WK_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    dialogues = [
        {
            'speaker': 'bang_jali',
            'text': f'Nah ini guys, {tema}! Gue punya yang terbaik!',
            'emotion': 'pede',
            'duration_sec': random.randint(5, 8)
        },
        {
            'speaker': 'mang_udin',
            'text': 'Gue tuh... liat ini jadi inget masa lalu. Dulu gue susah...',
            'emotion': 'nangis',
            'duration_sec': random.randint(6, 10)
        },
        {
            'speaker': 'asep',
            'text': f'Ini semua tentang filsafat hidup. {tema} itu relatif.',
            'emotion': 'ngawur',
            'duration_sec': random.randint(7, 12)
        },
        {
            'speaker': 'bang_dul',
            'text': '...Lu mau kopi apa?',
            'emotion': 'flat',
            'duration_sec': random.randint(2, 4)
        }
    ]
    
    return jsonify({
        'success': True,
        'script': {
            'script_id': script_id,
            'metadata': {
                'tema': tema,
                'season': season,
                'created': datetime.now().isoformat()
            },
            'dialogue': dialogues
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
