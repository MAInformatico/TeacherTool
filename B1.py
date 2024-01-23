import Cambridge

class B1(Cambridge):   
    def __init__(self):
        self.name = " "
        self.test = 0

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, nom):
        self.name = nom
        
    @property
    def test(self):
        return self.test
    
    @test.setter
    def test(self, n):
        self.test = n

    def Reading(self, reading_points, reading_total_points):
        self.percent_category(reading_points,reading_total_points)
    
    def Writting(self,writting_points,writting_total_points):
        self.percent_category(writting_points,writting_total_points)
    
    def Listening(self,listening_points,listening_total_points):
        self.percent_category(listening_points,listening_total_points)
    
    def Speaking(self,speaking_points,speaking_total_points):
        self.percent_category(speaking_points,speaking_total_points)