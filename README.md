## Descifrador AES, RSA, Base64 y MD5

Esta herramienta permite descifrar texto cifrado utilizando diversos algoritmos comunes, incluyendo AES, RSA y Base64. Además, incorpora la función MD5 para verificar la integridad del mensaje original.

**Enlace al proyecto:** [https://github.com/yosoymitxel/desencriptador-aes-rsa-base64-md5/](https://github.com/yosoymitxel/desencriptador-aes-rsa-base64-md5/)

## Funcionalidades:

* Decodifica Base64.
* Comprueba funciones hash (MD5, MD2, SHA1, SHA256).
* Intenta descifrado AES-CBC (clave simétrica de 128 bits).
* Intenta descifrado RSA-OAEP (clave pública RSA).
* Verifica integridad del mensaje original con MD5.

## Uso:

1. **Clonar el repositorio:**

```bash
git clone https://github.com/yosoymitxel/desencriptador-aes-rsa-base64-md5.git
```

2. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

3. **Ejecutar la herramienta:**

```bash
python desencriptador.py <texto_cifrado> <clave_opcional>
```

* **`texto_cifrado`**: Texto cifrado codificado.
* **`clave_opcional`**: Clave de descifrado (opcional, si se conoce).

### Ejemplo:

```bash
python desencriptador.py 1f61dcbf4aa6fae5dfdd4c6d195ca6ab EF
```

### Salida:

* **Descifrado exitoso:** Muestra el texto plano descifrado.
* **Descifrado fallido:** Indica que el algoritmo o la clave podrían ser incorrectos.

## Consideraciones:

* La herramienta prueba diferentes algoritmos de descifrado, pero no garantiza el éxito en todos los casos.
* Es fundamental contar con la clave de descifrado correcta para obtener el texto plano.
* La función MD5 se utiliza para verificar la integridad del mensaje original, pero no garantiza la autenticidad del mismo.

## Contribuciones:

* Se agradecen las contribuciones a este proyecto en forma de correcciones de errores, mejoras de código o nuevas funcionalidades.

## Licencia:

Este proyecto está bajo la licencia MIT. Consulte el archivo `LICENSE` para más detalles.
