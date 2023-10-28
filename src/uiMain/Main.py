from gestorAplicacion.Aerolinea.Asiento import Asiento
from gestorAplicacion.Aerolinea.Boleto import Boleto
from gestorAplicacion.Aerolinea.Maleta import Maleta
from gestorAplicacion.Aerolinea.Pasajero import Pasajero
from gestorAplicacion.Aerolinea.RestriccionesMaleta import RestriccionesMaleta
from gestorAplicacion.Aerolinea.ServiciosEspeciales import ServiciosEspeciales
from gestorAplicacion.Aerolinea.Vuelo import Vuelo

from gestorAplicacion.Cuenta.Usuario import Usuario
from gestorAplicacion.Cuenta.GestionUsuario import GestionUsuario

from gestorAplicacion.Descuentos.Descuento import Descuento
from gestorAplicacion.Descuentos.descuentoMaleta import descuentoMaleta
from gestorAplicacion.Descuentos.descuentoVuelo import descuentoVuelo
from gestorAplicacion.Descuentos.upgradeAsiento import upgradeAsiento

from gestorAplicacion.Mascotas.Animal import Animal 
from gestorAplicacion.Mascotas.Perro import Perro
from gestorAplicacion.Mascotas.Gato import Gato

from .Estetica import *


gestionUsuario = GestionUsuario()

def main():
    user = None # Variable para almacenar instancia del usuario
    opcion = 0 # Variable para almacenar la opción seleccionada
    # Función que imprime un separador visual en la consola
    separador()
    # Función que muestra un mensaje de bienvenida en color morado y negrita
    aviso(negrita(colorTexto("Bienvenido al programa", "morado")))
    # Otro separador
    separador()
    # Bucle principal del programa
    
    while True:
        user = gestionUsuario.getUser() # Obtiene la información del usuario
        if (user == None):
            # Si no hay un usuario registrado
            # Muestra un mensaje de aviso
            aviso("¡No hay sesión iniciada!")
            # Salto de línea
            salto()
            # Ofrece dos opciones al usuario: Iniciar Sesión o Salir
            identacion("1. Iniciar Sesión.")
            identacion("2. Salir.")
            # Salto de línea
            salto()
            # Pide al usuario que ingrese una opción
            prompt("Opcion:")
            opcion = inputI()
            # Separador grande
            separadorGrande()
            match (opcion):
                case 1:
                    # Iniciar Sesión
                    intentos = 0 # Variable para contar los intentos
                    while (user == None and intentos < 3):
                        # Muestra un mensaje de inicio de sesión en color morado
                        identacion(negrita(colorTexto("Iniciar sesión", "morado")), 4)
                        salto()
                        # Pide al usuario que ingrese su correo
                        printNegrita("Mail:")
                        mail = inputS()
                        # Pide al usuario que ingrese su contraseña
                        printNegrita("Contraseña:")
                        contrasena = inputS()
                        # Separador grande
                        separadorGrande()
                        # Intenta iniciar sesión con el correo y la contraseña proporcionados
                        user = gestionUsuario.iniciarSesion(mail, contrasena)
                        if (user == None):
                            # Si la sesión no se inicia con éxito, muestra un mensaje de error
                            salto()
                            aviso(colorTexto("inválido o no existe, intente nuevamente", "rojo"))
                            salto()
                            intentos += 1
                        
                    
                    if (intentos >= 3):
                        print("Demasiados intentos")
                        
                    
                    salto()
                    # Muestra un mensaje de sesión iniciada con éxito en color verde
                    aviso(colorTexto("Sesión iniciada con éxito", "verde"))
                    salto()
                    # Muestra un mensaje de bienvenida personalizado
                    titulo(colorTexto(("Bienvenido " + user.getNombre() + " :)"), "morado"))
                    salto()
                    continuar()
                    
                
                case 2:
                    # Si el usuario selecciona la opción 2, se sale del programa
                    print(colorTexto("Saliendo del programa. ¡Adios!", "morado"))
                    separadorGrande()
                    exit()
                    
                case _:
                    pass
                    # Si la opción ingresada no es válida, se establece user a None
                    user = None
                    aviso(colorTexto("Opción incorrecta", "rojo"))
                    
            
        
        while (opcion != 6 and user != None):
            # Bucle que se ejecuta mientras la opción no sea 6 (Salir) y haya un usuario
            # registrado
            # Separador grande
            separadorGrande()
            # Muestra un menú en color morado
            identacion(negrita(colorTexto("> - Menú - <", "morado")), 4)
            salto()
            identacion("1. Comprar vuelo")
            identacion("2. Reasignar vuelo")
            identacion("3. Cancelar vuelo")
            identacion("4. Gestion cuenta")
            identacion("5. Check in")
            identacion("6. Salir")
            separador()
            # Pide al usuario que seleccione una opción
            prompt("Seleccione una opción (1-5): ")
            opcion = inputI()
            salto()
            
            match (opcion):
                case 1:
                    # Opción 1: Comprar vuelo
                    salto()
                    seleccionado("Comprar vuelo")
                    separadorGrande()
                    # Llama a la función comprarVuelo pasando el objeto de usuario como argumento
                    comprarVuelo(user)
                    separadorGrande()
                    
                case 2:
                    # Opción 2: Reasignar vuelo
                    salto()
                    seleccionado("Reasignar vuelo")
                    separadorGrande()
                    # Llama a la función reasignarVuelo pasando el objeto de usuario como argumento
                    reasignarVuelo(user)
                    separadorGrande()
                    
                case 3:
                    # Opción 3: Cancelar vuelo
                    seleccionado("Cancelar vuelo")
                    separadorGrande()
                    # Llama a la función cancelarVuelo pasando el objeto de usuario como argumento
                    cancelarVuelo(user)
                    separadorGrande()
                    
                case 4:
                    # Opción 4: Gestion de cuenta
                    seleccionado("Gestion de cuenta")
                    separadorGrande()
                    # Llama a la función gestionCuenta pasando el objeto de usuario como argumento
                    gestionCuenta(user)
                    # Actualiza el objeto de usuario después de la gestión de la cuenta
                    user = gestionUsuario.getUser()
                    separadorGrande()
                    
                case 5:
                    # Opción 5: Check in
                    seleccionado("Check in")
                    # Actualiza el objeto de usuario después de realizar el check-in
                    user = gestionUsuario.getUser()
                    separadorGrande()
                    # Llama a la función checkin pasando el objeto de usuario como argumento
                    checkin(user)
                    separadorGrande()
                    user = gestionUsuario.getUser()
                    
                case 6:
                    # Opción 6: Salir
                    separadorGrande()
                    # Muestra un mensaje de despedida en color morado y sale del programa
                    print(negrita(colorTexto("Saliendo del programa. ¡Adios!", "morado")))
                    exitOp()
                case _:
                    pass
                    # Si la opción no es válida, muestra un mensaje de error en rojo
                    print(
                            colorTexto("Opción no válida. Por favor, seleccione una opción válida (1-5).", "rojo"))
                    
            
        

