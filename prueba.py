def match(array, obj):
    """
        Esta función recibe dos argumentos: una lista de objetos y un objeto
        adicional. Mediante iteración se extraen los objetos de la lista
        que poseen el par propiedad-valor coincidente con el objeto del segundo
        argumento.
    """
    result = [i for i in array for k, v in i.items() if i.get(k) == obj.get(k)]
    
    return result