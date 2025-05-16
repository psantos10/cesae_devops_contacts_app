from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/novo-contacto', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        # Here you would typically save the contact to a database
        return render_template('new.html', name=name, email=email, phone=phone)

    return render_template('new.html')

@app.route('/editar-contacto/<contact_id>', methods=('GET', 'PUT'))
def update(contact_id):
    if request.method == 'PUT':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        # Here you would typically update the contact in a database
        return render_template('edit.html', contact_id=contact_id, name=name, email=email, phone=phone)

    return render_template('edit.html', contact_id=contact_id)

@app.route('/eliminar-contacto/<contact_id>', methods=('GET', 'DELETE'))
def delete(contact_id):
    if request.method == 'DELETE':
        # Here you would typically delete the contact from a database
        return render_template('delete.html', contact_id=contact_id)

    return render_template('delete.html', contact_id=contact_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
