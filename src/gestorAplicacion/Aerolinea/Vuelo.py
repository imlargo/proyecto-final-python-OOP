class Vuelo:

    def __init__(self, origen, destino, aerolinea, id, tiempoSalida, tiempoLlegada):
        self.asientos = []
        self.equipajes = []

        self.AEROLINEA = aerolinea
        self.ID = id
        self.horarioSalida = tiempoSalida
        self.horarioLlegada = tiempoLlegada
        self.DESTINO = destino
        self.ORIGEN = origen

    @staticmethod
    def generarVuelos(self, cantidad, origen, destino):
        vuelos = []
        for x in range(0, cantidad):
            aerolinea = "Nn"
            id = str(x)
            hSalida = Vuelo.generarHora()
            hLlegada = "Nn"
            vuelos.append(Vuelo(origen, destino, aerolinea, id, hSalida, hLlegada))
        return vuelos
    
    @staticmethod
    def generarHora():
        horas = [
                "08:00 AM",
                "09:15 AM",
                "10:30 AM",
                "11:45 AM",
                "12:00 PM",
                "01:15 PM",
                "02:30 PM",
                "03:45 PM",
                "04:00 PM",
                "05:15 PM"]
        return horas[1] #implmeentar con random
    

    def generarAsientos(self, economicos,  premium, base):
        for i in range(0, premium):
            self.asientos.append(Asiento("Vip", i, (base * 1.25)))
        
        for j in range(0, economicos):
            self.asientos.append(Asiento("Economico", j, base))
        
    def getOrigenDestino(self):
        return f"{self.ORIGEN} - {self.DESTINO}"
    
    def getInfo(self):
        return f"Id: {self.ID}, Origen: {self.ORIGEN} , Destino: {self.DESTINO} , Hora salida: {self.horarioSalida}"

    ArrayList < Asiento > getAsientos()
        return self.asientos
    

    void setAsientos(ArrayList < Asiento > asientos)
        self.asientos = asientos
    

    getAEROLINEA()
        return self.AEROLINEA
    

    getID()
        return self.ID
    

    getHorarioSalida()
        return self.horarioSalida
    

    void setHorarioSalida(horarioSalida)
        self.horarioSalida = horarioSalida
    

    getHorarioLlegada()
        return self.horarioLlegada
    

    void setHorarioLlegada(horarioLlegada)
        self.horarioLlegada = horarioLlegada
    

    getDESTINO()
        return self.DESTINO
    

    getORIGEN()
        return self.ORIGEN
    

    ArrayList < Maleta > getEquipajes()
        return self.equipajes
    

    void setEquipajes(ArrayList < Maleta > equipajes)
        self.equipajes = equipajes
    

