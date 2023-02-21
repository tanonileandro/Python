"""
Calculadora de impuestos:
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
"""


# Funcion que calcula el total del pago
def funcion_impuestos(pago, impuesto):
    while 0 > pago or 0 > impuesto:
        print('Valor ingresado incorrerto, no usar valores negativos')
        funcion_impuestos(float(input('Ingrese nuevamente su pago sin impuestos: ')),
                          float(input('Ingrese nuevamente el monto del impuesto: ')))
    pagoTotal = pago + (pago * (impuesto / 100))
    return pagoTotal


# Se ejecuta la funcion
pago = float(input('Ingrese el pago sin el impuesto: '))
impuesto = float(input('Ingrese el monto del impuesto: '))

pagoConImpuestos = funcion_impuestos(pago, impuesto)
print(f'El pago total con impuestos es: {pagoConImpuestos}')
