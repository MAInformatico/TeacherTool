from B1 import B1

class B2(B1):

    def english_use(self, english_use_points, english_use_total_points):
        return str(self.percent_category(english_use_points,english_use_total_points))