from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Add your OpenAI API key here
openai.api_key = "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"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "Please provide a valid message."}), 400

    try:
        # Communicate with ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"You are a helpful assistant. User says: {user_message}",
            max_tokens=150,
            temperature=0.7,
        )
        reply = response.choices[0].text.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
