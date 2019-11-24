from flask import Flask, render_template
from fibonacci import fibonacci
from time import sleep
app = Flask(__name__)


@app.route('/')
def index():
	ans = fibonacci(80)
	return render_template('fib.html', number_list=ans)


if __name__ == '__main__':
	app.run(debug=True)