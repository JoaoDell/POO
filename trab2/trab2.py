#João Victor Dell Agli Floriano - 10799783
import quaternion as q
import math




cubo = q.obj(q.quaternion.vec3ToQuat( 1, 1, 1), q.quaternion.vec3ToQuat( 1, 1,-1), 
          q.quaternion.vec3ToQuat( 1,-1, 1), q.quaternion.vec3ToQuat(-1, 1, 1), 
          q.quaternion.vec3ToQuat( 1,-1,-1), q.quaternion.vec3ToQuat(-1, 1,-1), 
          q.quaternion.vec3ToQuat(-1,-1, 1), q.quaternion.vec3ToQuat(-1,-1,-1))


print("original\n")
print(cubo)


angle = 0.0


while (1):


    s = []
    print("Dê as três coordenadas do vetor eixo de rotação: \n")
    for i in range(3):
        print("coordenada " + str(i + 1) +": ")
        s.append(float(input()))


    vec = q.quaternion.vec3ToQuat(float(s[0]), float(s[1]), float(s[2]))


    print("\nDê o ângulo de rotação (em graus):")
    angle = (float(input())/360.0)*2*math.pi


    cubo = cubo.rotate(vec, angle)


    print("\n\nApós rotação:")
    print(cubo)


    print("\nDeseja fazer uma nova rotação?\n0 - não\n1 - sim\n")


    if int(input()) == 0:
        print("Obrigado por usar!\n")
        break