def comprarVuelo(user):
    # Solicitar al usuario el origen del vuelo.
    prompt("Por favor ingrese el origen: ")
    origen = inputS()

    # Solicitar al usuario el destino del vuelo.
    prompt("Por favor ingrese el destino: ")
    destino = inputS()
    # Ingrese la cantidad de vuelos a generar?
    # Generar una lista de n vuelos con el origen y destino proporcionados.
    vuelos = Vuelo.generarVuelos(5, origen, destino)
    separador()
    # Mostrar información sobre los vuelos generados.
    identacion(negrita("Vuelo - Origen - Destino"))
    salto()
    
    for vuelo in vuelos:
        identacion(vuelo.getInfo(), 2)
    
    separador()
    # Solicitar al usuario que seleccione un vuelo y se selecciona.
    prompt("Por favor, seleccione el número del vuelo deseado: ")
    indexVuelo = inputI()
    vuelo = vuelos[indexVuelo]
    # Generar asientos VIP y económicos para el vuelo seleccionado.
    vuelo.generarAsientos(3, 5, 100)
    # Crear un boleto para el usuario con el origen, destino y vuelo seleccionados.
    boleto = Boleto(origen, destino, user, vuelo)
    separador()
    # Mostrar los tipos de asientos disponibles y sus precios
    # print("Tipos de asientos disponibles:")
    # Mostrar información sobre los asientos disponibles en el vuelo.
    identacion(negrita(colorTexto("Asientos disponibles", "morado")))
    salto()
    asientos = vuelo.getAsientos()
    for asiento in asientos:
        identacion(asiento.getInfo(), 2)
    
    # Solicitar al usuario que seleccione un número de asiento.
    salto()
    prompt("Por favor, seleccione el número del asiento deseado: ")
    indexAsiento = inputI()
    asiento = asientos[indexAsiento - 1]
    boleto.setAsiento(asiento)
    # Si se selecciona y es valido se prosigue...
    # Se muestra una previsualizacion del precio
    separador()
    print((negrita("Previsualización del precio: "))
            + colorTexto(("$" + boleto.getValor()), "verde"))
    salto()
    continuar()
    # Si sí, sigue, sino, selecciona otro asiento??
    separador()
    # Preguntar al usuario si desea añadir equipaje.
    prompt("¿Desea añadir equipaje? Tiene derecho a llevar maximo 5 maletas. (1 si / 0 no)")
    opcion = inputI()
    cMaletas = 0
    if (opcion == 1):
        # Cada vez q se agrega un equipaje se va mostrando una previsualizacion del
        # precio..
        # Segun la cantidad de equipaje y los precios de cada uni
        exitOp = 1
        c = 0
    
        while (exitOp == 1 and cMaletas != 5):
            c += 1
            separador()
            # Solicitar información sobre el equipaje a agregar.
            prompt("Peso de la maleta (max 60Kg): ")
            peso = inputI()
            prompt("Ancho de la maleta (max 250cm): ")
            ancho = inputI()
            prompt("Largo de la maleta (max 250cm): ")
            largo = inputI()
            prompt("Alto de la maleta (max 250cm): ")
            alto = inputI()
            # Agregar una maleta al boleto y mostrar el nuevo valor del boleto.
            maleta = Maleta(c, peso, largo, ancho, alto)
            if (maleta.verificarRestricciones()):
                maleta.asignarBoleto(boleto)
                boleto.addEquipaje(maleta)
                cMaletas += 1
                separador()
                print(negrita(colorTexto("Nuevo valor del boleto:", "morado")))
                print((colorTexto("-> $" + boleto.getValor(), "verde")))
                salto()
                prompt("¿Desea agregar otro equipaje o continuar? (1 para Sí, 0 para No)")
                exitOp = inputI()
            else:
                salto()
                prompt("La maleta excede las especificaciones maximas, intente nuevamente")
                salto()
            
    
    salto()
    printNegrita("Maletas agregadas con exitOpo, cantidad de maletas: " + (boleto.getEquipaje()).size())
    continuar()
    # Mostrar los detalles de la compra y solicitar confirmación.
    separadorGrande()
    prompt("¿Desea finalizar la compra? Los detalles son los siguientes:")
    salto()
    identacion(boleto.getInfo())
    separadorGrande()
    prompt("Confirmar (Escriba 1 para Confirmar, 0 para Cancelar)")
    confirmacion = inputI()
    separadorGrande()
    if (confirmacion == 1):
        # Comprobar si el usuario tiene suficiente dinero y, si es así, realizar la
        # compra.
        if (user.getDinero() - boleto.getValor() >= 0):
            user.comprarBoleto(boleto)
            boleto.asignarAsiento(asiento)
            print(negrita(colorTexto("Boleto comprado con éxito.", "verde")))
            salto()
            print(negrita(colorTexto("Informacion y detalles:", "morado")))
            salto()
            identacion(boleto.getInfo())
            salto()
            continuar()
            # Mostrar los detalles del vuelo
        else:
            salto()
            print(colorTexto("Dinero insuficiente. Compra cancelada.", "rojo"))
            salto()
        
    else:
        prompt("Compra cancelada.")
    

