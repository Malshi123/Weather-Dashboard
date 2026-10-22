from flask import Flask, request, jsonify, render_template
# Import the subprocess module to run shell commands 
import subprocess  
import os

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-weather', methods=['POST'])
def get_weather():
    data = request.json
    city_name = data.get('city', '')
    if not city_name:
        return jsonify({'error': 'City name is required'}), 400 

    # Run the shell command to get weather information
    try:
        # Use subprocess to call the weather command
        current_dir = os.path.dirname(os.path.abspath(__file__))
        process = subprocess.run(
            ['/Library/Java/JavaVirtualMachines/jdk-26.jdk/Contents/Home/bin/java', 'WeatherServer', city_name],
            capture_output=True,
            text=True,
            encoding='utf-8',
            cwd=current_dir
        )

        # Get the output from the java command
        java_output = process.stdout.strip()
        if not java_output:
            java_output = process.stderr.strip()  # Capture error output if any
    except Exception as e:
        java_output = f"Error: {str(e)}"
        return jsonify({"weather": java_output})

    # The received response is sent back to the HTML (front-end).
    
    return jsonify({"weather": java_output})

if __name__ == '__main__':
    app.run(debug=True,port=8080)

