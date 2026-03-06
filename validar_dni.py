def validar_dni(dni):
    """
    Valida un DNI español.
    Formato: 8 dígitos + 1 letra (ej: 12345678A)
    
    Args:
        dni (str): El DNI a validar
    
    Returns:
        bool: True si el DNI es válido, False en caso contrario
    """
    # Letras válidas según el algoritmo
    letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    # Eliminar espacios y convertir a mayúsculas
    dni = dni.replace(" ", "").upper()
    
    # Validar formato (8 dígitos + 1 letra)
    if len(dni) != 9:
        return False
    
    # Verificar que los primeros 8 caracteres sean dígitos
    if not dni[:8].isdigit():
        return False
    
    # Verificar que el último carácter sea una letra
    if not dni[8].isalpha():
        return False
    
    # Calcular la letra correcta
    numero = int(dni[:8])
    letra_esperada = letras_validas[numero % 23]
    
    # Comparar con la letra proporcionada
    return dni[8] == letra_esperada


# Ejemplos de uso
if __name__ == "__main__":
    dni_valido = "12345678Z"
    dni_invalido = "12345678A"
    
    print(f"¿Es {dni_valido} válido? {validar_dni(dni_valido)}")
    print(f"¿Es {dni_invalido} válido? {validar_dni(dni_invalido)}")
    print(f"¿Es '12 345 678 Z' válido? {validar_dni('12 345 678 Z')}")  # Con espacios