def reasignarVuelo(user):
    # Obtener el historial de boletos del usuario
    historial = user.getHistorial()
    identacion(negrita(colorTexto("Información de los vuelos:", "morado")))
    salto()
    # Iterar a través del historial de boletos
    for i in range(len(historial)):
        boleto = historial[i]
        # Mostrar información de cada boleto en la lista
        identacion(i + ". " + boleto.getInfo(), 2)
    
    separador()
    prompt("Por favor, seleccione el número del vuelo deseado: ")
    indexVueloTemp = inputI()
    # Obtener el boleto seleccionado por el usuario
    boletoSelec = historial[indexVueloTemp]
    separadorGrande()
    print("Vuelo seleccionado, información detallada:")
    salto()
    identacion(boletoSelec.getInfo())
    separador()
    if (not boletoSelec.getCheckInRealizado()):
        prompt("Está seguro de reasignar el vuelo? (Escriba 1 para Confirmar, 0 para Cancelar):")
        confirmacionTemp = inputI()
        if (confirmacionTemp == 1):
            # Limpiar
            boletoSelec.resetEquipaje()
            asientoPrevio = boletoSelec.getAsiento()
            asientoPrevio.desasignarBoleto()
            user.reasignarBoleto(boletoSelec)
            boletoSelec.resetEquipaje()
            # - - - - - - - -
        else:
            print(colorTexto("Proceso cancelado, hasta luego!", "rojo"))
            return
        
        separadorGrande()
        # Solicitar al usuario el origen del vuelo.
        origen = boletoSelec.getOrigen()
        identacion(colorTexto("Origen: ", "morado") + origen)
        # Solicitar al usuario el destino del vuelo.
        destino = boletoSelec.getDestino()
        identacion(colorTexto("Destino: ", "morado") + destino)
        # Ingrese la cantidad de vuelos a generar?
        # Generar una lista de n vuelos con el origen y destino proporcionados.
        vuelos = Vuelo.generarVuelos(5, origen, destino)
        separador()
        # Mostrar información sobre los vuelos generados.
        identacion("Vuelo - Origen - Destino")# Por mejorar
        salto()
        for vuelo in vuelos:
            identacion(vuelo.getInfo(), 2)
        
        separador()
        # Solicitar al usuario que seleccione un vuelo y se selecciona.
        prompt("Por favor, seleccione el número del vuelo deseado: ")
        indexVuelo = inputI()
        vuelo = vuelos[indexVuelo]
        # Generar asientos VIP y económicos para el vuelo seleccionado.
        vuelo.generarAsientos(3, 5, 100)
        # Crear un boleto para el usuario con el origen, destino y vuelo seleccionados.
        boletoSelec.setVuelo(vuelo)
        separador()
        # Mostrar los tipos de asientos disponibles y sus precios
        # print("Tipos de asientos disponibles:")
        # Mostrar información sobre los asientos disponibles en el vuelo.
        identacion(negrita(colorTexto("Asientos disponibles:", "morado")))
        asientos = vuelo.getAsientos()
        salto()
        for asiento in asientos:
            identacion(asiento.getInfo(), 2)
        
        # Solicitar al usuario que seleccione un número de asiento.
        salto()
        prompt(
                "Por favor, seleccione el número del asiento deseado, a este valor se le agregara un sobrecargo del 10%: ")
        indexAsiento = inputI()
        asiento = asientos[indexAsiento - 1]
        boletoSelec.reasignarAsiento(asiento)
        # Si se selecciona y es valido se prosigue...
        # Se muestra una previsualizacion del precio
        separador()
        print("Previsualización del precio: " + colorTexto("$" + boletoSelec.getValor(), "verde")
                + " ,se agregará un recargo extra del 10%")
        separador()
        # Preguntar al usuario si desea añadir equipaje.
        prompt("¿Desea añadir equipaje? Tiene derecho a llevar maximo 5 maletas. (1 si / 0 no)")
        opcion = inputI()
        cMaletas = 0
        if (opcion == 1):
            # Cada vez q se agrega un equipaje se va mostrando una previsualizacion del
            # precio..
            # Segun la cantidad de equipaje y los precios de cada uni
            exitOp = 1
            c = 0
            while (exitOp == 1 and cMaletas != 5):
                c += 1
                separador()
                # Solicitar información sobre el equipaje a agregar.
                prompt("Peso de la maleta (max 60Kg): ")
                peso = inputI()
                prompt("Ancho de la maleta (max 250cm): ")
                ancho = inputI()
                prompt("Largo de la maleta (max 250cm): ")
                largo = inputI()
                prompt("Alto de la maleta (max 250cm): ")
                alto = inputI()
                # Agregar una maleta al boleto y mostrar el nuevo valor del boleto.
                maleta = Maleta(c, peso, largo, ancho, alto)
                if (maleta.verificarRestricciones()):
                    maleta.asignarBoleto(boletoSelec)
                    boletoSelec.addEquipaje(maleta)
                    cMaletas += 1
                    separador()
                    print(negrita(colorTexto("Nuevo valor del boleto:", "morado")))
                    print((colorTexto("-> $" + boletoSelec.getValor(), "verde")))
                    salto()
                    prompt("¿Desea agregar otro equipaje o continuar? (1 para Sí, 0 para No)")
                    exitOp = inputI()
                else:
                    salto()
                    prompt("La maleta excede las especificaciones maximas, intente nuevamente")
                    salto()
                
             
        salto()
        printNegrita("Maletas agregadas con exito, cantidad de maletas: " + cMaletas)
        continuar()
        # !!! Error !!! Error !!! Error !!!
        # Mostrar los detalles de la compra y solicitar confirmación.
        separadorGrande()
        prompt("¿Desea finalizar la compra? Los detalles son los siguientes:")
        salto()
        identacion(boletoSelec.getInfo())
        separadorGrande()
        prompt("Confirmar (Escriba 1 para Confirmar, 0 para Cancelar)")
        confirmacion = inputI()
        separador()
        if (confirmacion == 1):
            # Comprobar si el usuario tiene suficiente dinero y, si es así, realizar la
            # compra.
            if (user.getDinero() - boletoSelec.getValor() >= 0):
                user.comprarBoletoReasig(boletoSelec)
                boletoSelec.setStatus("Reasignado")
                boletoSelec.asignarAsiento(asiento)
                print(negrita(colorTexto("Boleto comprado con éxito. Detalles:", "morado")))
                identacion(boletoSelec.getInfo())
            else:
                print(colorTexto("Dinero insuficiente. Compra cancelada.", "rojo"))
            
        else:
            print(colorTexto("Compra cancelada.", "rojo"))
        
    else:
        separador()
        print(colorTexto(
                "Usted ya realizo el Check-in para este vuelo por lo tanto no es posible reasignar el vuelo",
                "rojo"))
        continuar()
    

