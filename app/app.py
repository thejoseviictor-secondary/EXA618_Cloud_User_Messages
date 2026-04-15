from flask import Flask, request, jsonify
from repository.db import get_connection
from http import HTTPStatus
from dotenv import load_dotenv
import os

# Loading environment variables:
load_dotenv()

app = Flask(__name__)

@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM messages_schema.messages_table")
        messages = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(messages)
    except:
        return jsonify({"error": "Erro interno ao buscar mensagens!"}), HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    action = data.get("action")
    message = data.get("message")
    author = data.get("author")

    try:
        if action == "put" and message and author:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO messages_schema.messages_table (action, message, author) VALUES (%s, %s, %s)",
                (action, message, author)
            )
            conn.commit()

            cursor.close()
            conn.close()

            return jsonify({"message": "Mensagem enviada com sucesso!"}), HTTPStatus.OK
        
        else:
            return jsonify({"error": "Dados inválidos, verifique os campos de entrada!"}), HTTPStatus.BAD_REQUEST
    except:
        return jsonify({"error": "Erro interno ao enviar mensagem!"}), HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(host=os.getenv("BACKEND_HOST"), port=os.getenv("BACKEND_PORT"), debug=True)
