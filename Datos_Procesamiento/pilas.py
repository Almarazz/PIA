class Stack: # Creamos la clase Stack
    def __init__(self): # __init__ método que inicializa los atributos del objeto que creamos
        self.items = [] # instancia de la clase para acceder a los atributos y métodos
    def is_empty(self): # Metodo para verificar si la pila esta vacia
        return self.items == []
    def push(self, item): # # Metodo para insertar elementos a la pila, inicialización en 0
        self.items.insert(0, item)
    def pop(self): # Metodo para eliminar el ultimo elemento apilado.
        return self.items.pop(0) # recuerda que un array inicializa en 0
    def print_stack(self): # Metodo para mostrar los elementos de la pila
        print(self.items)
pila = Stack() # Creamos una instancia de la pila 
# ingresamos algunos elementos a la pila
pila.push('a')
pila.push('b')
pila.push('c') 
pila.push('d') 
pila.push('e') 
pila.print_stack() # Mostramos los elementos de la pila
pila.pop() # Utilizamos el metodo pop, para eliminar el elemento
pila.print_stack() # Mostramos nuevamente los elementos de la pila
pila.pop() # Utilizamos el metodo pop, para eliminar el elemento
pila.print_stack() # Mostramos nuevamente los elementos de la pila