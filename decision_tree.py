#-------------------------------------------------------------------------
# AUTHOR: Irfan Iqbal
# FILENAME: decision_tree.py
# SPECIFICATION: creates decision tree using id3
# FOR: CS 4210.01-1 Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =

for row in db:
    xRow = []
    for i,value in enumerate(row):
        if i==4:
            continue
        if value=="Young" or value=="Myope" or value=="No" or value=="Reduced":
            xRow.append(1)
        elif value=="Prepresbyopic" or value=="Hypermetrope" or value=="Yes" or value=="Normal":
            xRow.append(2)
        elif value == "Presbyopic":
            xRow.append(3)
    X.append(xRow)


#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =

for row in db:
    if row[-1]=="Yes":
        Y.append(1)
    else:
        Y.append(2)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
