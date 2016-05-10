class Exporter:

    fhand = None

    def __init__(self, file):
        self.fhand = open(file + '.m', 'w')

    def surface(self, array_list):
        for  in