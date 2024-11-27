# Archivo: main.py

# Importar el menú desde otro archivo si está separado (por ejemplo, menu.py).
# from menu import main_menu

def main():
    """
    Función principal del programa.
    """
    print("\n" + "="*50)
    print("              Bienvenido a Poremon!")
    print("="*50)
    
    # Llamar al menú principal
    main_menu()
    
    print("\n" + "="*50)
    print("        ¡Hasta Pronto!       ")
    print("="*50)

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    main()
