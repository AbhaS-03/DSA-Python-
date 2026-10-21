x="Global"
def outer():
    x="Enclosing"
    def inner():
        x="Local"
        print("Inner",x)
    inner()
    print("Outer",x)
outer()
print(x)

#using global
def 