def cancelarVuelo(user):
    # Mostrar la lista de vuelos
    # Seleccionar el vuelo
    # Cancelarlo (Se modifica el boleto y se cambian los valores)
    # Obtener el historial de boletos del usuario
    historial = user.getHistorial()
    identacion(negrita(colorTexto("Información de los vuelos:", "morado")))
    salto()
    # Iterar a través del historial de boletos
    for i in range(len(historial)):
        boleto = historial[i]
        # Mostrar información de cada boleto en la lista
        identacion(i + ". " + boleto.getInfo(), 2)
        

        separador()

        prompt("Por favor, seleccione el número del vuelo deseado: ")
        indexVuelo = inputI()

        # Obtener el boleto seleccionado por el usuario
        boleto = historial.get(indexVuelo)

        separadorGrande()
        print(negrita(colorTexto("Vuelo seleccionado, información detallada:", "morado")))
        salto()
        identacion(boleto.getInfo())

        separadorGrande()

        if (boleto.getStatus() != "Cancelado"):
            prompt("Confirmar la cancelación (Escriba 1 para Confirmar, 0 para Cancelar):")
            confirmacion = inputI()

            separadorGrande()

            if (confirmacion == 1):
                # Realizar la cancelación del boleto
                boleto.setStatus("Cancelado")
                user.cancelarBoleto(boleto)
                asiento = boleto.getAsiento()
                asiento.desasignarBoleto()
                # Informar al usuario sobre la cancelación exitOposa
                print(colorTexto("La cancelación se ha realizado con éxito.", "verde"))
            else:
                separador()
                print(colorTexto("Proceso cancelado", "rojo"))
                continuar()
            
        else:
            separador()
            print(colorTexto("Este vuelo ya fue cancelado", "rojo"))
            continuar()
        
    



def gestionCuenta(user):
    historial = user.getHistorial() # Obtiene el historial de boletos del usuario
    opcion = None
    
    while (opcion != 6): # Continúa el bucle hasta que la opción seleccionada sea 6
        # Muestra un menú para gestionar la cuenta del usuario
        separadorGrande()
        prompt("¿Qué desea hacer?")
        salto()
        identacion("1. Ver información de la cuenta")
        identacion("2. Ver historial de vuelos")
        identacion("3. Depositar dinero")
        identacion("4. Canjear millas")
        identacion("5. Cerrar sesión")
        identacion("6. Volver al menú anterior")
        salto()
        # Pide al usuario que seleccione una opción
        prompt("> Seleccione una opción (1-6):")
        opcion = inputI()
        salto()
        match (opcion):
            case 1:
                # Opción 1: Ver información general de la cuenta
                # Muestra el estado de la cuenta en color morado
                separador()
                identacion(negrita(colorTexto("Estado de la cuenta", "morado")), 4)
                separadorGrande()
                print(user.getInfo()) # Imprime la información de la cuenta
                separadorGrande()
                continuar()
                salto()
                
            case 2:
                # Opción 2: Ver historial de vuelos
                separador()
                # Muestra información de los vuelos en color morado
                salto()
                print(negrita(colorTexto("Información de los vuelos:", "morado")))
                salto()
                # Itera a través del historial de boletos del usuario
                for i in range(len(historial)):
                    boleto = historial[i] # Obtiene un boleto del historial
                    # Muestra información de cada boleto en la lista
                    identacion(i + ". " + boleto.getInfo())
                
                salto()
                continuar()
                salto()
                
            
            case 3:
                # Opción 3: Depositar dinero
                # Pide al usuario que ingrese la cantidad de dinero que desea depositar
                prompt("Ingrese el valor que desea depositar: ")
                valor = inputI()
                user.depositarDinero(valor) # Llama a la función para depositar dinero en la cuenta
                salto()
                print(colorTexto("Transacción realizada con éxito", "verde")) # Muestra un mensaje de
                                                                                            # éxito
                separador()
                
            case 4:
                # Opción 4: Canjear millas
                # Llama a la función canjearMillas pasando el objeto de usuario como argumento
                canjearMillas(user)
                salto()
                
            case 5:
                # Opción 5: Cerrar sesión
                aviso(colorTexto("Cerrando sesión", "rojo")) # Muestra un mensaje de cierre de sesión en rojo
                salto()
                user = gestionUsuario.cerrarSesion(user) # Llama a la función para cerrar la sesión del usuario
                opcion = 6 # Establece la opción en 6 para volver al menú anterior
                salto()
                
            case 6:
                # Opción 6: Volver al menú
                salto()
                aviso(colorTexto("¡Volviendo al menú!", "verde")) # Muestra un mensaje de regreso al menú en verde
                salto()
                
            case _:
                pass
                aviso(colorTexto("Opción incorrecta", "rojo")) # Muestra un mensaje de opción incorrecta en rojo
                salto()
                
        
