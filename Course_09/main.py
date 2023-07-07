from flask import Flask, jsonify, request

app = Flask(__name__)

todos = ["Buy groceries", "Feed the cat", "Wash clothes"]


@app.route("/")
def index():
    return "Hello, Flask!"


@app.route("/todos", methods=["GET"])
def get_all_todos():
    response = {}
    counter = 0
    for t in todos:
        response[counter] = t
        counter += 1
    return jsonify(response)


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    if 0 <= todo_id < len(todos):
        return jsonify(todos[todo_id])
    else:
        return jsonify("Invalid id"), 400


@app.route("/todos", methods=["POST"])
def add_todo():
    todo = request.json
    todos.append(todo)
    return jsonify({"id": len(todos)-1}), 201


@app.route("/todos", methods=["PUT"])
def edit_todo():
    id = request.args.get("id")
    todo_id = int(id)
    if 0 <= todo_id < len(todos):
        todo = request.json
        todos[todo_id] = todo
        return "", 204
    else:
        return jsonify("Invalid id"), 400


@app.route("/todos", methods=["DELETE"])
def delete_todo():
    id = request.args.get("id")
    todo_id = int(id)
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
        return "", 200
    else:
        return jsonify("Invalid id"), 400


if __name__ == '__main__':
    app.run(port=9990, debug=True)
