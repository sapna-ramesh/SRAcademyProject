from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
	my_friends = {'sapna' : 61}
	return render_template('me.html', my_friends=my_friends)
	
@app.route('/login')
def login():
	return render_template('index.html',


if __name__ == "__main__":
	app.run()