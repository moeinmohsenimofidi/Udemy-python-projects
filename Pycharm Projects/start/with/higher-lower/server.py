from flask import Flask
import random

random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style = 'text-align = center'>Guess a number between 0 and 9 </h1>" \
           '<img src = "https://media1.giphy.com/media/UDU4oUJIHDJgQ/200w.webp?cid=ecf05e47mlj1eux7vdl4u3k5yakqpjejggcbvnbsejps34x4&rid=200w.webp&ct=g">'

@app.route("/<int:guess>")
def guess_number(guess):
        if guess > random_number:
            return "<h1 style= 'color: red'>Too high,try again.</h1>"\
                   "<img src='https://media4.giphy.com/media/3orieYSIw6FQMsmFQQ/200w.webp?cid=ecf05e47c2f101hivnqg7xuguho5p7l431lxbqoust9a42g1&rid=200w.webp&ct=g width:200'>"
        elif guess < random_number:
            return "<h1 style= 'color: purple'>Too low,try again.</h1>"\
            "<img src='https://media1.giphy.com/media/RJo6Uas77p4zzcEj5I/200.webp?cid=ecf05e4791w2me6ildhbnohwatwgts28rr4lsk73qkf02eh0&rid=200.webp&ct=g width:200'>"

        else :
            return "<h1 style='color: yellow'> You found me</h1>"\
                   "<img src='https://media4.giphy.com/media/BPJmthQ3YRwD6QqcVD/200w.webp?cid=ecf05e47v1zn7crz4sybxp71tqmx9peafoa4835lmbon7ib6&rid=200w.webp&ct=g'>"


if __name__ == "__server__":
    app.run(debug=True)



