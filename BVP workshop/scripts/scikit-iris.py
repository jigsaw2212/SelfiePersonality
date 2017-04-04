import sklearn  #Import the scikit-learn library
from sklearn import datasets   #Importing the datasets that scikit-learn has

iris = datasets.load_iris()  #Loading the data set 


#Looking at the data
print iris.data
X = iris.data
print iris.target
y =  iris.target

#The 3 classes in the iris dataset are respectively [Setosa, Versicolour, and Virginica]

#Loading logistic regression
from sklearn.linear_model import LogisticRegression
estimator = LogisticRegression(verbose=1, max_iter=100) 	#Loading the estimator
estimator.fit(X,y)


#Print the model to see all the parameters
print estimator


#Unseen samples/ Test data
T = [[ 6.5 , 3.0, 5.2 , 0.2 ],
	[ 6.2 , 3.4 , 5.4 , 2.3],
	[ 5.9 , 3.0 ,  5.1 , 1.8]]

#Print the predictions for the unseen samples
print estimator.predict(T)