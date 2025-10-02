public class clasesJava {
    public static void main(String[] args) {
        Persona profesor = new Persona("Alberto", "Dominguez", 30);
        Persona alumno = new Persona("Alejandro", "Barrera", 23);
        Persona chofer = new Persona("Zayuri", "Espinoza", 29);
        Persona deportista = new Persona("Lebron", "James", 30)
    }
}

class Persona {
    String nombre;
    String apellido;
    int edad;

    Persona(String nombre, String apellido, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    void saludar() {
        System.out.println(nombre + " está saludando.");
    }

    void comer() {
        System.out.println(nombre + " está comiendo.");
    }

    void mostrarInfo() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellido: " + apellido);
        System.out.println("Edad: " + edad);
    }
}
