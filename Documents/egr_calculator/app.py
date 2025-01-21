from flask import Flask, request, render_template
import math

app = Flask(__name__)

def calculate_egr(crank_length, front_teeth, rear_teeth, tire_diameter):
    # Calculate gear ratio
    gear_ratio = front_teeth / rear_teeth

    # Convert tire diameter to meters if given in inches
    tire_diameter_m = tire_diameter * 0.0254

    # Calculate tire circumference
    tire_circumference = math.pi * tire_diameter_m

    # Calculate distance traveled per pedal stroke
    distance_traveled = tire_circumference * gear_ratio

    # Calculate Effective Gear Ratio (EGR)
    egr = distance_traveled / (crank_length / 1000)  # Convert crank length to meters

    return {
        "gear_ratio": gear_ratio,
        "tire_circumference": tire_circumference,
        "distance_traveled": distance_traveled,
        "egr": egr
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    crank_length = float(request.form['crank_length'])
    front_teeth = int(request.form['front_teeth'])
    rear_teeth = int(request.form['rear_teeth'])
    tire_diameter = float(request.form['tire_diameter'])

    results = calculate_egr(crank_length, front_teeth, rear_teeth, tire_diameter)

    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

