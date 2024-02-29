import turtle
import random

palabras = ["manzana", "elefante", "catedral", 
            "guitarra", "pijama", "pelota", "heore", 
            "barco", "tren", "cielo", "lukas", "ojitos", 
            "chachi", "amor", "conejo", "madrid"]
aburrido = False




#crear pantalla 
pantalla = turtle.Screen()
pantalla.title("AHORCADO By M41k80")
pantalla.bgcolor("blue")

#dibujar el muneco
def dibujar_hombre(x):
    intento = x
    
    ##cabeza
    if intento == 1:
        turtle.color("red")
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15, None, 100)
        turtle.penup()
       
        
    ##cuerpo
    
    elif intento == 2:
        turtle.color("red")
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
        
    ### brazos
    
    elif intento == 3:
        turtle.color("red")
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
        
    elif intento == 4:
        turtle.color("red")
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(70)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    
    ### piernas
    
    elif intento == 5:
        turtle.color("red")
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(60)
        turtle.right(180)
        turtle.forward(60)
        turtle.penup()
        
    elif intento == 6:
        turtle.color("red")
        turtle.goto(-74,70 )
        turtle.pendown()
        turtle.right(120)
        turtle.forward(60)
        turtle.penup()
        

###inicio 

turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)


while not aburrido:
    turtle.home()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(74)
    turtle.left(90)
    turtle.forward(35)
    turtle.penup()
    turtle.goto(-135, -35)
    
    palabra = random.choice(palabras)
    
    for i in palabra:
        turtle.write("_", True,font=("Arial", 20, "normal"))
        
    correcta = []
    incorrecta = 0
    terminado = False
    
    while incorrecta < 6 and not terminado:
     letra = turtle.textinput('Ahorcado', 'Atina la palabra:')
     turtle.goto(-135, -35)
     if letra not in correcta:
        for i in palabra:
            if i == letra:
                turtle.write(letra.upper() +' ', True, font=("Arial", 20, "normal"))
                correcta += letra
            else:
                turtle.write('_ ', True, font=("Arial", 20, "normal"))
     if letra not in palabra:
        incorrecta += 1
        dibujar_hombre(incorrecta)
        
     if incorrecta == 6:
        turtle.goto(-135, -35)
        for i in palabra:
            if i in correcta:
                turtle.write('_ ', True, font=("Arial", 20, "normal"))
                
                
            else:
                turtle.write(i.upper() + ' ', True, font=("Arial", 20, "normal"))
                turtle.goto(-90, -60)
                #turtle.textinput('lo siento has perdido!!  Preciona enter')
                turtle.write('\nLo siento, has perdido!!', False,
                             align='center', font=("Arial", 20, "normal"))
                
          
     if len(correcta) == len(palabra):
                turtle.goto(-90, -60)
                turtle.write('\nFELICIDADES!!!!!!!', False, align='center',
                             font=("Arial", 20, "normal"))
                terminado = True
                
    responde = turtle.textinput('Ahorcado', 'Quieres jugar de nuevo???? (y o n):  ')
    while responde != 'y' and responde != 'n':
        
        responde = turtle.textinput('Ahorcado', 'Porfavor press "y" o "n" :')
        if responde == 'y':
            turtle.clear()
            turtle.home()
        elif responde == 'n':
            turtle.clear()
            turtle.home()
            turtle.write('Gracias por haber jugado!!', False, align="center",
                     font=("Arial", 25, "normal")) 
        
        aburrido = True                
    
        
        
        
        
           