def checkin(user):
    # Mostrar la lista de vuelos
    # Seleccionar el vuelo
    # Cancelarlo (Se modifica el boleto y se cambian los valores)
    # Obtener el historial de boletos del usuario
    historial = user.getHistorial()
    print(colorTexto("Información de los vuelos:", "morado"))
    salto()
    # Iterar a través del historial de boletos
    for i in range(len(historial)):
        boleto = historial[i]
        # Mostrar información de cada boleto en la lista
        identacion(i + ". " + boleto.getInfo())
        
    salto()
    prompt("Por favor, seleccione el número del vuelo deseado:")
    indexVuelo = inputI()
    # Obtener el boleto seleccionado por el usuario
    boleto = historial.get(indexVuelo)
    separador()
    print(colorTexto("Vuelo seleccionado, información detallada:", "morado"))
    salto()
    identacion(boleto.getInfo())
    salto()
    continuar()
    opcion
    # verifica si ya se realizo el checkin para el vuelo
    # en caso de que ya se realizo el check in no dejaria entrar a este menu
    if ((not boleto.getCheckInRealizado()) and boleto.getStatus() != "Cancelado"):
        
        while (opcion != 4 and (not boleto.getCheckInRealizado())):
            separadorGrande()
            # muestra el menu del check in
            identacion(negrita(colorTexto("Bienvenido al sistema de check-in del vuelo", "morado")), 3)
            salto()
            identacion("1. Realizar check-in")
            identacion("2. Mejorar asiento")
            identacion("3. Comprar servicios especiales")
            identacion("4. Volver al menú anterior")
            salto()
            prompt("> Seleccione una opción (1-4): ")
            opcion = inputI()
            match (opcion):
                case 1:
                    # realizar el check in
                    salto()
                    prompt("Confirma el check-in? (Escriba 1 para Confirmar, 0 para Cancelar):")
                    confirmacion = inputI()
                    separador()
                    if (confirmacion == 1):
                        boleto.setStatus("Confirmado")
                        boleto.setCheckInRealizado(True)
                        print(colorTexto("CheckIn Realizado con éxito.", "verde"))
                    else:
                        print(colorTexto("Proceso cancelado.", "rojo"))
                    
                    continuar()
                    
                case 2:
                    mejorarAsiento(boleto)
                    
                case 3:
                    comprarServiciosEspeciales(boleto, user)
                    
                case 4:
                    # Volver al menu (Listo)
                    salto()
                    aviso("¡Volviendo al menu!")
                    salto()
                    
                case _:
                    pass
                    aviso(colorTexto("Opción incorrecta", "rojo"))
                    
            
    else:
        if (boleto.getStatus() == "Cancelado"):
            separador()
            print(colorTexto("No es posible realizar el checkIn ya que el vuelo fue cancelado", "rojo"))
            continuar()
        else:
            separador()
            print(colorTexto("Usted ya realizo el Check-in para este vuelo", "rojo"))
            continuar()
        
    

def mejorarAsiento(boleto):
    asiento = boleto.getAsiento()
    # se verifica que el asiento sea economico
    # si es vip ya no se puede mejorar
    if (asiento.getTipo() == "Economico"):
        separador()
        prompt("Desea mejorar su asiento a VIP?, esto tiene un costo de $25 (1 Si, 0 No)")
        confirmacion = inputI()
        if (confirmacion == 1):
            # Mejorar asiento
            salto()
            print(negrita(colorTexto("Informacion de su asiento:", "morado")))
            salto()
            identacion(asiento.getInfo())
            salto()
            # Hacer asiento vip
            asientos = (boleto.getVuelo()).getAsientos()
            printNegrita(colorTexto("Asientos disponibles", "morado"))
            salto()
            for asientoTemp in asientos:
                if (asientoTemp.getTipo() == ("Vip")):
                    identacion(asientoTemp.getInfo(), 2)
                
            
            salto()
            prompt("Por favor, seleccione el número del asiento deseado: ")
            indexAsiento = inputI()
            # ... Cambiar y reasignar todo
            newAsiento = asientos[indexAsiento - 1]
            user = boleto.getUser()
            if (user.getDinero() >= 25):
                boleto.upgradeAsiento(asiento, newAsiento)
                boleto.getUser().realizarPago(25)
                separador()
                printNegrita(colorTexto("Mejora de asiento realizado con exitOpo", "verde"))
                salto()
            else:
                print(colorTexto("Dinero insuficiente, mejora cancelada", "rojo"))
            
            continuar()
    else:
        separador()
        print(colorTexto("Su asiento ya es VIP", "verde"))
        separador()
        continuar()
    
def comprarServiciosEspeciales(boleto, user):
    opcion = None
    
    while (opcion != 7):
        separador()
        identacion(negrita(colorTexto("Servicios disponibles", "morado")), 4)
        salto()
        identacion("1. Comida a la carta")
        identacion("2. Viaje con mascota")
        identacion("3. Acompañante para menor de edad")
        identacion("4. Asistencia para pasajero con necesidades especiales")
        identacion("5. Transporte terrestre")
        identacion("6. Ver servicios contratados")
        identacion("7. Volver al menú anterior")
        salto()
        prompt("> Seleccione una opción (1-7): ")
        opcion = inputI()
        separador()
        match (opcion):
            case 1:
                comprarComidaCarta(boleto, user)
                
            case 2:
                viajarConMascota(boleto, user)
                
            case 3:
                contratarAcompanante(boleto, user)
                
            case 4:
                prompt("Desea contratar un asistencia para pasajero con necesidades especiales?")
                prompt("Este servicio no tiene ningun costo (1/0)")
                respuesta = inputI()
                if (respuesta == 1):
                    boleto.anadirServiciosEspeciales(ServiciosEspeciales.ASISTENCIA_NECESIDADES_ESPECIALES)
                    salto()
                    printNegrita(colorTexto("Compra realizada con exitOpo!", "verde"))
                else:
                    prompt("Cancelado")
                
                
            case 5:
                contratarTrasporteTerrestre(boleto, user)
                
            case 6:
                verServiciosContratados(boleto)
                
            case 7:
                # Volver al menu (Listo)
                salto()
                aviso("¡Volviendo al menu!")
                salto()
                
            case _:
                pass
                aviso(colorTexto("Opción incorrecta", "rojo"))
                continuar()
                

