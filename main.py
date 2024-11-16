#here is an example coding platform for python

# Updated Recommended Daily Amounts (RDA) for a 2000 Calorie Diet
rda = {
    "calories_100g": 2000,
    "proteins_100g": 50,
    "fat_100g": 70,
    "sat_fat_100g": 20,
    "insat_fat_100g": 40,
    "carbs_100g": 300,
    "sugars_100g": 25,
    "fibers_100g": 30,
    "cholesterol_100g": 300,
    "iron_100g": 18,
    "calcium_100g": 1000,
    "vitamin_c_100g": 90,
    "vitamin_b9_100g": 400,
    "omega_3_100g": 1.6,
    "omega_6_100g": 17,
    "sodium_100g": 2300,
    "magnesium_100g": 400,
    "vitamin_a_retinol_100g": 900,
    "vitamin_d_100g": 20,
    "vitamin_e_100g": 15,
    "vitamin_k1_100g": 120,
    "zinc_100g": 11,
    "copper_100g": 0.9,
    "manganese_100g": 2.3,
    "selenium_100g": 55,
    "iodine_100g": 150,
    "chromium_100g": 35,
    "molybdenum_100g": 45,
}

# Nutritional data for the food item
nutritional_data = {
    "calories_100g": 0.0,
    "proteins_100g": 0.0,
    "fat_100g": 0.0,
    "sat_fat_100g": 0.411,
    "insat_fat_100g": 0.965,
    "carbs_100g": 0.0,
    "sugars_100g": 0.0,
    "fibers_100g": 0.0,
    "cholesterol_100g": 0.0294,
    "iron_100g": 0.000946,
    "calcium_100g": 0.0194,
    "vitamin_c_100g": 0.0,
    "vitamin_b9_100g": 9.2e-06,
    "omega_3_100g": 0.01209,
    "omega_6_100g": 0.205,
    "sodium_100g": 0.0406,
}

# Normalize and calculate the score using updated RDA values
def calculate_nutritional_score(data, weights, rda):
    score = 0
    for nutrient, weight in weights.items():
        value = data.get(nutrient, 0)
        recommended = rda.get(nutrient, 1)  # Avoid division by zero
        normalized = value / recommended
        score += weight * normalized
    return score

# Define nutrient weights (for example, positive and negative weightings)
weights = {
    "calories_100g": 0.2,
    "proteins_100g": 0.3,
    "fat_100g": -0.2,
    "sat_fat_100g": -0.3,
    "insat_fat_100g": 0.1,
    "carbs_100g": 0.1,
    "sugars_100g": -0.4,
    "fibers_100g": 0.3,
    "cholesterol_100g": -0.2,
    "iron_100g": 0.2,
    "calcium_100g": 0.2,
    "vitamin_c_100g": 0.15,
    "vitamin_b9_100g": 0.1,
    "omega_3_100g": 0.2,
    "omega_6_100g": 0.1,
    "sodium_100g": -0.3,
}

# Compute the score
nutritional_score = calculate_nutritional_score(nutritional_data, weights, rda)
print(f"Nutritional Score: {nutritional_score:.2f}")

