# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:39:14 2023

@author: johan
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmr')
def bmr():
    return render_template('bmr.html')

@app.route('/tdee')
def tdee():
    return render_template('tdee.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')

@app.route('/to_burn')
def to_burn():
    return render_template('to_burn.html')

@app.route('/calculate_bmr', methods=['POST'])
def calculate_bmr():
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    age = int(request.form.get('age'))
    gender = int(request.form.get('gender'))

    bmr = 10 * weight + 6.25 * height - 5 * age + gender
    result = f"Your Basal Metabolic Rate is {bmr:.0f} kcal"
    
    return render_template('bmr.html', result=result)
@app.route('/calculate_tdee', methods=['POST'])
def calculate_tdee():
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    age = int(request.form.get('age'))
    gender = int(request.form.get('gender'))
    activity_level = float(request.form.get('activity_level'))

    tdee = (10 * weight + 6.25 * height - 5 * age + gender) * activity_level
    result = f"Your Total Daily Energy Expenditure is {tdee:.0f} kcal"
    
    return render_template('tdee.html', result=result)

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    

    bmi = weight / (height/100) ** 2
    result = f"Your Body Mass Index is {bmi:.1f}"
    
    return render_template('bmi.html', result=result)

@app.route('/calculate_ctb', methods=['POST'])
def calculate_ctb():
    jogging_constant = 60 / 70
    walking_constant = 55 / 70
    calories_to_burn = float(request.form.get('to_burn'))
    weight = float(request.form.get('weight'))
    jogging_weight_constant = jogging_constant * weight
    walking_weight_constant = walking_constant * weight
    jogging_distance = calories_to_burn / jogging_weight_constant
    walking_distance = calories_to_burn / walking_weight_constant
    
    result = f"To burn {calories_to_burn:.0f} calories, you need to jog\
        {jogging_distance:.1f} km or power walk {walking_distance:.1f} km!"
    
    return render_template('to_burn.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)
