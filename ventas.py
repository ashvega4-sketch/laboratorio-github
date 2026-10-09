def calcular_total(precio, cantidad):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
 
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")
    return precio * cantidad

def aplicar_descuento(total, porcentaje):
    if not 0 <= porcentaje <= 100:
        raise ValueError(
            "El descuento debe estar entre 0 y 100"
        )
 
    return total * (1 - porcentaje / 100)