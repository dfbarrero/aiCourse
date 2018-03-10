>>> from pybrain.supervised.trainers import BackpropTrainer
>>> net = buildNetwork(2, 3, 1, bias=True)
>>> trainer = BackpropTrainer(net, ds)
>>> trainer.train()
0.31516384514375834
>>> trainer.trainUntilConvergence()
