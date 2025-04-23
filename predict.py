# predict.py

def predict_rainfall(temp, humidity):
    if temp < 20 and humidity > 70:
        return "Rain Likely"
    else:
        return "No Rain"
