>>> from pybrain.structure import SoftmaxLayer
>>> net = buildNetwork(2, 3, 2, outclass=SoftmaxLayer, bias=True)
>>> net.activate((2, 3))
array([ 0.6656323,  0.3343677])
