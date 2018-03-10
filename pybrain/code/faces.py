from sklearn import datasets
olivetti = datasets.fetch_olivetti_faces()
X, y = olivetti.data, olivetti.target

from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer

ds = ClassificationDataSet(4096, 1 , nb_classes=40)
for k in xrange(len(X)): 
	 ds.addSample(X[k], y[k])

tstdata, trndata = ds.splitWithProportion(0.25)
trndata._convertToOneOfMany()
tstdata._convertToOneOfMany()
fnn = buildNetwork( trndata.indim, 64, trndata.outdim, outclass=SoftmaxLayer)
trainer = BackpropTrainer(fnn, dataset=trndata, momentum=0.1, learningrate=0.01, verbose=True, weightdecay=0.01) 

trainer.trainEpochs(50)
print 'Percent Error on Test dataset: ', percentError(trainer.testOnClassData(dataset=tstdata), tstdata['class'])

