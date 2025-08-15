from flask import Flask, jsonify, request
app = Flask(__name__)

planets = {
    "Mercury": {
        "id": 1,
        "radius_km": 2439.7,
        "mass_kg": 3.3011e23,
        "gravity_m_s2": 3.7,
        "composition_1":"Oxygen",
        "composition_2":"Sodium",
        "composition_3":"Hydrogen",
        "composition_4":"Helium",
        "composition_5":"Potassium",
        "temperature_in_F":332,
        "temperature_in_C":167,
        "position": {"x": 57.9, "y": 0}  # distância média do Sol em milhões de km
    },
    "Venus": {
        "id": 2,
        "radius_km": 6051.8,
        "mass_kg": 4.8675e24,
        "gravity_m_s2": 8.87,
        "composition_1":"Carbon Dioxide",
        "composition_2":"Nitrogen",
        "temperature_in_F":867,
        "temperature_in_C":464,
        "position": {"x": 108.2, "y": 0}
    },
    "Earth": {
        "id": 3,
        "radius_km": 6371,
        "mass_kg": 5.97237e24,
        "gravity_m_s2": 9.807,
        "composition_1":"Oxygen",
        "composition_2":"Nitrogen",
        "composition_3":"Argon",
        "composition_5":"Carbon Dioxide",
        "temperature_in_F":59,
        "temperature_in_C":15,
        "position": {"x": 149.6, "y": 0}
    },
    "Mars": {
        "id": 4,
        "radius_km": 3389.5,
        "mass_kg": 6.4171e23,
        "gravity_m_s2": 3.721,
        "composition_1":"Carbon Dioxide",
        "composition_2":"Nitrogen",
        "composition_3":"Argon",
        "temperature_in_F":-76,
        "temperature_in_C":-60,
        "position": {"x": 227.9, "y": 0}
    },
    "Jupiter": {
        "id": 5,
        "radius_km": 69911,
        "mass_kg": 1.8982e27,
        "gravity_m_s2": 24.79,
        "composition_1":"Hydrogen",
        "composition_2":"Helium",
        "temperature_in_F":-231,
        "temperature_in_C":-145,
        "position": {"x": 778.5, "y": 0}
    },
    "Saturn": {
        "id": 6,
        "radius_km": 58232,
        "mass_kg": 5.6834e26,
        "gravity_m_s2": 10.44,
        "composition_1":"Hydrogen",
        "composition_2":"Helium",
        "temperature_in_F":-288,
        "temperature_in_C":-178,
        "position": {"x": 1434, "y": 0}
    },
    "Uranus": {
        "id": 7,
        "radius_km": 25362,
        "mass_kg": 8.6810e25,
        "gravity_m_s2": 8.69,
        "composition_1":"Hydrogen",
        "composition_2":"Helium",
        "composition_3":"Methane",
        "temperature_in_F":-324,
        "temperature_in_C":-197,
        "position": {"x": 2871, "y": 0}
    },
    "Neptune": {
        "id": 8,
        "radius_km": 24622,
        "mass_kg": 1.02413e26,
        "gravity_m_s2": 11.15,
        "composition_1":"Hydrogen",
        "composition_2":"Helium",
        "composition_3":"Methane",
        "temperature_in_F":-334,
        "temperature_in_C":-201,
        "position": {"x": 4495, "y": 0}
    }
}

@app.route("/planets_info")

def get_planet_info():
    return jsonify(planets)

@app.route("/planets_info/<int:id>")
def get_planet_info_by_id(id):
    for name, planet in planets.items():
        if planet["id"] == id:
            return jsonify({name:planet})
    return jsonify({"error": "Planet not found"}), 404
if __name__ == "__main__":
    app.run(port=5000,host='localhost', debug=True)
