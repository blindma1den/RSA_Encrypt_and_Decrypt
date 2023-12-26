import rsa

def generar_claves():
    # Genera un par de claves RSA de 2048 bits
    clave_publica, clave_privada = rsa.newkeys(2048)

    return clave_publica, clave_privada

def cifrar(mensaje, clave_publica):
    # Cifra un mensaje usando la clave pública
    cypher = rsa.encrypt(mensaje.encode("utf-8"), clave_publica)

    return cypher

def descifrar(cypher, clave_privada):
    # Descifra un mensaje cifrado usando la clave privada
    mensaje = rsa.decrypt(cypher, clave_privada).decode("utf-8")

    return mensaje

if __name__ == "__main__":
    # Generamos un par de claves
    clave_publica, clave_privada = generar_claves()

    # Ciframos un mensaje
    mensaje = "Este es un mensaje cifrado"
    cypher = cifrar(mensaje, clave_publica)

    # Desciframos el mensaje
    mensaje_descifrado = descifrar(cypher, clave_privada)

    print(mensaje_descifrado)