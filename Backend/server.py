from flask import Flask, request, jsonify
import products_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')    
    return response

@app.route('/getUom' , methods=['GET'])
def get_uom():
    response = uom_dao.get_uom(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    product_id = request.form['product_id']
    response = products_dao.delete_product(connection, product_id)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)