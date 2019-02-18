from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('index.html')


@app.route("/about")
def about():
	return render_template('about.html')


@app.route("/reiki_levels/level_1")
def level_1():
	return render_template('level_1.html')


@app.route("/reiki_levels/level_2")
def level_2():
	return render_template('level_2.html')


@app.route("/reiki_levels/level_3")
def level_3():
	return render_template('level_3.html')


@app.route("/bracelets/men")
def men():
	return render_template('men.html')


@app.route("/women")
def women():
	return render_template('women.html')


@app.route("/couple")
def couple():
	return render_template('couple.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
	return render_template('register.html')


@app.route("/login")
def login():
	return render_template('login.html')


@app.route("/contact-us")
def contact():
	return render_template('contact.html')


if __name__ == '__main__':
	app.run(debug=True)	
