import requests
from flask import Flask, request, jsonify
from flask_cors import CORS  # 导入 CORS

app = Flask(__name__)
CORS(app)  # 启用 CORS 支持

# 设置 OpenAI 的 API 密钥
API_KEY = '输入你的openai KEY'

# 定义一个处理来自前端的 POST 请求的路由
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # 发送请求到 OpenAI API
        response = requests.post(
            'https://api.chatanywhere.org/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": user_message}],
                "max_tokens": 1000
            }
        )

        # 检查响应状态
        response_data = response.json()
        if response.status_code == 200:
            reply = response_data['choices'][0]['message']['content'].strip()
            return jsonify({'reply': reply})
        else:
            return jsonify({'error': response_data.get('error', {}).get('message', 'Unknown error')}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)  # 仅保留这一行
