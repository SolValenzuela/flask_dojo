from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request


@app.route('/')
def index():
    return redirect ('/dojos')


@app.route('/dojos')
def dojos():
    return render_template('dojos.html', all_dojos=Dojo.get_all())


@app.route('/dojos/process' ,methods=['POST'])
def process_new_dojo():
    print(request.form)
    data={
        'name':request.form['name']
    }
    new_dojo=Dojo.add_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojo_details(id):
    data={
        'dojo_id': id
    }
    dojos_ninjas=Dojo.get_dojos_y_ninjas(data)
    return render_template('dojo_details.html', dojo=dojos_ninjas)