def comprarComidaCarta(boleto, user):
    prompt("Desea comprar el servicio de comida a la acarta durante el vuelo? Esto tiene un costo de $40")
    match (confirmarTransaccion(user, ServiciosEspeciales.COMIDA_A_LA_CARTA.getPrecio())):
        case 1:
            # anade a el servicio a la lista del boleto
            boleto.anadirServiciosEspeciales(ServiciosEspeciales.COMIDA_A_LA_CARTA)
            # realiza el pago del servicio
            boleto.getUser().realizarPago(ServiciosEspeciales.COMIDA_A_LA_CARTA.getPrecio())
            printNegrita(colorTexto("Compra realizada con exitOpo!", "verde"))
            salto()
            continuar()
            
        case -1:
            prompt("Dinero insuficiente, compra cancelada")
            continuar()
            
        case 0:
            prompt("Cancelado")
            continuar()
            
        case _:
            pass
            
        
    

def viajarConMascota(boleto, user):
    mascota = None
    # Se pregunta si la mascota es perro o gato
    prompt("Desea viajar con un perro o un gato? ( 1. Perro 2. Gato)")
    op = inputI()
    salto()
    # Se obtienen los datos de la mascota
    prompt("Por favor ingrese el nombre de la mascota")
    nombre = inputS()
    salto()
    prompt("Por favor ingrese la raza de la mascota")
    raza = inputS()
    salto()
    prompt("Por favor ingrese el tamano de la mascota")
    tamano = inputD()
    salto()
    prompt("Por favor ingrese el peso de la mascota")
    peso = inputD()
    salto()
    if (op == 1):
        # Se crea una instancia de perro
        mascota = Perro(nombre, raza, tamano, peso)
    else:
        # Se crea una instancia de gato
        mascota = Gato(nombre, raza, tamano, peso)
    
    # Verifica que la mascota si pueda viajar en cabina o bodega y que no sobrepase
    # el limite de 1 en cabina y 2 en bodega
    if ((mascota.puedeViajarEnCabina() and boleto.getMascotasEnCabina() < 1) or (mascota.puedeViajarEnBodega() and boleto.getMascotasEnBodega() < 2)):
        # Pregunta si desea llevarla en cabina
        prompt("Desea llevar la mascota en cabina? (1 Si, 0 No) Esto tiene un costo de $40")
        opcion = inputI()
        salto()
        # Si desea viajar en cabina
        if (opcion == 1):
            # Verifica que si sea posible viajar en cabina
            if (mascota.puedeViajarEnCabina() and boleto.getMascotasEnCabina() < 1):
                # Confirma la transaccion
                match (confirmarTransaccion(user, ServiciosEspeciales.MASCOTA_EN_CABINA.getPrecio())):
                    case 1:
                        # anade a el servicio a la lista del boleto
                        boleto.anadirServiciosEspeciales(ServiciosEspeciales.MASCOTA_EN_CABINA)
                        # Anade la mascota a la lista del boleto
                        boleto.anadirServiciosMascota(mascota)
                        # realiza el pago del servicio
                        boleto.getUser().realizarPago(ServiciosEspeciales.MASCOTA_EN_CABINA.getPrecio())
                        printNegrita(colorTexto("Compra realizada con exitOpo!", "verde"))
                        salto()
                        continuar()
                        
                    
                    case 0:
                        prompt("Cancelado")
                        continuar()
                        
                    case -1:
                        prompt("Dinero insuficiente, compra cancelada")
                        continuar()
                        
                    case _:
                        pass
                        
                
            elif (boleto.getMascotasEnBodega() < 2):
                # Si no puede viajar en cabina se indica que va a aviajar en bodega
                prompt("La mascota no cumple las restricciones de la aerolinea para viajar en cabina o ya se cumplio el limite permitido.")
                prompt(" Puede viajar en bodega. Esto tiene un costo de $30")
                # Se confirma la transaccion
                match (confirmarTransaccion(user, ServiciosEspeciales.MASCOTA_EN_BODEGA.getPrecio())):
                    case 1:
                        # anade a el servicio a la lista del boleto
                        boleto.anadirServiciosEspeciales(ServiciosEspeciales.MASCOTA_EN_BODEGA)
                        # Anade la mascota a la lista del boleto
                        boleto.anadirServiciosMascota(mascota)
                        # realiza el pago del servicio
                        boleto.getUser().realizarPago(ServiciosEspeciales.MASCOTA_EN_BODEGA.getPrecio())
                        printNegrita(colorTexto("Compra realizada con exitOpo!", "verde"))
                        salto()
                        continuar()
                        
                    case 0:
                        prompt("Cancelado")
                        continuar()
                        
                    case -1:
                        prompt("Dinero insuficiente, compra cancelada")
                        continuar()
                        
                    case _:
                        pass
                        
                
            else:
                aviso(colorTexto("No es posible viajar con la mascota en bodega ya se alcanzo el limite permitido",
                        "rojo"))
                continuar()
            
            # Si desea viajar en bodega
        elif (boleto.getMascotasEnBodega() < 2):
            prompt("El viaje en bodega tiene un costo de $30")
            # Se confirma la transaccion
            match (confirmarTransaccion(user, ServiciosEspeciales.MASCOTA_EN_BODEGA.getPrecio())):
                case 1:
                    # anade a el servicio a la lista del boleto
                    boleto.anadirServiciosEspeciales(ServiciosEspeciales.MASCOTA_EN_BODEGA)
                    # Anade la mascota a la lista del boleto
                    boleto.anadirServiciosMascota(mascota)
                    # realiza el pago del servicio
                    boleto.getUser().realizarPago(ServiciosEspeciales.MASCOTA_EN_BODEGA.getPrecio())
                    printNegrita(colorTexto("Compra realizada con exitOpo!", "verde"))
                    salto()
                    continuar()
                    
                case 0:
                    prompt("Cancelado")
                    continuar()
                    
                case -1:
                    prompt("Dinero insuficiente, compra cancelada")
                    continuar()
                    
                case _:
                    pass
                    
            
        else:
            aviso(colorTexto("No es posible viajar con la mascota en bodega ya se alcanzo el limite permitido",
                    "rojo"))
            continuar()
        
        # Si no se puede viajar de ninguna forma
    else:
        aviso(colorTexto("La mascota no cumple con las restricciones de la aerolinea ", "rojo"))
        aviso(colorTexto("o ya se cumplio el limite permitido por lo tanto no puede viajar", "rojo"))
        continuar()
    

