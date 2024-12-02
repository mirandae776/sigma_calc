from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Results mapped to direct image URLs for Sigma results
results_with_images = {
    "sigma:- you’re just a chill guy": "/static/images/Sigma1ChillGuy.png",
    "sigma:- you got that special something congratz": "/static/images/Sigma2WallBoiz.png",
    "walk proud alpha": "/static/images/Sigma3WalkProud.png",
    "sigma:- yasss queen": "/static/images/Sigma4YasssQueen.png",
    "sigma:- pop off king": "/static/images/Sigma5ThickOfIt.png",
    "chad:- peaking in highschool": "/static/images/Chad HS.png",
    "born to mew": "/static/images/Chad BornMew.png",
    "rizzler:- I want you": "/static/images/RizzWantYou.png",
    "rizzler:- You got pull more than a black hole": "/static/images/RizzBlackHole.png",
    "npc:- this is you -> -_-": "/static/images/NPCThisYou.png",
    "npc:- stay in school": "/static/images/NPCSchool.png",
    "beta:- maybe in the next life": "/static/images/BetaNextLife.png",
    "BETAAAAAAAAAAAAAAA": "/static/images/Bettttttaaaaa.png",
}

loading_phrases = [
    "trying to leave ohio...",
    "calculating mew streak...",
    "assessing chad qualities...",
    "queen never cry...",
    "looksmaxing...",
    "is this a jojo reference?...",
    "gooning...",
    "rizzing up...",
    "baby gronk is stopping by...",
    "kai cenat says hello...",
    "chat is this real?...",
    "i like my cheese drippy bruh...",
    "you hear about mr beast?...",
    "from the screen to the ring to the pen to the king ...",
    "pipipipipipipipipipipipi..."
]

def get_random_phrases():
    percentages = ["0%", "33%", "57%", "70%", "80%"]
    selected_phrases = random.sample(loading_phrases, len(percentages))
    return [f"{percentages[i]}... {selected_phrases[i]}" for i in range(len(percentages))]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    user_input = request.json.get("input", "")
    if not user_input:
        return jsonify({"error": "Input cannot be empty!"}), 400

    loading_messages = get_random_phrases()
    result = random.choice(list(results_with_images.keys()))
    image = results_with_images[result]

    return jsonify({
        "loading_messages": loading_messages,
        "result_text": result,
        "result_image": image
    })

if __name__ == "__main__":
    app.run(debug=True)
