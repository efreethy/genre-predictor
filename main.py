# Consumes a dataset of people (strictly formatted) and predicts how strongly they
# associate across 4 different genres

# Accepts input file formats (csv|tsv) and supports output formats (csv|tsv|json)

# Input:
#   Dataset of people
# Output:
#   Same dataset, populated with predicted genre information
# USAGE (at the command line)
#  params:
#    input-filename=<name>                      Input file must live in same dir. as main.py
#    output-filename=<my-output-filename>
#    output-format=(csv|tsv|json)
#
#  python main.py input-filename=<name>.(csv|tsv) output-filename=<my-output-filename> output-format=(csv|tsv|json)

# Example
#  python main.py input-filename=test_data.csv output-filename=bestresults output-format=tsv

# created by efreethy on 05/18/17
import json
import sys
import csv
import numpy as np
import pickle
from sklearn.externals import joblib

clf = joblib.load('genre_regression.pkl')

inputFilename = ''
outputFilename = 'results'
outputFormat = 'csv'
inputDelimiter = outputDelimiter = ','

# ---- Evaluate command line arguments
for arg in sys.argv:
    items = arg.split('=')
    param = items[0]
    value = len(items) > 1 and items[1]

    if (param=='input-filename'):
        inputFilename = value
    if (param=='input-filename' and value.lower().endswith(('.tsv'))):
        inputDelimiter='\t'

    if (param=='output-format' and value=='json'):
        outputFormat = 'json'
    elif (param=='output-format' and value=='tsv'):
        outputFormat = 'tsv'
        outputDelimiter = '\t'

    if (param=='output-filename'):
        outputFilename=value


# ---- Main
with open(inputFilename) as file:
    print 'input delimiter: '+ inputDelimiter
    reader = csv.reader(file, delimiter = inputDelimiter)
    next(reader)
    observations = np.array(list(reader))

# converts array of strings to floats
observations = [[float(value) for value in observation] for observation in observations]
# extracts all independentObservations (columns 5-23) for this particular data set
independentObservations = [np.array(row[5:]).reshape(1, -1) for row in observations]
# computes predictions using sci-kit multivariate regression model
predictions = [clf.predict(row) for row in independentObservations]

# transform original file into an array
with open(inputFilename) as file:
    reader = csv.reader(file, delimiter = inputDelimiter)
    original = np.array(list(reader))
# takes predictions and writes them into the original dataset
for index, row in enumerate(original[1:]):
    row[1:5] = predictions[index]

# if output requested is csv or tsv, deliver in this format
if (outputFormat=='csv' or outputFormat=='tsv'):
    print outputFilename+"."+outputFormat
    np.savetxt(outputFilename+"."+outputFormat, original, fmt='%5s',delimiter=outputDelimiter)
elif(outputFormat=='json'):
    # if output requested is json, format predictions into json objects then dump into file
    mappedObjects=[]
    for index, row in enumerate(original[1:]):
        observation = { }
        for j, header in enumerate(original[0]):
            observation[header] = original[index+1][j]
            mappedObjects.append(observation)
    with open(outputFilename+"."+outputFormat, 'w') as f:
        f.truncate()
        json.dump(mappedObjects, f)
