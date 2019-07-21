class Singleton:
    __single = None
    def __init__( self ):

         # __single is not "None" 
         # (an instance of this class has been already created)
        if Singleton.__single: 
            raise Singleton.__single

         # __single is "None"     
        Singleton.__single = self 
           
def Handle():
    try:
        single = Singleton()
    except Singleton, s:
        single = s
    return single    


test1=Handle()
test2=Handle()

print("test1",test1)
print("test2",test2)