class nodoArbol(object): 
    def __init__(self, carnet, nombre):
        self.nombre = nombre 
        self.carnet = carnet 
        self.izquierda = None
        self.derecha = None
        self.altura = 1
  
class arbolAVL(object): 
  
    def insertar(self, raiz, cnt, nom): 
      
        if not raiz: 
            return nodoArbol(cnt,nom) 
        elif cnt < raiz.carnet: 
            raiz.izquierda = self.insertar(raiz.izquierda, cnt, nom) 
        else: 
            raiz.derecha = self.insertar(raiz.derecha, cnt, nom) 
  
        raiz.altura = 1 + max(self.getAltura(raiz.izquierda), 
                           self.getAltura(raiz.derecha)) 
  
        balance = self.getBalance(raiz) 
  
        # Caso 1 - izquierda  izquierda 
        if balance > 1 and cnt < raiz.izquierda.carnet: 
            return self.rotacionDerecha(raiz) 
  
        # Caso 2 - derecha derecha 
        if balance < -1 and cnt > raiz.derecha.carnet: 
            return self.rotacionIzquierda(raiz) 
  
        # Caso 3 - izquierda derecha 
        if balance > 1 and cnt > raiz.izquierda.carnet: 
            raiz.izquierda = self.rotacionIzquierda(raiz.izquierda) 
            return self.rotacionDerecha(raiz) 
  
        # Caso 4 - derecha izquierda
        if balance < -1 and cnt < raiz.derecha.carnet: 
            raiz.derecha = self.rotacionDerecha(raiz.derecha) 
            return self.rotacionIzquierda(raiz) 
  
        return raiz 
  
    def rotacionIzquierda(self, z): 
  
        y = z.derecha 
        T2 = y.izquierda 
   
        y.izquierda = z 
        z.derecha = T2 
  
        z.altura = 1 + max(self.getAltura(z.izquierda), 
                         self.getAltura(z.derecha)) 
        y.altura = 1 + max(self.getAltura(y.izquierda), 
                         self.getAltura(y.derecha)) 
  
        return y 
  
    def rotacionDerecha(self, z): 
  
        y = z.izquierda 
        T3 = y.derecha 
  
        y.derecha = z 
        z.izquierda = T3 
  
        z.altura = 1 + max(self.getAltura(z.izquierda), 
                        self.getAltura(z.derecha)) 
        y.altura = 1 + max(self.getAltura(y.izquierda), 
                        self.getAltura(y.derecha)) 
  
        return y 
  
    def getAltura(self, raiz): 
        if not raiz: 
            return 0
  
        return raiz.altura 
  
    def getBalance(self, raiz): 
        if not raiz: 
            return 0
  
        return self.getAltura(raiz.izquierda) - self.getAltura(raiz.derecha) 
  
    def preOrder(self, raiz): 
  
        if not raiz: 
            return
  
        print("{0} ".format(raiz.carnet), end="") 
        self.preOrder(raiz.izquierda) 
        self.preOrder(raiz.derecha) 

    def inOrder(self, raiz):
        if not raiz:
            return

        self.inOrder(raiz.izquierda) 
        print("{0} ".format(raiz.carnet), end="") 
        self.inOrder(raiz.derecha)    

    def postOrder(self,raiz):
        if not raiz:
            return
           
        self.postOrder(raiz.izquierda) 
        self.postOrder(raiz.derecha)    
        print("{0} ".format(raiz.carnet), end="") 
        
  
myTree = arbolAVL() 
raiz = None
  
raiz = myTree.insertar(raiz, 10,"hola1") 
raiz = myTree.insertar(raiz, 20,"hola2") 
raiz = myTree.insertar(raiz, 30,"hola3") 
raiz = myTree.insertar(raiz, 40,"hola4") 
raiz = myTree.insertar(raiz, 50,"hola5") 
raiz = myTree.insertar(raiz, 25,"hola6") 
  
print("pre orden")  
myTree.preOrder(raiz)
print()
print("in orden")
myTree.inOrder(raiz)
print()
print("post order")
myTree.postOrder(raiz) 
