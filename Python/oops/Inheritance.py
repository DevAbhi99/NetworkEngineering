class Parent:
    wealth=1000000

    def prop(self):
        return "Ancestral Propery with a wealth of ",self.wealth



class Child(Parent):
    wealth=200000000

    def prop(self):

        print(super().prop()," But now new wealth is ", self.wealth)



obj=Child()

obj.prop()

