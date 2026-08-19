from maquina_de_cafe import MaquinaDeCafe


def pedir_numero(mensaje, minimo=0):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"Escribe un número mayor o igual a {minimo}.")
        except ValueError:
            print("Escribe un número válido.")


def main():
    maquina = MaquinaDeCafe()

    print("=== MAQUINA DE CAFE ===")
    print("1. Pequeño - 3 Oz")
    print("2. Mediano - 5 Oz")
    print("3. Grande  - 7 Oz")

    opciones = {
        "1": "pequeno",
        "2": "mediano",
        "3": "grande",
    }

    opcion = input("Selecciona el tamaño del vaso: ").strip()

    if opcion not in opciones:
        print("Tamaño no válido.")
        return

    vaso = maquina.obtener_tipo_de_vaso(opciones[opcion])
    cantidad_azucar = pedir_numero("Cantidad de cucharadas de azúcar: ", 0)

    resultado = maquina.obtener_vaso_de_cafe(
        vaso=vaso,
        cantidad_vasos=1,
        cantidad_azucar=cantidad_azucar,
    )

    print(resultado)


if __name__ == "__main__":
    main()
