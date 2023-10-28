package gestorAplicacion.Mascotas;

import java.util.ArrayList;
import java.util.ArrayList;
import java.io.Serializable;

class Perro extends Animal implements Serializable {
    private static final long serialVersionUID = 1L;

    private double tamano; // Tamaño del perro
    private double peso;  // Peso del perro

   private static ArrayList<String> razasExcluidasCabina = new ArrayList<>();
   private static ArrayList<String> razasExcluidasBodega = new ArrayList<>();

    private static final double PESO_MAXIMO_BODEGA = 30.0;

    private static final double TAMANO_MAXIMO_BODEGA = 30.0;

    private static final double PESO_MAXIMO_CABINA = 8.0;

    private static final double TAMANO_MAXIMO_CABINA = 20.0;

    static {
        // Agregar las razas que están excluidas de volar en la cabina
        razasExcluidasCabina.add("Bulldog");
        razasExcluidasCabina.add("Dóberman");
        razasExcluidasCabina.add("Pitbull");
        razasExcluidasCabina.add("Rottweiler");

        // Agregar las razas que están excluidas de volar en la bodega
        razasExcluidasBodega.add("Pitbull");
        razasExcluidasBodega.add("Rottweiler");
    }
    public Perro(String nombre, String raza, double tamano, double peso) {
        super(nombre, raza);
        this.tamano = tamano;
        this.peso = peso;
    }

    public double getPeso() {
        return this.peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getTamano() {
        return this.tamano;
    }

    public void setTamano(double tamano) {
        this.tamano = tamano;
    }

    @Override
    public boolean puedeViajarEnCabina() {
        if (!razasExcluidasCabina.contains(raza) && getPeso() <= PESO_MAXIMO_CABINA
                && getTamano() <= TAMANO_MAXIMO_CABINA) {
            return true;
        }
        return false;
    }

    @Override
    public boolean puedeViajarEnBodega() {
        if (!razasExcluidasBodega.contains(raza) && getPeso() <= PESO_MAXIMO_BODEGA
                && getTamano() <= TAMANO_MAXIMO_BODEGA) {
            return true;
        }
        return false;
    }

    public String toString() {
        return "nombre: " + this.getNombre() + ", raza: " + this.getRaza() + ", especie: Perro";
    }
}
