
public abstract class Animal {
    protected String nombre; // Nombre del animal
    protected String raza;  // Raza del animal
    public Animal(String nombre, String raza) {
        this.nombre = nombre;
        this.raza = raza;
    }
    
    public String getNombre() {
        return this.nombre;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public String getRaza() {
        return this.raza;
    }
    
    public void setRaza(String raza) {
        this.raza = raza;
    }
    
    public abstract boolean puedeViajarEnCabina();

    public abstract boolean puedeViajarEnBodega();
}
