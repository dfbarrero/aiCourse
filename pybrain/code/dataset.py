alldata = ...

tstdata, trndata = alldata.splitWithProportion(0.25)

trndata._convertToOneOfMany()
tstdata._convertToOneOfMany()

fnn = buildNetwork(trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer)
trainer = BackpropTrainer(fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)
trnresult = percentError(trainer.testOnClassData(), trndata['class'])
tstresult = percentError(trainer.testOnClassData(dataset=tstdata ), tstdata['class'])
