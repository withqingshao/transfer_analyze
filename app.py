from flask import Flask,request
import pandas as pandas
from flask_cors import *
import json

app = Flask(__name__)
app.debug=True
CORS(app, resources=r'/*')

@app.route('/read')
def readData():
    url=request.args.get("url")
    type=request.args.get("type")
    print(url)
    if type=="json":
        res=pandas.read_json(url)
    if type=="csv":
        res=pandas.read_csv(url)
    result=res.to_json(orient='table')
    product_dic = json.loads(result)
    print(product_dic)
    #print(product_dic["data"])
    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8082)