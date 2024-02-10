from flask import Flask, request, jsonify
from models.task import Task



app = Flask(__name__)


tasks = []
task_id_control = 1


@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    
    data = request.get_json()
    
    new_task = Task(id=task_id_control ,title=data["title"], description=data.get("description", ""))
    
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({
        "message": "Nova tarfa criada com sucesso"
    })
        
    
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks":task_list,
        "total_tasks": len(task_list)  
    }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message":"tarefa nao encontrada"}), 404
    
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if task == None:
        return jsonify({"Esta tarefa nao goi encontrada "}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completedd = data['completed']
    
    return jsonify({"message ": "Tarefa atualizada"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
            
    if not task:
        return jsonify({"message":"Esta tarefa nao goi encontrada ou ja foi removida"}), 404
    
    tasks.remove(task)
    return jsonify({"message ": "Tarefa removida "})

if __name__ == "__main__":
    app.run(debug=True)

