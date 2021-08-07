import math

class quaternion:
    '''Classe quaternion que armazena quatro valores, q1, q2, q3, e q4, que se organizam:
       quaternion = q1 + q2i + q3j + q4k'''

    def __init__(self, q1, q2, q3, q4):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4


    def __add__(self, qua):
        if(type(qua) == int or type(qua) == float):
            return quaternion(self.q1 + qua, self.q2, self.q3, self.q4)
        elif(type(qua) == complex):
            return quaternion(self.q1 + qua.real, self.q2 + qua.imag, self.q3, self.q4)
        elif(type(qua) == quaternion):
            return quaternion(self.q1 + qua.q1, self.q2 + qua.q2, self.q3 + qua.q3, self.q4 + qua.q4)


    def __radd__(self, qua):
        if(type(qua) == int or type(qua) == float):
            return quaternion(self.q1 + qua, self.q2, self.q3, self.q4)
        elif(type(qua) == complex):
            return quaternion(self.q1 + qua.real, self.q2 + qua.imag, self.q3, self.q4)
        elif(type(qua) == quaternion):
            return quaternion(self.q1 + qua.q1, self.q2 + qua.q2, self.q3 + qua.q3, self.q4 + qua.q4)


    def __sub__(self, qua):
        if(type(qua) == int or type(qua) == float):
            return quaternion(self.q1 - qua, self.q2, self.q3, self.q4)
        elif(type(qua) == complex):
            return quaternion(self.q1 - qua.real, self.q2 - qua.imag, self.q3, self.q4)
        elif(type(qua) == quaternion):
            return quaternion(self.q1 - qua.q1, self.q2 - qua.q2, self.q3 - qua.q3, self.q4 - qua.q4)


    def __rsub__(self, qua):
        if(type(qua) == int or type(qua) == float):
            return quaternion(-self.q1 + qua, -self.q2, -self.q3, -self.q4)
        elif(type(qua) == complex):
            return quaternion(-self.q1 + qua.real, -self.q2 + qua.imag, -self.q3, -self.q4)
        elif(type(qua) == quaternion):
            return quaternion(-self.q1 + qua.q1, -self.q2 + qua.q2, -self.q3 + qua.q3, -self.q4 + qua.q4)


    def __mul__(self, qua):
        if(type(qua) == int or type(qua) == float):
            return quaternion(self.q1*qua - self.q2*0   - self.q3*0   - self.q4*0  , 
                              self.q1*0   + self.q2*qua + self.q3*0   - self.q4*0  ,
                              self.q1*0   - self.q2*0   + self.q3*qua + self.q4*0  ,
                              self.q1*0   + self.q2*0   - self.q3*0   + self.q4*qua)
        elif(type(qua) == complex):
            return quaternion(self.q1*qua.real - self.q2*qua.imag - self.q3*0 - self.q4*0, 
                              self.q1*qua.imag + self.q2*qua.real + self.q3*0 - self.q4*0,
                              self.q1*0 - self.q2*0 + self.q3*qua.real + self.q4*qua.imag,
                              self.q1*0 + self.q2*0 - self.q3*qua.imag + self.q4*qua.real)
        elif(type(qua) == quaternion):        
            return quaternion(self.q1*qua.q1 - self.q2*qua.q2 - self.q3*qua.q3 - self.q4*qua.q4, 
                              self.q1*qua.q2 + self.q2*qua.q1 + self.q3*qua.q4 - self.q4*qua.q3,
                              self.q1*qua.q3 - self.q2*qua.q4 + self.q3*qua.q1 + self.q4*qua.q2,
                              self.q1*qua.q4 + self.q2*qua.q3 - self.q3*qua.q2 + self.q4*qua.q1)


    def __rmul__(self, qua):
        if(type(qua) == int or type(qua) == float):
            return quaternion(self.q1*qua - self.q2*0 - self.q3*0 - self.q4*0, 
                              self.q2*qua + self.q1*0 + self.q4*0 - self.q3*0,
                              self.q3*qua - self.q4*0 + self.q1*0 + self.q2*0,
                              self.q4*qua + self.q3*0 - self.q2*0 + self.q1*0)
        elif(type(qua) == complex):
            return quaternion(qua.real*self.q1 - qua.imag*self.q2 - self.q3*0 - self.q4*0, 
                              qua.real*self.q2 + qua.imag*self.q1 + self.q4*0 - self.q3*0,
                              qua.real*self.q3 - qua.imag*self.q4 + self.q1*0 + self.q2*0,
                              qua.real*self.q4 + qua.imag*self.q3 - self.q2*0 + self.q1*0)
        elif(type(qua) == quaternion):        
            return quaternion(qua.q1*self.q1 - qua.q2*self.q2 - qua.q3*self.q3 - qua.q4*self.q4, 
                              qua.q1*self.q2 + qua.q2*self.q1 + qua.q3*self.q4 - qua.q4*self.q3,
                              qua.q1*self.q3 - qua.q2*self.q4 + qua.q3*self.q1 + qua.q4*self.q2,
                              qua.q1*self.q4 + qua.q2*self.q3 - qua.q3*self.q2 + qua.q4*self.q1)


    def __neg__(self):
        return quaternion(-self.q1, -self.q2, -self.q3, -self.q4)


    def conjugate(self):
        '''Retorna o quaternion conjugado.'''
        return quaternion(self.q1, -self.q2, -self.q3, -self.q4)


    def mod(self):
        '''Retorna o módulo do quaternion.'''
        return math.sqrt(self.q1*self.q1 + self.q2*self.q2 + self.q3*self.q3 + self.q4*self.q4)


    def inverse(qua):
        '''Retorna o quaternion especificado invertido.'''
        if(type(qua) == int or type(qua) == float):
            return quaternion(1/qua, 1/qua, 1/qua, 1/qua)
        elif(type(qua) == complex):
            qaux = quaternion(qua.real, qua.imag, 0, 0)
            qq = qaux*qaux.conjugate()
            divider = qq.mod()
            divisor = qaux.conjugate()
            return quaternion(divisor.q1/divider, divisor.q2/divider, divisor.q3/divider, divisor.q4/divider)
        elif(type(qua) == quaternion):
            qq = qua*qua.conjugate()
            divider = qq.mod()
            divisor = qua.conjugate()
            return quaternion(divisor.q1/divider, divisor.q2/divider, divisor.q3/divider, divisor.q4/divider)


    def __truediv__(self, qua):
        if(type(qua) == int or type(qua) == float):
            return quaternion(self.q1/qua, self.q2/qua, self.q3/qua, self.q4/qua)
        elif(type(qua) == complex):
            qaux = quaternion(qua.real, qua.imag, 0, 0)
            qq = qaux*qaux.conjugate()
            divider = qq.mod()
            divisor = self * qaux.conjugate()
            return quaternion(divisor.q1/divider, divisor.q2/divider, divisor.q3/divider, divisor.q4/divider)
        elif(type(qua) == quaternion):
            qq = qua*qua.conjugate()
            divider = qq.mod()
            divisor = self * qua.conjugate()
            return quaternion(divisor.q1/divider, divisor.q2/divider, divisor.q3/divider, divisor.q4/divider)


    def __rtruediv__(self, qua):
        if(type(qua) == int or type(qua) == float):
            return quaternion(qua/self.mod(), qua/self.mod(), qua/self.mod(), qua/self.mod())
        elif(type(qua) == complex):
            qaux = quaternion(qua.real, qua.imag, 0, 0)
            qq = self*self.conjugate()
            divider = qq.mod()
            divisor = qaux * self.conjugate()
            return quaternion(divisor.q1/divider, divisor.q2/divider, divisor.q3/divider, divisor.q4/divider)
        elif(type(qua) == quaternion):
            qq = self*self.conjugate()
            divider = qq.mod()
            divisor = qua*self.conjugate()
            return quaternion(divisor.q1/divider, divisor.q2/divider, divisor.q3/divider, divisor.q4/divider)


    def __repr__(self):
        sq1 =       str(self.q1) if self.q1 >= 0 else  "- " + str(abs(self.q1))
        sq2 = "+ " + str(self.q2) if self.q2 >= 0 else "- " + str(abs(self.q2))
        sq3 = "+ " + str(self.q3) if self.q3 >= 0 else "- " + str(abs(self.q3))
        sq4 = "+ " + str(self.q4) if self.q4 >= 0 else "- " + str(abs(self.q4))

        return "(" + sq1 + " " + sq2 + "i" + " " + sq3 + "j" + " " + sq4 + "k)" 


    def vec3ToQuat(q2, q3, q4):
        '''Converte um vetor nos espaço tridimensional em um quaternion representativo.'''
        return quaternion(0, q2, q3, q4)





    

    
