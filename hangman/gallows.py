

class Gallows(object):
    def __init__(self):
        self.gallows = self.empty_gallows()
        self.miss_count = 0

    def empty_gallows(self):
        return """
       ---------    
       |         |    
       |            
       |            
       |             
       |            
       |            
    -------         """

    def gallows1(self):
        return """
       ---------    
       |         |    
       |        O    
       |            
       |             
       |            
       |            
    -------         """

    def gallows2(self):
        return """
       ---------    
       |         |    
       |        O    
       |         |    
       |             
       |            
       |            
    -------         """

    def gallows3(self):
        return """
       ---------    
       |         |    
       |       \\O    
       |         |    
       |             
       |            
       |            
    -------         """

    def gallows4(self):
        return """
       ---------    
       |         |    
       |       \\O/   
       |         |    
       |             
       |            
       |            
    -------         """

    def gallows5(self):
        return """
       ---------    
       |         |    
       |       \\O/   
       |         |    
       |        /      
       |            
       |            
    -------         """

    def full_gallows(self):
        return """
       ---------    
       |         |    
       |       \\O/   
       |         |    
       |        / \\    
       |            
       |            
    -------         """

    def increment_gallows(self):
        self.miss_count += 1
        if self.miss_count == 1:
            self.gallows = self.gallows1()
        elif self.miss_count == 2:
            self.gallows = self.gallows2()
        elif self.miss_count == 3:
            self.gallows = self.gallows3()
        elif self.miss_count == 4:
            self.gallows = self.gallows4()
        elif self.miss_count == 5:
            self.gallows = self.gallows5()
        elif self.miss_count == 6:
            self.gallows = self.full_gallows()
        else:
            raise ValueError('Invalid number of misses.')

    def __str__(self):
        return self.gallows

    def __repr__(self):
        return self.gallows
