from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample diet plans based on goals
diet_plans = {
    "weight_loss": ["BREAK FAST: Oatmeal with fruits", "LUNCH: Grilled chicken salad", "DINNER: Steamed vegetables"],
    "muscle_gain": ["BREAK FAST: Egg omelette", "LUNCH: Chicken with quinoa", "DINNER: Peanut butter smoothie"],
    "balanced": ["BREAK FAST: Rice with lentils", "LUNCH: Mixed vegetable curry", "DINNER: Yogurt with nuts"],
    "Heart-Healthy":["BREAK FAST: Oats with walnuts","LUNCH: Grilled salmon with steamed broccoli","DINNER: Fresh fruit bowl"],
    "Detox-Diet-Plan":["BREAK FAST: Warm lemon water with honey","LUNCH: Grilled fish with avocado","DINNER: Herbal tea"],
    "Ayurveda-Diet-plan":["BREAK FAST: Warm ginger tea with honey","LUNCH: Brown rice with vegetable curry","DINNER: Dates & almonds"]
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_diet', methods=['POST'])
def get_diet():
    data = request.json
    goal = data.get("goal", "balanced")  
    diet = diet_plans.get(goal, diet_plans["balanced"])
    return jsonify({"diet_plan": diet})

if __name__ == '__main__':
    app.run(debug=True)
