from flask import Flask, render_template, request, redirect, url_for
from hinterlands import generate_contract

app = Flask(__name__)

@app.route('/contract')
def contract():
    contract_values=generate_contract()
    print(contract_values)
    return render_template(
        'contract.html',
        contract_values=contract_values
        )
