from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initialize an empty list to store To Do items
todo_list = []


@app.route('/')
def view_todo_list():
    return render_template('index.html', todo_list=todo_list)


@app.route('/submit', methods=['POST'])
def submit_todo():
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')

    # Data validation
    if not email or '@' not in email:
        return redirect('/')

    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # If validation passes, add the new To Do item to the list
    todo_list.append({'task': task, 'email': email, 'priority': priority})

    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear_todo_list():
    # Clear the list
    todo_list.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
