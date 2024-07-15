import pandas as pd

# Sample data for the Titanic dataset
data = {
    'PassengerId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    'Pclass': [3, 1, 3, 1, 3, 3, 1, 3, 3, 2],
    'Name': [
        'Braund, Mr. Owen Harris', 
        'Cumings, Mrs. John Bradley (Florence Briggs Thayer)', 
        'Heikkinen, Miss. Laina', 
        'Futrelle, Mrs. Jacques Heath (Lily May Peel)', 
        'Allen, Mr. William Henry', 
        'Moran, Mr. James', 
        'McCarthy, Mr. Timothy J', 
        'Palsson, Master. Gosta Leonard', 
        'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)', 
        'Nasser, Mrs. Nicholas (Adele Achem)'
    ],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'male', 'female', 'female'],
    'Age': [22, 38, 26, 35, 35, None, 54, 2, 27, 14],
    'SibSp': [1, 1, 0, 1, 0, 0, 0, 3, 0, 1],
    'Parch': [0, 0, 0, 0, 0, 0, 0, 1, 2, 0],
    'Ticket': ['A/5 21171', 'PC 17599', 'STON/O2. 3101282', '113803', '373450', '330877', '17463', '349909', '347742', '237736'],
    'Fare': [7.25, 71.2833, 7.925, 53.1, 8.05, 8.4583, 51.8625, 21.075, 11.1333, 30.0708],
    'Cabin': [None, 'C85', None, 'C123', None, None, 'E46', None, None, None],
    'Embarked': ['S', 'C', 'S', 'S', 'S', 'Q', 'S', 'S', 'S', 'C']
}

# Create a DataFrame
titanic = pd.DataFrame(data)

# Save the DataFrame to an Excel file with a specific sheet name
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

print("titanic.xlsx file has been created.")
