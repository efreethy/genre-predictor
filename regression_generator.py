# Creates and persists a multivariate linear regression model.

# USAGE
#  python regression_generator.py data_set.csv

# created by efreethy on 05/18/17
import sys
print "This is the name of the script: ", sys.argv[1]
from sklearn import linear_model
import csv
import numpy as np
from sklearn.externals import joblib

REGRESSOR_OUTPUT_PATH = 'genre_regression.pkl';

with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    observations = np.array(list(reader))

observations = [[float(value) for value in observation] for observation in observations]

# explanatory variables of the dataset span columns 5-23
independents = [row[5:] for row in observations]
# response variables (Genres) of dataset span columns 1-4
dependents = [row[1:5] for row in observations]

clf = linear_model.LinearRegression()
clf.fit(independents, dependents)

# pesists the regression to an output file, making it possible to load
# the regression from elsewhere
joblib.dump(clf, REGRESSOR_OUTPUT_PATH)

print clf.predict(independents[0])
