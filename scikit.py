from sklearn import tree
features=[[180, 80, 44], [177, 70, 43], [160, 60 ,38],[154, 44, 37],
          [166, 65, 40], [190, 90, 47], [175, 64, 39],
          [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
labels=['male', 'male','female', 'female','male', 'male','female', 'female','female','male','female']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features, labels)
prediction=clf.predict([[190, 70, 43]])
print(prediction)