def contratarAcompanante(boleto, user):
    prompt("Desea contratar un acompañante para el pasajero menor de edad? Esto tiene un costo de $15")
    match (confirmarTransaccion(user, ServiciosEspeciales.ACOMPANANTE_PARA_MENOR.getPrecio())):
        case 1:
            # anade a el servicio a la lista del boleto
            boleto.anadirServiciosEspeciales(ServiciosEspeciales.ACOMPANANTE_PARA_MENOR)
            # realiza el pago del servicio
            boleto.getUser().realizarPago(ServiciosEspeciales.ACOMPANANTE_PARA_MENOR.getPrecio())
            separador()
            printNegrita(colorTexto("Asignado con exitOpo ✔", "verde"))
            salto()
            continuar()
            
        case -1:
            prompt("Dinero insuficiente, compra cancelada")
            continuar()
            
        case 0:
            prompt("Cancelado")
            continuar()
            
        case _:
            pass
            
        
    
        
def contratarTrasporteTerrestre(boleto, user):
    prompt("Desea contratar el servicio de transporte terrestre? Esto tiene un costo de $70")
    match (confirmarTransaccion(user, ServiciosEspeciales.TRANSPORTE_TERRESTRE.getPrecio())):
        case 1:
            # anade a el servicio a la lista del boleto
            boleto.anadirServiciosEspeciales(ServiciosEspeciales.TRANSPORTE_TERRESTRE)
            # realiza el pago del servicio
            boleto.getUser().realizarPago(ServiciosEspeciales.TRANSPORTE_TERRESTRE.getPrecio())
            separador()
            printNegrita(colorTexto("Compra realizada con exitOpo!", "verde"))
            salto()
            continuar()
            
        case -1:
            prompt("Dinero insuficiente, compra cancelada")
            continuar()
            
        case 0:
            prompt("Cancelado")
            continuar()
            
        case _:
            pass
            
    

def verServiciosContratados(boleto):
    if (boleto.getServiciosContratados().size() != 0):
        print(colorTexto(("Usted tiene los siguientes servicios contratados"), "morado"))
        salto()
        index = 0
        for servicio in boleto.getServiciosContratados():
            identacion(f"Servicio: {servicio.getServicio()} por un valor de: ${servicio.getPrecio()}")
            if (servicio == ServiciosEspeciales.MASCOTA_EN_CABINA or servicio == ServiciosEspeciales.MASCOTA_EN_BODEGA):
                print("	-" + boleto.getMascotas()[index])
                index += 1    
        continuar()
        
    else:
        print(colorTexto("No tiene servicios contratados", "morado"))
        continuar()
    

def confirmarTransaccion(user, valor):
    prompt("Confirmar Transaccion (Escriba 1 para Confirmar, 0 para Cancelar)")
    confirmacion = inputI()
    salto()
    if (confirmacion == 1):
        if (user.getDinero() >= valor):
            return 1
        else:
            return -1    
    else:
        return 0
    

    

def canjearMillas(user):
    seleccionado("Canjear millas")
    separadorGrande()
    identacion(f"Hola {user.getNombre()}", 3)
    salto()
    opcion = None
    
    while (opcion != 6):
        identacion("En este momento usted posee " + colorTexto("" + user.getMillas(), "morado") + " millas")
        salto()
        prompt("Escoja en que desea canjear sus millas")
        salto()
        # print("Menu")
        identacion("1. Mejora de silla" + " (" + upgradeAsiento.costoMillas + ")")
        identacion("2. Descuento vuelo" + " (" + descuentoVuelo.costoMillas + ")")
        identacion("3. Descuento maleta" + " (" + descuentoMaleta.costoMillas + ")")
        identacion("4. Aplicar descuentos")
        identacion("5. Ver descuentos del usuario")
        identacion("6. Volver al menú anterior")
        salto()
        prompt("> Seleccione una opción (1-6): ")
        opcion = inputI()
        separador()
        # Imprimir las opciones
        match (opcion):
            case 1:
                match (verificarMillas(user, upgradeAsiento.costoMillas)):
                    case 1:
                        user.descontarMillas(upgradeAsiento.costoMillas)
                        printNegrita("Canjeado con éxito, millas restantes: "
                                + colorTexto("" + user.getMillas(), "verde"))
                        separador()
                        prompt("Desea aplicar el descuendo de una vez? (1 si / 0 no)")
                        aplicar = inputI()
                        if (aplicar == 1):
                            descuento = upgradeAsiento(user)
                            millasAsiento(user, descuento)
                        else:
                            descuento = upgradeAsiento(user)
                            descuento.guardar()
                            separador()
                            printNegrita(colorTexto(
                                    "Se guardo el descuento en su cuenta, puedes aplicarlo cuando desees",
                                    "verde"))
                            salto()
                            continuar()
                            separador()
                    case -1:
                        prompt("Millas insuficientes!")
                        
                    case 0:
                        prompt("Operacion cancelada")
                        
                    case _:
                        pass
                        
                
                
            case 2:
                match (verificarMillas(user, descuentoVuelo.costoMillas)):
                    case 1:
                        user.descontarMillas(descuentoVuelo.costoMillas)
                        printNegrita("Canjeado con éxito, millas restantes: "
                                + colorTexto("" + user.getMillas(), "verde"))
                        separador()
                        prompt("Desea aplicar el descuendo de una vez? (1 si / 0 no)")
                        aplicar = inputI()
                        if (aplicar == 1):
                            descuento = descuentoVuelo(user)
                            millasVuelo(user, descuento)
                        else:
                            descuento = descuentoVuelo(user)
                            descuento.guardar()
                            separador()
                            printNegrita(colorTexto(
                                    "Se guardo el descuento en su cuenta, puedes aplicarlo cuando desees",
                                    "verde"))
                            salto()
                            continuar()
                            separador()
                    case -1:
                        prompt("Millas insuficientes!")
                        
                    case 0:
                        prompt("Operacion cancelada")
                        
                    case _:
                        pass
                        
                
            case 3:
                match (verificarMillas(user, descuentoMaleta.costoMillas)):
                    case 1:
                        user.descontarMillas(descuentoMaleta.costoMillas)
                        printNegrita("Canjeado con éxito, millas restantes: "
                                + colorTexto("" + user.getMillas(), "verde"))
                        separador()
                        prompt("Desea aplicar el descuendo de una vez? (1 si / 0 no)")
                        aplicar = inputI()
                        if (aplicar == 1):
                            descuento = descuentoMaleta(user)
                            millasMaleta(user, descuento)
                        else:
                            descuento = descuentoMaleta(user)
                            descuento.guardar()
                            separador()
                            printNegrita(colorTexto(
                                    "Se guardo el descuento en su cuenta, puedes aplicarlo cuando desees",
                                    "verde"))
                            salto()
                            continuar()
                            separador()
                    case -1:
                        prompt("Millas insuficientes!")
                        
                    case 0:
                        prompt("Operacion cancelada")
                        
                    case _:
                        pass
                        
            case 4:
                # Aplicar descuento
                descuentos = verDescuentos(user, 1)
                separador()
                # Solicitar al usuario que seleccione un vuelo y se selecciona.
                prompt("Por favor, seleccione el número del descuento deseado: ")
                index = inputI()
                descuento = descuentos.get(index)
                match (descuento.getTipo()):
                    case "Mejora de asiento":
                        millasAsiento(user, descuento)
                        
                    case "Descuento Vuelo":
                        millasVuelo(user, descuento)
                        
                    case "Descuento de maleta":
                        millasMaleta(user, descuento)
                        
                    case _:
                        pass
                        
            case 5:
                # Ver descuento
                prompt("Desea ver solo los descuentos disponibles/canjeados o los aplicados tambien (1 / 0)")
                op = inputI()
                verDescuentos(user, op)
                salto()
                continuar()
                
            case 6:
                aviso(colorTexto("Volviendo al menu", "rojo"))
                separador()
                
            case _:
                pass
                aviso(colorTexto("Opción incorrecta", "rojo"))        
        separadorGrande()
    

