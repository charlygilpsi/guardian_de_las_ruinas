def opcion_valida(value, max_option):
    """
    Comprueba que la opción introducida sea un entero dentro del rango
    
    :param value: Valor introducido por el usuario.
    :type value: str
    :param max_option: Opción máxima permitida
    :type max_option: int
    """
    return value.isdigit() and 1 <= int(value) <= max_option