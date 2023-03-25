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
    

dog1=Dog("deshi kutta", 3, "male", 'Sarail hound')
print("Dog name is {a}. {a} is {b} years old. {a} is {c} and his/her breed is {d}. He/she sleeps like {e}. By the way, he/she is a {f}".format(a=dog1.get_name(),
                                                                                                               b=dog1.get_age(),
                                                                                                               c=dog1.get_sex(),
                                                                                                               d=dog1.get_breed(),
                                                                                                               e=dog1.sleep(),
                                                                                                               f=dog1.animal_category
                                                                                                               ))
        
        
