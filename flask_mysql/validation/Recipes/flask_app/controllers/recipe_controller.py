from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_app import app 
from flask import render_template, redirect, request, session ,flash
from datetime import date



@app.route('/delete/<int:id>')
def delete_recipe(id):
    print(id)
    data  = {
        'id':id
    }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def display_edit_recipe(id):
    if session:
       
        data = {
            'id':id
        }
        recipe = Recipe.get_one_by_id(data)
        return render_template('edit_recipe.html', recipe = recipe)
    return redirect('/register')

@app.route('/recipes/new')
def display_add_recipe():
    if session:
        data = {
            'email' : session['user_email']
        }
        user = User.get_one_by_email_obj(data)
        return render_template('add_new_recipe.html', user = user)
    return redirect ('/register')

@app.route('/recipes/<int:id>')
def display_recipe(id):
    if session:
        data = {
                'email' : session['user_email']
            }
        user = User.get_one_by_email_obj(data)
        data = {
            'id':id
        }
        recipe = Recipe.get_one_by_id(data)
        return render_template('view_recipe.html', recipe = recipe, user=user)
    return redirect('/register')

@app.route('/create/recipe', methods =['POST'])
def create_recipe():
    if request.form['date_made'] == "":
        flash("YOU MUST ENTER A DATE","recipe_date")
        return redirect ('/recipes/new')
    if Recipe.validate_recipe(request.form) == False:
        return redirect ('/recipes/new')
    else:
        Recipe.create_recipe(request.form)
        return redirect('/dashboard')

@app.route('/edit/recipe', methods = ['POST'])
def edit_recipe():
    num = request.form['id']
    if Recipe.validate_recipe(request.form) == False:
        return redirect (f'/recipes/edit/{num}')
    else:
        Recipe.edit_recipe(request.form)
        return redirect('/dashboard')