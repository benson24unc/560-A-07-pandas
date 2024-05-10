#https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player_data = {
    "Last Name": ["Davis", "Trimble", "Lebo"],
    "First Name": ["RJ", "Seth", "Creighton"],
    "Height": [72, 75, 73], 
    "Weight": [180, 195, 180]  
}

data = pd.DataFrame(player_data)


data["BMI"] = (data["Weight"] / 2.205) / ((data["Height"] * 0.0254) ** 2)


print(data)

data.to_csv("bmi.csv")
