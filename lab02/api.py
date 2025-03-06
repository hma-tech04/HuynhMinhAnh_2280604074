from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher


app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
rail_fence = RailFenceCipher()


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/caesar/decypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


@app.route("/api/railfence/encrypt", methods=["POST"])
def rail_fence_encypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = rail_fence.railfence_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/railfence/decrypt", methods=["POST"])
def rail_fence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = rail_fence.railfence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
