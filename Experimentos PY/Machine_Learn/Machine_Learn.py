from sklearn import tree

#Table de aprendizagem
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)#Criador de Padrões

print (clf.predict([[160, 0]]))