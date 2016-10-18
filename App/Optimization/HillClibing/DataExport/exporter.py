class Exporter:

    fhand = None

    def __init__(self, file):
        self.fhand = open(file + '.m', 'w')

    def surface_data_export(self, array_list):
        print ('TODO!!!!!!')