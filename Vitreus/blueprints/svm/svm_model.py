# converter em rest api e finalizar
from sklearn import svm
from sklearn import metrics
# loading the dataset
data = datasets.load_digits()
# create a classifier
cls = svm.SVC(kernel="linear")
# train the model
cls.fit(X_train, y_train)
# predict the response
pred = cls.predict(X_test)

# accuracy
print("acuracy:", metrics.accuracy_score(y_test, y_pred=pred))
# precision score
print("precision:", metrics.precision_score(y_test, y_pred=pred))
# recall score
print("recall", metrics.recall_score(y_test, y_pred=pred))
print(metrics.classification_report(y_test, y_pred=pred))
