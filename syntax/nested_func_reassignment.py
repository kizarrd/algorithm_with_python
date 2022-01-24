class Example:
    cv = 1
    def function(self):
        lv = 2
        print("-------------------------------before nested function")
        print(self.cv)
        print(id(self.cv))
        print(lv)
        print(id(lv))
        
        def nested_function():
            self.cv = 11
            lv = 22
            print("----------------------------------------inside nested function")
            print(self.cv)
            print(id(self.cv))
            print(lv)
            print(id(lv))
            
        nested_function()
        print("----------------------------------------------after nested function")
        print(self.cv)
        print(id(self.cv))
        print(lv)
        print(id(lv))

e = Example()
e.function()