#!/usr/bin/python

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

dataModel = [
    [(0,0), (X,)],
    [(0,1), (X,)],
    [(1,0), (X,)],
    [(1,1), (X,)],
]

ds = SupervisedDataSet(X, X)
for input, target in dataModel:
    ds.addSample(input, target)

net = buildNetwork(X, X, X, bias=True)

trainer = BackpropTrainer(net, ds, learningrate = X, momentum = X)
trainer.trainEpochs(epochs=X)

print '0,0->', net.activate([0,0])
print '0,1->', net.activate([0,1])
print '1,0->', net.activate([1,0])
print '1,1->', net.activate([1,1])
