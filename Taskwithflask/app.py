from flask import Flask,render_template,url_for,request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow) 
    
    def __repr__(self):
        return '<task %r>' % self.id
    

@app.route('/', methods=['POST', 'GET'])
def add():
    if request.method == 'POST': 
        task_content=request.form['usr']
        new_task=Task(task=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception:
            return"An issue occurred adding your task"
    else:
        tasks=Task.query.order_by(Task.date_created).all()
        return render_template('index.html', tasks=tasks)
    
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete=Task.query.get_or_404(id )
    try:
        db.session.delete(task_to_delete)
        db.session.commit() 
        return redirect('/')
    except Exception:
        return "Error deleting task"
    
@app.route('/update/<int:id>', methods=["GET","POST"])
def update(id): 
    task1=Task.query.get_or_404(id )
    if request.method =='POST':
        task1.task=request.form['usr']
        try:
            db.session.commit()
            return redirect('/')
        except Exception:
            return "Error updating your task"
    else:
        return render_template('update.html',task=task1)
    

if __name__=="__main__":
    app.run(debug=True)
    