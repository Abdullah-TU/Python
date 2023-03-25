class Dog:
    # class variable
    animal_category="Mammal."
    
    # constructor with Instance variable
    def __init__(self, name, age, sex, breed):
        self.name= name
        self.age=age
        self.sex=sex
        self.breed=breed
        
    def get_name(self):
        return self.name  
    
    
    def get_age(self):
        return self.age
    
    def get_sex(self):
        return self.sex
    
    def get_breed(self):
        return self.breed
    
    def sleep(self):
        return "Zzzzzzzzzzz...."
    
    def print_about_dog(self):
        print("Dog name is {a}. {a} is {b} years old. {a} is {c} and his/her breed is {d}. He/she sleeps like {e}. By the way, he/she is a {f}".format(a=self.get_name(),
                                                                                                               b=self.get_age(),
                                                                                                               c=self.get_sex(),
                                                                                                               d=self.get_breed(),
                                                                                                               e=self.sleep(),
                                                                                                              f=self.animal_category
                                                                                                               ))       
    
    def update_attribute(self, attribute_name, new_value):
        setattr(self, attribute_name, new_value)
        print(f"{attribute_name} is updated to {new_value}")
          
dog1=Dog("deshi kutta", 3, "male", 'Sarail hound')

dog1.print_about_dog()        
