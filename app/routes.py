from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)
tasks = []

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template('index.html', tasks=tasks)
