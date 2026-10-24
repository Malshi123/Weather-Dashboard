# 🌤️ 3-Language Weather Dashboard

A simple and interactive Weather Dashboard application built by integrating three different programming environments: **HTML (Front-end)**, **Python Flask (Backend API)**, and **Java (Core Logic)**.

## 🛠️ Tech Stack
* **Front-end:** HTML5 & CSS3 (Clean, responsive user interface)
* **Backend API:** Python Flask (Handles HTTP requests and serves as a bridge)
* **Core Logic:** Java / OpenJDK (Executes background processes to retrieve data)

## 📂 Project Structure
* `index.html` - The user interface containing the search box, styling, and fetch requests.
* `app.py` - The Flask web server that handles API routing and runs the Java sub-process.
* `WeatherServer.java` - The standalone Java program that processes input parameters and evaluates weather conditions using case-insensitive logic.
* `WeatherServer.class` - The compiled Java bytecode executed dynamically by Python.

## 🚀 How to Run Locally

### Prerequisites
Make sure you have **Python 3** and **Java JDK** installed on your machine.

### Step-by-Step Setup
1. Clone or download this project folder.
2. Open your terminal inside the project directory and install Flask:
   ```bash
   pip install flask
   ```
3. Compile the Java file to generate the bytecode:
   ```bash
   javac WeatherServer.java
   ```
4. Start the Python backend server:
   ```bash
   python3 app.py
   ```
5. Open your web browser and navigate to:
   ```text
   http://127.0.0.1:8080
   ```
6. Enter a city name (e.g., `colombo`, `kandy`, `galle`, or `kaluthara`) and click **Get Weather** to see the live dynamic response from the Java core!
