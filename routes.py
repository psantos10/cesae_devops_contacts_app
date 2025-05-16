from flask import render_template, request, redirect, make_response
from models import Contact

def register_routes(app, db):
    @app.route('/')
    def index():
        contacts = Contact.query.all()
        return render_template('index.html', contacts=contacts)

    @app.route('/novo-contacto', methods=('GET', 'POST'))
    def create():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')

            # Criar nova instancia de Contact
            contact = Contact(name=name, email=email, phone=phone)

            # Salvar no banco de dados
            db.session.add(contact)
            db.session.commit()

            return redirect('/')

        return render_template('new.html')

    @app.route('/editar-contacto/<id>', methods=('GET', 'POST'))
    def update(id):
        contact = Contact.query.get(id)

        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')

            # Atualizar o objecto contact
            contact.name = name
            contact.email = email
            contact.phone = phone

            # Persistir o objeto contact
            db.session.commit()

            return redirect('/')

        return render_template('edit.html', contact=contact)

    @app.route('/eliminar-contacto/<id>', methods=('POST',))
    def delete(id):
        if request.method == 'POST':
            contact = Contact.query.get(id)

            if contact is None:
                response = make_response()
                response.status_code = 404

                return response
            else:
                db.session.delete(contact)
                db.session.commit()

                return redirect('/')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', error_code=404), 404
