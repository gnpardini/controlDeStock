import random

def validarCodigosDeProductos():
    codigoDeUnProducto = int(input("Ingrese un código de un producto(FINALIZAR CON -1)"))
    while ((codigoDeUnProducto < 1000) and (codigoDeUnProducto != -1)) or (codigoDeUnProducto > 9999):
        codigoDeUnProducto = int(input("Error. Ingrese un código válido de un producto(FINALIZAR CON -1)"))
    return codigoDeUnProducto
        
def generarStockRandom():
    stock = random.randint(0,20)
    return stock
    

def contarSiHayRepeticionesEnLaListaDeCodigos(listadoDeCodigosDeProductos, codigoDeUnProducto):
    contador = 0
    for i in range (len(listadoDeCodigosDeProductos)):
        if  codigoDeUnProducto == listadoDeCodigosDeProductos[i]:
            contador = contador + 1
    return contador 


def mostrarListadoCompletoDeCodigosYDeStock(listaDeCodigos,listaStockDeCodigos):
    for i in range (len(listaDeCodigos)):
        print("El producto",listaDeCodigos[i],"tiene un stock de",listaStockDeCodigos[i])

    
def contarCuantosProductosPoseenMenosDelStockMinimo(listaDeCodigos, listaDeStockDeCodigosDeProductos):
    contadorDeStockMinimo = 0
    for i in range (len(listaDeStockDeCodigosDeProductos)):
        if listaDeStockDeCodigosDeProductos[i] < 5:
            contadorDeStockMinimo = contadorDeStockMinimo + 1
    return contadorDeStockMinimo

def informarCantidadDeProductosQuePoseenMenosDelStockMinimo(contadorDeStockMinimo):
        if contadorDeStockMinimo == 0:
            print("La cantidad de productos que poseen stock minimo es nulo")
        if contadorDeStockMinimo == 1:
            print("La cantidad de productos que poseen stock minimo es 1")
        if contadorDeStockMinimo > 1:
            print("La cantidad de productos poseen stock minimo son", contadorDeStockMinimo)
            
def contarCualEsLaMayorCantidadDeStock (listaStockDeCodigosDeProductos):
    mayorStock = 0
    for i in range(len(listaStockDeCodigosDeProductos)):
        if listaStockDeCodigosDeProductos[i] > mayorStock:
            mayorStock = listaStockDeCodigosDeProductos[i]                  
    return mayorStock
        
        
def informarMayorCantidadEnStock(mayorCantidadDeStock):
    print("La mayor cantidad en stock es", mayorCantidadDeStock)
    
def codigosDeProductosQueTienenLaMayorCantidadEnStock(listaDeStockDeCodigos, listaDeCodigosDeProductos,mayorCantidadDeStock):
    for i in range (len(listaDeStockDeCodigos)):
        if listaDeStockDeCodigos[i] == mayorCantidadDeStock:
            print("Los códigos de productos que tienen la mayor cantidad de stock son: ", listaDeCodigosDeProductos[i])
            
            
def pedirCantidadVendida():  
    cantidadDeVentas = int(input("Ingrese la cantidad vendida del producto"))
    return cantidadDeVentas

def actualizarStock(listaDeStockDeCodigos,cantidadDeVentas,listaDeCodigosProductos,codigosDeProductos):
    for i in range (len(listaDeStockDeCodigos)):
        if codigosDeProductos == listaDeCodigosProductos[i]:
            resta = listaDeStockDeCodigos [i] - cantidadDeVentas
            listaDeStockDeCodigos[i] = resta
    return listaDeStockDeCodigos[i]
    
def emitirMensajeSiNoHayMasStockDisponible(resta):
    if resta <= 0:
        print("No existen unidades para vender")
        

        
    
    

#Programa principal
    
listaDeCodigos = []
listaStockDeCodigos = []
codigosProductos = validarCodigosDeProductos()
while codigosProductos != -1:
    calculoDeCantidadDeRepeticiones = contarSiHayRepeticionesEnLaListaDeCodigos(listaDeCodigos,codigosProductos)
    if calculoDeCantidadDeRepeticiones > 0:
        print("El código ingresado ya existe")
    else:
        listaDeCodigos.append(codigosProductos)
        cantidadDeStock = generarStockRandom()
        listaStockDeCodigos.append(cantidadDeStock)
    codigosProductos = validarCodigosDeProductos()
mostrarListadoCompletoDeCodigosYDeStock(listaDeCodigos,listaStockDeCodigos)
productosQuePoseenMenosDelStockMinimo = contarCuantosProductosPoseenMenosDelStockMinimo(listaDeCodigos, listaStockDeCodigos)
informarCantidadDeProductosQuePoseenMenosDelStockMinimo(productosQuePoseenMenosDelStockMinimo)
mayorCantidadDeStock = contarCualEsLaMayorCantidadDeStock (listaStockDeCodigos)
informarMayorCantidadEnStock(mayorCantidadDeStock )
codigosDeProductosQueTienenLaMayorCantidadEnStock(listaStockDeCodigos,listaDeCodigos,mayorCantidadDeStock)
codigosProductos = validarCodigosDeProductos()
while codigosProductos != -1:
    calculoDeCantidadDeRepeticiones = contarSiHayRepeticionesEnLaListaDeCodigos(listaDeCodigos,codigosProductos)
    if calculoDeCantidadDeRepeticiones > 0:
        cantidadVendida = pedirCantidadVendida()
        actualizacionDeStock = actualizarStock(listaStockDeCodigos,cantidadVendida,listaDeCodigos,codigosProductos)
        emitirMensajeSiNoHayMasStockDisponible(actualizacionDeStock)
    else:
        listaDeCodigos.append(codigosProductos)
        cantidadDeStock = generarStockRandom()
        listaStockDeCodigos.append(cantidadDeStock)
        
    codigosProductos = validarCodigosDeProductos()
mostrarListadoCompletoDeCodigosYDeStock(listaDeCodigos,listaStockDeCodigos)
    

        

