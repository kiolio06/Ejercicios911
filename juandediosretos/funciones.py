#juan De Dios

#funciones definidas por el usuario

#simple
def my_sum():
    num1 = (2 + 3)
    print(num1)


my_sum()


#return
def my_sum_return():
    return 2 + 3

my_sum_return()

my_sum = my_sum_return()
print(my_sum)

# con arumentos

def my_sum_args(num1 , num2):
    print(f"{num1} {num2}")

my_sum_args((2 + 4) , (3 + 5))
my_sum_args((23 + 32) , (7 + 5))

# con argumento predeterminado
def my_sum_args_default(num1 = 2):
    print(f"{num1}")

my_sum_args_default()
my_sum_args_default(5 + 5)

# con retorno de varios valores
def my_sum_multiple_return():
    return 2 + 4 , 3 + 5

number_one, number_two = my_sum_multiple_return()
print(number_one)
print(number_two)

#con un numero variable de argumentos

def my_sum_variable_args(*args):
    for arg in args:
        print(f"numeros agregados {arg}")

my_sum_variable_args((7824 + 322), (43 * 12), (22 - 6), (54/11),(23 % 4))

#con un numero variable de argunmentos y palabras clave
def my_sum_variable_args_key(**args):
    for key, value in args.items():
        print(f"operacion agregada {value} ({key})")

my_sum_variable_args_key(suma = (7824 + 322), 
                        multiplicacion = (43 * 12), 
                        resta = (22 - 6), 
                        division = (54/11), 
                        residuo = (23 % 4))


#funcions dentro de funciones
def my_sum_outside_function():
    def my_sum_inside_function():
        print("Hola desde la funcion interna")
    my_sum_inside_function()

my_sum_outside_function()

#funciones de lenguaje (built-in)

print(len("hello world"))
print((type(34.6)))

nombres = ["Ana", "Luis", "Pedro", "Juan", "Maria"]
for i, nombre in enumerate(nombres):
    print(i, nombre)

sum([1, 2, 3])  # suma
max([1, 2, 3])  # maximo valor
min([1, 2, 3])  # minimo vaLor

#variables globales y locales

global_var = 10 + 20

print(global_var)

def my_sum_global():
    local_var = 5 + 5
    print(f"mi suma es {local_var} , {global_var}")

my_sum_global()

#extra

def print_numbers(text1, text2):
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{text1} {text2}")
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1
    return count
print(print_numbers("text1", "text2"))
