## Save Tasks and there summary using sqlite via flask_restful api

from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

# Define request parser for incoming data
parser = reqparse.RequestParser()
parser.add_argument("task", type=str, help="Task is required", required=True)
parser.add_argument("summary", type=str, help="Summary is required", required=True)

# Define fields for marshalling
resource_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'summary': fields.String
}

# Define the database model
class ToDoDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    summary = db.Column(db.String(250), nullable=False)

# Define resource for the todo list
class ToDoList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return ToDoDB.query.all()
# Define resource for individual todo items
class ToDo(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_id):
        todo = ToDoDB.query.get(todo_id)
        if todo is None:
            abort(404, message="Task not found")
        return todo

    def post(self, todo_id):
        # Check if task already exists
        if ToDoDB.query.get(todo_id):
            abort(400, message="Task with this ID already exists")
        args = parser.parse_args()
        todo = ToDoDB(id=todo_id, task=args['task'], summary=args['summary'])  # Correct creation
        db.session.add(todo)
        db.session.commit()
        return {
            'id': todo.id,
            'task': todo.task,
            'summary': todo.summary
        }
    
    @marshal_with(resource_fields)
    def put(self, todo_id):
        args = parser.parse_args()
        todo=ToDoDB.query.filter_by(id=todo_id).first()
        if not todo:
            abort(404, message="Task not found")
        if args['task']:
            todo.task=args['task']
        if args['summary']:
            todo.summary=args['summary']
        db.session.commit()
        return todo
    
    def delete(self,todo_id):
        if todo:=ToDoDB.query.get(todo_id):
            db.session.delete(todo)
            return"Task Deleted"
        return "Task not Found"            
            


# Add resources to the API
api.add_resource(ToDoList, '/todo')
api.add_resource(ToDo, '/todo/<int:todo_id>')

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
