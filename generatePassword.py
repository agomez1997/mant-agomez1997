# Metodo que genera una contraseña de entre 4 y 16 caracteres
# Parametros:
#   N/A.
import random
import string
def generatePassword():
    cantidad= random.randint(4,16)
    password = ''.join(random.choice(string.punctuation+string.ascii_lowercase+string.ascii_uppercase + string.digits+string.ascii_letters) for x in range(cantidad))
    print(password)
    
#Ejecución principal    
generatePassword()