class obj(quaternion):
    '''Classe construída para armazenar e manipular vértices de objetos no espaço tridimensional
       usando a representação dos mesmos em quaternions.'''

    def __init__(self, *args):
        vertices = list(args)

        self.vert = []
        self.numb_vert = len(vertices)
        for i in range(self.numb_vert):
            self.vert.append(args[i])



    def insert(self, *args):
        '''Insere um quaternion no array de objetos.'''
        vertices = list(args)

        for i in range(len(vertices)):
            self.numb_vert += 1
            self.vert.append(vertices[i])




    def __mul__(self, a):
        aux = []

        o = obj()
        if(type(a) == int or type(a) == float):
            for i in range(self.numb_vert):
                o.insert(quaternion(self.vert[i].q1*a - self.vert[i].q2*0 - self.vert[i].q3*0 - self.vert[i].q4*0, 
                                    self.vert[i].q1*0 + self.vert[i].q2*a + self.vert[i].q3*0 - self.vert[i].q4*0,
                                    self.vert[i].q1*0 - self.vert[i].q2*0 + self.vert[i].q3*a + self.vert[i].q4*0,
                                    self.vert[i].q1*0 + self.vert[i].q2*0 - self.vert[i].q3*0 + self.vert[i].q4*a))

        elif(type(a) == complex):
            for i in range(self.numb_vert):
                o.insert(quaternion(self.vert[i].q1*a.real - self.vert[i].q2*a.imag - self.vert[i].q3*0 - self.vert[i].q4*0, 
                                    self.vert[i].q1*a.imag + self.vert[i].q2*a.real + self.vert[i].q3*0 - self.vert[i].q4*0,
                                    self.vert[i].q1*0 - self.vert[i].q2*0 + self.vert[i].q3*a.real + self.vert[i].q4*a.imag,
                                    self.vert[i].q1*0 + self.vert[i].q2*0 - self.vert[i].q3*a.imag + self.vert[i].q4*a.real))
        elif(type(a) == quaternion):  
            for i in range(self.numb_vert):      
                o.insert(quaternion(self.vert[i].q1*a.q1 - self.vert[i].q2*a.q2 - self.vert[i].q3*a.q3 - self.vert[i].q4*a.q4, 
                                    self.vert[i].q1*a.q2 + self.vert[i].q2*a.q1 + self.vert[i].q3*a.q4 - self.vert[i].q4*a.q3,
                                    self.vert[i].q1*a.q3 - self.vert[i].q2*a.q4 + self.vert[i].q3*a.q1 + self.vert[i].q4*a.q2,
                                    self.vert[i].q1*a.q4 + self.vert[i].q2*a.q3 - self.vert[i].q3*a.q2 + self.vert[i].q4*a.q1)) 
        return o

    def __rmul__(self, a):
        o = obj()
        if(type(a) == int or type(a) == float):
            for i in range(self.numb_vert):
                o.insert(quaternion(a*self.vert[i].q1 - self.vert[i].q2*0 - self.vert[i].q3*0 - self.vert[i].q4*0, 
                                    a*self.vert[i].q2 + self.vert[i].q1*0 + self.vert[i].q4*0 - self.vert[i].q3*0,
                                    a*self.vert[i].q3 - self.vert[i].q4*0 + self.vert[i].q1*0 + self.vert[i].q2*0,
                                    a*self.vert[i].q4 + self.vert[i].q3*0 - self.vert[i].q2*0 + self.vert[i].q1*0))

        elif(type(a) == complex):
            for i in range(self.numb_vert):
                o.insert(quaternion(a.real*self.vert[i].q1 - self.vert[i].q2*a.imag - self.vert[i].q3*0 - self.vert[i].q4*0, 
                                    a.real*self.vert[i].q2 + self.vert[i].q1*a.imag + self.vert[i].q4*0 - self.vert[i].q3*0,
                                    a.real*self.vert[i].q3 - self.vert[i].q4*a.imag + self.vert[i].q1*0 + self.vert[i].q2*0,
                                    a.real*self.vert[i].q4 + self.vert[i].q3*a.imag - self.vert[i].q2*0 + self.vert[i].q1*0))
        elif(type(a) == quaternion):  
            for i in range(self.numb_vert):      
                o.insert(quaternion(a.q1*self.vert[i].q1 - a.q2*self.vert[i].q2 - a.q3*self.vert[i].q3 - a.q4*self.vert[i].q4, 
                                    a.q1*self.vert[i].q2 + a.q2*self.vert[i].q1 + a.q3*self.vert[i].q4 - a.q4*self.vert[i].q3,
                                    a.q1*self.vert[i].q3 - a.q2*self.vert[i].q4 + a.q3*self.vert[i].q1 + a.q4*self.vert[i].q2,
                                    a.q1*self.vert[i].q4 + a.q2*self.vert[i].q3 - a.q3*self.vert[i].q2 + a.q4*self.vert[i].q1)) 
        return o
        
        

    
    def __repr__(self):

        aux = "\0"

        for i in range(self.numb_vert):
            sq2 = "+ " + str("%.3f" % self.vert[i].q2) if self.vert[i].q2 >= 0 else "- " + str("%.3f" % abs(self.vert[i].q2))
            sq3 = "+ " + str("%.3f" % self.vert[i].q3) if self.vert[i].q3 >= 0 else "- " + str("%.3f" % abs(self.vert[i].q3))
            sq4 = "+ " + str("%.3f" % self.vert[i].q4) if self.vert[i].q4 >= 0 else "- " + str("%.3f" % abs(self.vert[i].q4))

            aux = aux + "v" + str(i) + "    (" + sq2 + ", " + sq3 + ", " + sq4 + ")" + "\n"
        
        return aux



    def rotate(self, vec, angle):
        '''Rotaciona todos os vértices armazenados no objeto de acordo com um vetor como eixo e um ângulo de rotação.'''
        
        divider = vec.mod()

        r = math.cos(angle/2) + math.sin(angle/2)*(1/divider)*vec

        aux = r*self*r.conjugate()

        return aux
