
#------subproces es mejor

import subprocess

cmd = "notepad"

returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
print('returned value:', returned_value)

#------- os esta quedando en desuso

import os
os.system('microsoftedge') #abrir un programa

print(os.getcwd())#tomar ruta

f = open(os.path.join(os.getcwd(), "archivo.txt"))#ruta en archivo

#os.system('date')#fecha


valor1 = os.system("whoami")
print("Resultado:", valor1)

'''
Saber si se puede acceder a un archivo o directorio	    os.access(path, modo_de_acceso)
Conocer el directorio actual	                        os.getcwd()
Cambiar de directorio de trabajo	                    os.chdir(nuevo_path)
Cambiar al directorio de trabajo raíz	                os.chroot()
Cambiar los permisos de un archivo o directorio     	os.chmod(path, permisos)
Cambiar el propietario de un archivo o directorio	    os.chown(path, permisos)
Crear un directorio	                                    os.mkdir(path[, modo])
Crear directorios recursivamente	                    os.mkdirs(path[, modo])
Eliminar un archivo	                                    os.remove(path)
Eliminar un directorio	                                os.rmdir(path)
Eliminar directorios recursivamente	                    os.removedirs(path)
Renombrar un archivo	                                os.rename(actual, nuevo)
'''



print(os.path.getsize(os.getcwd()), "bytes", " - 1000 bytes = 1kb" ) #

'''
Ruta absoluta	                            os.path.abspath(path)
Directorio base	                            os.path.basename(path)
Saber si un directorio existe	            os.path.exists(path)
Conocer último acceso a un directorio	    os.path.getatime(path)
Conocer tamaño del directorio	            os.path.getsize(path)
Saber si una ruta es absoluta       	    os.path.isabs(path)
Saber si una ruta es un archivo	            os.path.isfile(path)
Saber si una ruta es un directorio	        os.path.isdir(path)
Saber si una ruta es un enlace simbólico	os.path.islink(path)
Saber si una ruta es un punto de montaje	os.path.ismount(path)
'''

import webbrowser
webbrowser.open_new_tab("http://www.google.com")

