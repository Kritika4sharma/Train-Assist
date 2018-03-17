# importing necessary libraries
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier

from pandas import read_csv
from pandas import DataFrame

def make_class(row):
	if row['delay'] <= 60:
		return "1"
	elif row['delay'] <= 120:
		return "2"
	elif row['delay'] <= 180:
		return "3"
	elif row['delay'] <= 240:
		return "4"
	elif row['delay'] <= 300:
		return "5"
	elif row['delay'] <= 360:
		return "6"
	elif row['delay'] <= 420:
		return "7"
	elif row['delay'] <= 480:
		return "8"
	else:
		return "9"

# loading the dataset
ourdata = read_csv('our_data.csv', header=None, names = ['vis1','vis2','vis3','vis4','vis5','tempmax1','tempmax2','tempmax3','tempmax4','tempmax5','tempmin1','tempmin2','tempmin3','tempmin4','tempmin5','distance','delay'])
ourdata = ourdata.assign(output_class=ourdata.apply(make_class, axis=1))

# X -> features, y -> label
X = ourdata.loc[:,['vis1','vis2','vis3','vis4','vis5','tempmax1','tempmax2','tempmax3','tempmax4','tempmax5','tempmin1','tempmin2','tempmin3','tempmin4','tempmin5','distance']]
y = ourdata.loc[:,'output_class']
 
# dividing X, y into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
 
# training a linear SVM classifier

svm_model_linear = SVC(kernel = 'linear').fit(X_train, y_train)
svm_predictions = svm_model_linear.predict(X_test)
 
# model accuracy for X_test  
accuracy = svm_model_linear.score(X_test, y_test)
 
# creating a confusion matrix
cm = confusion_matrix(y_test, svm_predictions)
print(cm)

clf = RandomForestClassifier(n_estimators = 5, max_depth=5, random_state=0)
clf.fit(X, y)

#print(clf.predict([['2018', '04', '01']]))
print(clf.score(X, y, sample_weight=None))

clf2 = GradientBoostingClassifier(n_estimators=10, learning_rate=1.0, max_depth=5, random_state=0).fit(X_train, y_train)
print(clf2.score(X_test, y_test))
#print(clf2.predict([['2018', '04', '01']]))

eclf1 = VotingClassifier(estimators=[('lsvm', svm_model_linear), ('rf', clf), ('gbc', clf2)], voting = 'hard')
eclf1 = eclf1.fit(X, y)
print(eclf1.score(X,y,sample_weight=None))
#print(eclf1.predict([['2018', '04', '01']]))