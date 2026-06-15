from flask import Flask, render_template, request, jsonify
from datetime import datetime
from models import db, Event, Task, Reminder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400

    events = Event.query.filter_by(date=selected_date).all()
    tasks = Task.query.filter_by(date=selected_date).all()
    reminders = Reminder.query.filter_by(date=selected_date).all()

    sessions = {
        'events': [e.to_dict() for e in events],
        'tasks': [t.to_dict() for t in tasks],
        'reminders': [r.to_dict() for r in reminders]
    }

    return jsonify(sessions)

if __name__ == '__main__':
    app.run(debug=True)
