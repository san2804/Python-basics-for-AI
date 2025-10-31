import pandas as pd

data = {
    "Name": ["Asha", "Nimal", "Ravi", "Kavya", "Lahiru", "Maya", "Nuwan"],
    "Math": [85, 67, 90, 45, 78, 88, 62],
    "Science": [92, 60, 88, 50, 80, 95, 55],
    "English": [75, 58, 85, 40, 72, 90, 60]
}

df = pd.DataFrame(data)
print(df)
