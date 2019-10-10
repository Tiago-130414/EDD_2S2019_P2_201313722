class nodoArbol(object): 
    def __init__(self, carnet): 
        self.carnet = carnet 
        self.izquierda = None
        self.derecha = None
        self.altura = 1
  
class arbolAVL(object): 
  

    def insertar(self, raiz, cnt): 
      
        if not raiz: 
            return nodoArbol(cnt) 
        elif cnt < raiz.carnet: 
            raiz.izquierda = self.insertar(raiz.izquierda, cnt) 
        else: 
            raiz.derecha = self.insertar(raiz.derecha, cnt) 
  

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
  
  
myTree = arbolAVL() 
raiz = None
  
raiz = myTree.insertar(raiz, 10) 
raiz = myTree.insertar(raiz, 20) 
raiz = myTree.insertar(raiz, 30) 
raiz = myTree.insertar(raiz, 40) 
raiz = myTree.insertar(raiz, 50) 
raiz = myTree.insertar(raiz, 25) 
  
myTree.preOrder(raiz) 
