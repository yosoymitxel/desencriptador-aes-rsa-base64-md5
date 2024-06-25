import base64
import hashlib
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
from Crypto.Hash import MD2  # Import MD2 from pycryptodome


def intentar_descifrar(texto_cifrado, clave=None):
  """
  Intenta descifrar el texto cifrado usando varios algoritmos.

  Args:
      texto_cifrado (str): El texto cifrado codificado en Base64.
      clave (bytes, opcional): La clave de descifrado (si está disponible).

  Returns:
      str: El texto plano descifrado (si tiene éxito), None de lo contrario.
  """

  # Decodificación Base64
  try:
    texto_plano = base64.b64decode(texto_cifrado)
  except Exception as e:
    print(f"Error al decodificar Base64: {e}")
    return None

  # Intento de comprobación de funciones hash
  funciones_hash = ["md5", "md2", "sha1", "sha256"]
  for nombre_funcion in funciones_hash:
    if nombre_funcion == "md2":
      funcion_hash = MD2.new()
    else:
      funcion_hash = getattr(hashlib, nombre_funcion)
    # Se omite la generación del resumen hash para evitar información innecesaria
    # hash_digest = funcion_hash(texto_plano).hexdigest()
    # print(f"Posible hash {nombre_funcion}: {hash_digest}")  # Comentado

  # Intento de descifrado AES-CBC (común para cifrado simétrico)
  try:
    cifrador = AES.new(clave[:16], AES.MODE_CBC, clave[16:32])  # Suponiendo clave de 128 bits y IV de 16 bytes
    descifrado = unpad(cifrador.decrypt(texto_plano), AES.block_size)
    print(f"Posible descifrado AES-CBC: {descifrado.decode('utf-8')}")
    return descifrado.decode('utf-8')
  except Exception as e:
    pass  # Continuar probando otros algoritmos

  # Intento de descifrado RSA-OAEP (común para cifrado asimétrico con clave pública)
  if clave:
    try:
      clave_pem = RSA.importKey(clave)
      cifrador = PKCS1_OAEP.new(clave_pem)
      descifrado = cifrador.decrypt(texto_plano)
      print(f"Posible descifrado RSA-OAEP: {descifrado.decode('utf-8')}")
      return descifrado.decode('utf-8')
    except Exception as e:
      pass  # Continuar si RSA falla

  # Descifrado fallido
  print("Descifrado fallido. El algoritmo y/o la clave podrían ser incorrectos.")
  return None


# Uso de ejemplo (reemplazar con su texto cifrado y clave, si está disponible)
texto_cifrado = "1f61dcbf4aa6fae5dfdd4c6d195ca6ab"
clave = 'EF'  # Reemplazar con su clave de descifrado (si está disponible)

texto_descifrado = intentar_descifrar(texto_cifrado, clave)

if texto_descifrado:
  print(f"Texto descifrado: {texto_descifrado}")
