from setuptools import setup

#otra opcion es __all__ en el init pero no tengo ni idea de lo que es :)
setup(
    name = 'paquete',
    version = '1.0',
    description = 'No se que estoy haciendo jaja saludos',
    author = 'Satanito',
    package = ['paquete','paquete.hola','paquete.adios'],
    scripts = ['']
)

#se supone que tiene que crearse una carpeta dist pero no lo hace asi que a llorar. En esta carpeta se tiene que crear un archivo llamado paquete no se que
#Sacamos ese archivo de la carpeta y lo instalamos en la terminal con pip install (nombre del archivo)
#Para desinstalar: pip unintall (nombre archivo)