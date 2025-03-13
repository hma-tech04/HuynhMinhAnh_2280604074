from flask import Flask, request, jsonify

from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.transpositon.transposition_cipher import TranspositionCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
rail_fence = RailFenceCipher()
playfair = PlayFairCipher()
transposition = TranspositionCipher()


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
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


@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair.create_playfair_matrix(key)
    return jsonify("playfair_matrix:", playfair_matrix)


@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    plain_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(plain_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})


@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = transposition.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = transposition.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
