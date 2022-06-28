from re import A


class perro:     
    def __ini__(self):
        self.a=5
        self.b=2
        self.c=0
    def verificabotonbuildingapp(self,a,b,c):
            self.a=a
            self.b=b
            self.c=c
            try:
                self.c=a/b
                return True
            except :

                return False      

nuevoperro=perro()
a=nuevoperro.verificabotonbuildingapp(5,2,0)
if a:
    print (a)

else: print(a)