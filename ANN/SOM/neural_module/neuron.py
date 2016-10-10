import numpy

class Neuron(object):
    
    def __init__(self, wheights, calss_id):
        self.wheights = wheights
        self.calss_id = calss_id
    
    def activation_function(self):
        pass