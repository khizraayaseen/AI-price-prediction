from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('cloth.pkl', 'rb'))

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    brand = request.form['brand']
    category = request.form['category']
    color = request.form['color']
    size = request.form['size']
    material = request.form['material']
    if brand=='New Balance':
        brand=0
    elif brand=='Under Armour':
        brand=1
    elif brand=='Nike':
        brand=2
    elif brand=='Adidas':
        brand=3
    elif brand=='Reebok':
        brand=4
    elif brand=='Puma':
        brand=5
    
    if category=='Dress':
        category=0
    elif category=='Jeans':
        category=1
    elif category=='Shoes':
        category=2
    elif category=='Sweater':
        category=3
    elif category=='Jacket':
        category=4
    elif category=='T-shirt':
        category=5

    if color=='White':
        color=0
    elif color=='Black':
        color=1
    elif color=='Red':
        color=2
    elif color=='Green':
        color=3
    elif color=='Yellow':
        color=4
    elif color=='Blue':
        color=5

    if size=='XS':
        size=0
    elif size=='S':
        size=1
    elif size=='M':
        size=2
    elif size=='L':
        size=3
    elif size=='XL':
        size=4
    elif size=='XXL':
        size=5

    if material=='Nylon':
        material=0
    elif material=='Silk':
        material=1
    elif material=='Wool':
        material=2
    elif material=='Cotton':
        material=3
    elif material=='Polyester':
        material=4
    elif material=='Denim':
        material=5
    arr = np.array([[brand, category, color, size, material]])
    new_data_df = pd.DataFrame(arr, columns=['Brand', 'Category', 'Color', 'Size', 'Material'])
    # pred = lin_reg_model.predict(new_data_df)
    pred = model.predict(new_data_df)
    print(pred)
    return render_template('home.html', data=pred[0], prediction_made=True)

if __name__ == "__main__":
    app.run(debug=True)