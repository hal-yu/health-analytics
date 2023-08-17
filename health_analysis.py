import pandas as pd
import numpy as np

# Number Variable
Five = 5

# String Variable
String = "String"

# List
List = [1, 2, 3, 4,5]

# Dictionary
Yu_Dictionary = {
    "FirstName": "Haley",
    "LastName": "Yu",
    "age": 23,
    "contacts": ["haley.yu@stonybrook.edu", "718-718-0718"],
    "address": {
        "Country": "United States",
        "State": "New York",
        "County": "Queeens",
        "Zip Code": "10000"
    }
}

# Function
def gradePointAverage(HHA506, HHA503):
    # Check Research GPA First
    if HHA506 >= 93:
        HHA506_output = 'good'
    else:
        HHA506_output = 'bad'
    # Check HIPAA GPA Second
    if HHA503 >= 93:
        HHA503_output = 'good'
    else:
        HHA503_output = 'bad'
    output = [HHA506_output, HHA503_output]
    return output
    
HHA506Input = 94
HHA503Input = 92

function_output = gradePointAverage(HHA506Input, HHA503Input)

print('HHA 506 GPA: ', HHA506Input)
print('HHA506 Interpretation: ', function_output[0])
print('HHA 503 GPA: ', HHA503Input)
print('HHA503 Interpretation: ', function_output[1])