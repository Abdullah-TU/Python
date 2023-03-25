class GuideDog(Dog):
    # class variable
    job_type = "Guide Dog."
    
    # constructor with instance variables
    def __init__(self, name, age, sex, breed, trained_years):
        super().__init__(name, age, sex, breed)
        self.trained_years = trained_years
        
    def get_trained_years(self):
        return self.trained_years
    
    def assist(self):
        return "He's helping my human friend navigate the world!"
    
    def print_about_dog(self):
        super().print_about_dog()
        print("He's also a {g}, and he've been trained for {h} years to help my human friend.".format(g=GuideDog.job_type, 
                                                                                                      h=self.get_trained_years()))

      