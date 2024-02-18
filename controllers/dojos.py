from __init__ import app

from flask import redirect,request,render_template,redirect

from models.dojo import Dojo
from models.ninja import Ninja

@app.route('/dojos')
def display_dojos():
    return render_template('dojos.html',dojos=Dojo.show())

@app.route('/ninjas')
def display_create_ninjas():
    return render_template("ninjas.html",dojos=Dojo.show())

@app.route('/create',methods=['POST'])
def create():
    Ninja.save(request.form)
    return redirect('/ninjas')

@app.route('/dojos/<int:id>')
def dojos_ninjas_display(id):
    data={
        'id':id,
    }
    return render_template('dojo_show.html',dojo=Dojo.ninjas_dojos(data))

