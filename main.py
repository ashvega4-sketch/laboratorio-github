from ventas import calcular_total, aplicar_descuento
 
print("=== SISTEMA DE VENTAS ===")
 
producto = "Laptop"
precio = 450000
cantidad = 2
 
subtotal = calcular_total(precio, cantidad)
total = aplicar_descuento(subtotal, 10)
 
print(f"Producto: {producto}")
print(f"Subtotal: ₡{subtotal:,.2f}")
print("Descuento: 10%")
print(f"Total: ₡{total:,.2f}")
