from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/form', methods=['GET'])
def get_form():
    form_structure = {
        "fields": [
            {"type": "text", "label": "Name", "key": "name", "required": True},
            {"type": "email", "label": "Email", "key": "email", "required": True},
            {"type": "number", "label": "Age", "key": "age", "required": False},
             {"type": "email", "label": "Email", "key": "email", "required": True},
            {"type": "number", "label": "Age", "key": "age", "required": False},
             {"type": "email", "label": "Email", "key": "email", "required": True},
            {"type": "number", "label": "Age", "key": "age", "required": False},
             {"type": "email", "label": "Email", "key": "email", "required": True},
            {"type": "number", "label": "Age", "key": "age", "required": False},
        ]
    }
    return jsonify(form_structure)

if __name__ == '__main__':
    app.run(debug=True)
