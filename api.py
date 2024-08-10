from flask import Flask, request, jsonify

app = Flask(__name__)

# Variable global para almacenar el último valor recibido por POST
last_trash_type = {"type": "Organico", "imageName": "leaf.fill"}

@app.route('/api/trash_type', methods=['GET','POST'])
def receive_trash_type():
    global last_trash_type
    if request.method == 'GET':
        # Retornar el último valor recibido por POST
        return jsonify(last_trash_type), 200

    elif request.method == 'POST':
        # Recibir datos JSON del cuerpo de la solicitud
        data = request.get_json()
        trash_type = data.get('type')
        image_map = {
            "Organico": "leaf.fill",
            "Inorganico": "trash.fill"
        }
        image_name = image_map.get(trash_type, "unknown")
        if trash_type in image_map:
            last_trash_type = {"type": trash_type, "imageName": image_name}
            print(f"Received trash type: {trash_type}")
            print(last_trash_type)
            return jsonify(last_trash_type), 200
        else:
            print(f"Received trash type: {trash_type}")
            return jsonify({"status": "error", "message": "Invalid trash type"}), 400
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)