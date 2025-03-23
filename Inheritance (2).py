# inheritance 

# class Human():
#     def __init__(self):
#         self.energy = 100
    
#     def walk(self):
#         print("I'm now walking")

    

# class Athlete(Human):
#     def __init__(self):
#         super().__init__()
    
#     def run(self):
#         print("I'm now running fast!")

#     def walk(self):                # if we want to add exclusive attributes to the inheritor
#         print("I can walk faster")    # if the inheritor share the same attribute's name with the super, the inheritor's will be excuted [Overriding]


#     # def walk(self):             # if we want to inheritat the same attribute from the super 
#     #     super().walk()


#     # def walk(self):             # if we want to inheritate an attribute and add more features
#     #     super().walk()
#     #     print("I'm walking even more faster")


#     def run(self):                  
#         print("I can run very fast. I am faster than a bullet!")
# runner = Athlete()
# runner.walk()


# class Lamb():
#     def __init__(self):
#         self.switch = 10

#     def switcher(self):
#         print("I can be switched on/off")

# class Smart_lamb(Lamb):
#     def __init__(self):
#         super().__init__()

#     def wifi(self):
#         print("I can connect also to WIFI")

#     def timer(self):
#         print("When I switched off, I count from 5 to 0")


# e_lumb = Smart_lamb()
# e_lumb.switcher()
# e_lumb.wifi()
# e_lumb.timer()


class Device():
    def __init__(self):
        self.connection = True

    def e_connection(self):
        print("I can be connected to electricity")

    def restart(self):
        print("I also has as a feature the restart option")

class Laptop(Device):
    def __init__(self): 
        super().__init__()

    def program_access(self):
        print("I can access to programs data to open or close")

    def smart_restart(self):
        print("I ask first before restarting if you want to reopen the applications or just ignore!!\nOh yeah")

smart_laptop = Laptop()
smart_laptop.e_connection()
smart_laptop.restart()
smart_laptop.program_access()
smart_laptop.smart_restart()