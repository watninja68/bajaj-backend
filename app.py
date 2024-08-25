from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl_endpoint():
    if request.method == 'POST':
        try:
            data = request.json
            input_array = data.get('data', [])
            aa = ""
            for i in input_array:
                aa += i
            # Process the array items as strings
            aa.split(":")[-1].split(",")
            bb = []
            for i in aa:
                bb.append(i.replace("\"",""))
            # Extract alphabets and numbers
            bb = bb[10:]
            numbers = [int(item) for item in bb if re.match(r'\d', item)]
            alphabets = [str(item) for item in bb if re.match(r'[a-zA-Z]', item)]
            # print(numbers,alphabets)
            # Find the highest alphabet (case-insensitive)
            highest_alphabet =  max((x for x in alphabets if x.islower()), default=None)

            response = {
                "is_success": True,
                "user_id": "Karneeshkar",  
                "email": "karneeshkar68@gmail.com",  
                "roll_number": "21BLC1591",  
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowecase_alphabet": [highest_alphabet] if highest_alphabet else []
            }
            
            return jsonify(response), 200
        
        except Exception as e:
            return jsonify({"is_success": False, "error": str(e)}), 400
    
    elif request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
