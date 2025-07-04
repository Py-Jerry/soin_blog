from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    # 打开'./templates/index.html'
    return render_template('home.html')
@app.route('/blog')
def bolg():  # put application's code here
    # 打开'./templates/index.html'
    return render_template('blog.html')



if __name__ == '__main__':
    app.run()
