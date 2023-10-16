"""
Los Módulos te permitirán crear librerías
de funcionalidades que puedas utilizar o 
reutilizar en cualquier momento en tu proyecto
"""

igv = 0.18

def obtenerIGVconSubtotal(subtotal):    
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal * (1 + 0.18)
    return subtotal*(1+igv)
# y porque no poner 1.18???
# Porque si hago cambios solo necesitaria cambiar la linea 7

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)
