from flask import Flask, request, jsonify
from helper.moviesRecommendation import recommendMovies
from helper.userSentiments import getEmotionsList

app = Flask(__name__)

@app.route('/')
def test():
    response_data = {'message': "API is up and running..."}
    return jsonify(response_data)

@app.route('/movies/basedOnUserText', methods=['POST'])
def recommendMoviesBasedOnUserText():
    data = request.get_json()
    emotions = getEmotionsList(data['user_response'])
    emotion = max(emotions, key=emotions.get).strip()
    movies = recommendMovies(emotion)
    response_data = {'movies': movies}
    return jsonify(response_data)

@app.route('/movies/basedOnUserEmotion', methods=['POST'])
def recommendMoviesBasedOnUserEmotion():
    data = request.get_json()
    movies = recommendMovies(data['user_response'])
    response_data = {'movies': movies}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)