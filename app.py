from flask import Flask, render_template, request

from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
from pprint import pprint

app = Flask(__name__)

# model_path = "./model/entity_vector.model.bin"
model_path = "/Users/tatsu/Desktop/geek/product/model/word2vec.gensim.model"

# model = KeyedVectors.load_word2vec_format(model_path, binary=False)
model = Word2Vec.load(model_path)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/mode1')
def mode1():
    return render_template('mode1_1.html')


@app.route('/mode1', methods=["post"])
def m1_post():
    word = request.form["word"]
    if word in model.wv:
        sim_word = model.most_similar(word)
        return render_template('mode1_2.html', word=word, sim_word=sim_word)
    else:
        return render_template('error.html')


@app.route('/mode2')
def mode2():
    return render_template('mode2_1.html')


@app.route('/mode2', methods=["post"])
def m2_post():
    word1 = request.form["word1"]
    word2 = request.form["word2"]
    if (word1 in model.wv) and (word2 in model.wv):
        sim = model.similarity(word1, word2)
        return render_template('mode2_2.html', word1=word1, word2=word2, sim=sim)
    else:
        return render_template('error.html')


@app.route('/mode3')
def mode3():
    return render_template('mode3_1.html')


@app.route('/mode3', methods=["post"])
def m3_post():
    pos = request.form["pos"]
    neg = request.form["neg"]
    pos = list(pos.split(sep=","))
    neg = list(neg.split(sep=","))
    try:
        ans = model.most_similar(positive=pos, negative=neg)
        return render_template('mode3_2.html', pos=pos, neg=neg, ans=ans)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)
