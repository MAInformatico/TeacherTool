
class Cambridge:
    def __init__(self, n, num):
        self.name = str(n)
        self.test = int(num)

    def filter(self, chain):
        values = chain.split('/').strip()
        return values


    def percent_category(self, good, total):        
        return round(good/total * 100, 2)
    
    def reading(self, reading_points, reading_total_points):
        return str(self.percent_category(reading_points,reading_total_points))
    
    def writting(self,writting_points,writting_total_points):
        return str(self.percent_category(writting_points,writting_total_points))
            
    def listening(self,listening_points,listening_total_points):
        return str(self.percent_category(listening_points,listening_total_points))
    
    def speaking(self,speaking_points,speaking_total_points):
        return str(self.percent_category(speaking_points,speaking_total_points))