def millasAsiento(user, descuento):
    boleto = selecBoleto(user)
    asiento = boleto.getAsiento()
    # se verifica que el asiento sea economico
    # si es vip ya no se puede mejorar

    if (asiento.getTipo() == "Economico"):
        # Hacer asiento vip
        asientos = (boleto.getVuelo()).getAsientos()
        printNegrita(colorTexto("Asientos disponibles", "morado"))
        salto()
        for asientoTemp in asientos:
            if (asientoTemp.getTipo() == ("Vip")):
                identacion(asientoTemp.getInfo(), 2)
            
        
        salto()
        prompt("Por favor, seleccione el número del asiento deseado: ")
        indexAsiento = inputI()
        # ... Cambiar y reasignar todo
        newAsiento = asientos[indexAsiento - 1]
        boleto.upgradeAsientoMillas(asiento, newAsiento)
        descuento.aplicarDescuento(boleto)
        separador()
        printNegrita(colorTexto("Mejora de asiento realizado con exitOpo", "verde"))
        salto()
        printNegrita(colorTexto("Detalles del nuevo asiento:", "morado"))
        salto()
        identacion((boleto.getAsiento()).getInfo())
        salto()
        continuar()
    else:
        descuento.guardar()
        separador()
        printNegrita(colorTexto(
                "Su asiento ya es VIP, se guardo el descuento en su cuenta", "verde"))
        salto()
        continuar()
        separador()
        



def millasVuelo(user, descuento):
    boleto = selecBoleto(user)
    descuento.aplicarDescuento(boleto)
    # Listo, su costo de maleta ha sdo reducido en un % y se ha regresado el dinero
    printNegrita(f"Se ha aplicado un {descuentoVuelo.descuento} % de descuento en el valor de su vuelo, ahorro de: $ {boleto.getValorInicial() * (0.2)}")
    salto()
    continuar()
    

def verDescuentos(user, op):
    separador()
    descuentos = user.getDescuentos()
    identacion(negrita(colorTexto("Descuentos disponibles:", "morado")), 4)
    salto()
    if (op == 1):
        # Iterar a través del historial de boletos
        for i in range(len(descuentos)):
            descuento = descuentos.get(i)
            if (descuento.isUsado() == False):
                # Mostrar información de cada boleto en la lista
                identacion(i + ". " + descuento.getInfo())
    else:
        # Iterar a través del historial de boletos
        for i in range(len(descuentos)):
            descuento = descuentos.get(i)
            # Mostrar información de cada boleto en la lista
            identacion(i + ". " + descuento.getInfo())
    return descuentos
    
def selecBoleto(user):
    # Obtener el historial de boletos del usuario
    historial = user.getHistorial()
    salto()
    printNegrita(colorTexto("Información de los vuelos:", "morado"))
    salto()
    # Iterar a través del historial de boletos
    for i in range(len(historial)):
        boleto = historial[i]
        # Mostrar información de cada boleto en la lista
        identacion(i + ". " + boleto.getInfo())
    
    salto()
    prompt("Por favor, seleccione el número del vuelo deseado:")
    indexVuelo = inputI()
    # Obtener el boleto seleccionado por el usuario
    boleto = historial.get(indexVuelo)
    separador()
    print(colorTexto("Vuelo seleccionado, información detallada:", "morado"))
    salto()
    identacion(boleto.getInfo())
    salto()
    continuar()
    salto()
    return boleto

def verificarMillas(user, valor):
    prompt("Confirmar canjeo de millas (1 si / 0 no)")
    confirmacion = inputI()
    salto()
    if (confirmacion == 1):
        if (user.getMillas() >= valor):
            return 1
        else:
            return -1
        
    else:
        return 0
        
    

def millasMaleta(user, descuento):
    boleto = selecBoleto(user)
    descuento.aplicarDescuento(boleto)
    # Listo, su costo de maleta ha sdo reducido en un % y se ha regresado el dinero
    printNegrita(f"Se ha aplicado un {descuentoMaleta.descuento}% de descuento en el costo de su equipaje, ahorro de: ${boleto.getValorInicial() * 0.2}")
    salto()
    continuar()
    


