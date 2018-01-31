# Docker

![Docker Logo](logo.png)

## ¿Qué es Docker?

* Plataforma de virtualización a nivel de sistema operativo
* Emplea una tecnología denominada *linux contenedores*
* Suite de herramientas para gestionar contenedores

# ¿Qué hacer con Docker?

* Instalar aplicaciones con dependencias complejas fácilmente sin "ensuciar" el sistema operativo.
* Mantener varias versiones de una misma aplicación aisladas unas de otras.
* Usar aplicaciones de Linux en cualquier sistema operativo.
* Definir un entorno de desarrollo portable y aislado del sistema particular de cada desarrollador.
* Garantizar que el entorno de desarrollo simule exactamente el entorno de producción para evitar errores de configuración o dependencias en el despliegue.
* Desplegar en una multitud de arquitecturas diferentes sin necesidad de una configuración particular para cada una.
* Desplegar automáticamente una aplicación en función del uso.

# ¿En qué se diferencia Docker de una máquina virtual?

* Una máquina virtual requiere mayores recursos
* Una máquina virtual es más pesada de encender y apagar
* En una máquina virtual es más complejo configurar como compartir la red, o el sistema de ficheros, tanto con el *host* como con otras máquinas virtuales.
* Un contenedor por defecto es una copia temporal de una imagen
* Una imagen de Docker se define por un archivo de texto `Dockerfile`
* Control por línea de comandos de `docker`
* Banco de imágenes inmenso creado por la comunidad

# ¿En qué se diferencia Docker de una máquina virtual?

![Docker vs Virtual Machines](docker.png)

# Un ejemplo

* Antonio tiene en su máquina instalado `Java 7` que lo usa diariamente para sus desarrollos.
* Jose tiene en su máquina `Java 8`.
* Antonio quiere que Jose pruebe su aplicación, pero para ello Jose tendrá que instalar `Java 7`, cambiar su configuración de `$PATH` y esto posiblemente entrará en conflicto con su otra instalación.
* Para colmo de males, Jose trabaja en Windows 10 pero la aplicación de Antonio solo ha sido probada en Ubuntu.

Con `docker` esta situación no es ningún problema, Antonio simplemente le da a Jose el arhivo `Dockerfile` (o directamente la imagen) y Jose puede probar la aplicación en un entorno aislado, seguro, e idéntico al que Antonio utiliza.

# Docker para usuarios

## Instalando `docker`

Antes de comenzar, aquí hay unos *links* con las guías de instalación oficiales:

* **Windows**: [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/)
* **Mac OS**: [https://docs.docker.com/docker-for-mac/install/](https://docs.docker.com/docker-for-mac/install/)
* **Linux (Ubuntu)**: [https://docs.docker.com/install/linux/docker-ce/ubuntu/](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

# Usando `docker` para ejecutar una aplicación


## Repositorio Oficial de Docker

[https://hub.docker.com](https://hub.docker.com).

```bash
$ docker pull gplsi/leto
```

```bash
$ docker run [opciones] gplsi/leto [comando]
```

```bash
$ docker run -p 5000:5000 gplsi/leto \
         python /leto/leto-ui/app.py
```

# Usar `Linux` en cualquier lugar

Una imagen particularmente útil es cualquier imagen de Linux, por ejemplo `Ubuntu`.

```bash
$ docker pull ubuntu
```

```bash
$ docker run -it ubuntu bash
root@2d4995fe3d48:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
```

```bash
$ docker stats --no-stream
contenedor     CPU %   MEM USAGE / LIMIT   MEM % ...
2d4995fe3d48   0.00%   1.555MiB / 7.7GiB   0.02% ...
```

# Docker para desarrolladores

* Todos los desarrolladores tienen el mismo entorno de desarrollo.
* El entorno de desarrollo y el de ejecución en producción siempre son compatibles
* Toda característica del entorno de ejecución es expresada en código ejecutable, no en documentación que se queda atrasada rápidamente.
* Cualquier cambio de configuración, nueva dependencia, etc., en el entorno, queda registrada en el control de versiones, haciendo imposible que un desarrollador se quede atrás.
* Es posible replicar automáticamente el entorno en cualquier plataforma, en particular en un servidor de integración continua (CI), para garantizar que los *tests* siempre están al día.

# Manejando una aplicación

Archivo `Dockerfile`:

```Dockerfile
FROM python:3.6
RUN pip install --no-cache-dir Flask
COPY ./app /app
EXPOSE 5000
CMD [ "python", "/app/app.py" ]

```

```bash
$ docker build -t gplsi/example .
```

```bash
$ docker run --rm -p 5000:5000 gplsi/example
```

# Desarrollo en modo "debug"


Comandos de inicio personalizados:

```bash
$ docker run --rm -p 5000:5000 gplsi/example
         python /app/app.py --debug
```

**Volúmenes**: puntos de montaje de archivos.

```bash
$ docker run --rm -p 5000:5000
         -v "`pwd`/app:/app" gplsi/example
         python /app/app.py --debug
```

# Manejando más de un servicio

Archivo `docker-compose.yml`:

```yaml
version: "3.3"

services:
  app:
    image: gplsi/example
    build: "."
    ports:
      - "5000:5000"
    command: "python /app/app_mongo.py"

  mongo:
    image: mongo
```

```bash
$ docker-compose up [-d]
```

# Manejando más de un servicio (desarrollo)

Archivo `dev.yml`:

```yaml
version: "3.3"

services:
  app:
    command: "python /app/app_mongo.py --debug"
    volumes:
      - "./app:/app"
```

```bash
$ docker-compose -f docker-compose.yml -f dev.yml up
```

# Consideraciones finales

> Docker es mucho más que lo que hemos visto hasta aquí...

> Pero lo fundamental es el cambio de paradigma...

> Más allá de tener una "máquina virtual" más ligera, lo que hemos logrado con Docker es **convertir nuestra infraestructura en parte integral del proceso de desarrollo**.

> [https://github.com/apiad/docker-intro](https://github.com/apiad/docker-intro)
