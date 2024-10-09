# ip_locator

Este proyecto consta de un script en Python para rastrear información sobre direcciones IP públicas y generar enlaces de Google Maps basados en la latitud y longitud obtenida.

## Requisitos

- **Python 3.x**
- [Requests](https://pypi.org/project/requests/) (para realizar solicitudes HTTP)
- [Colorama](https://pypi.org/project/colorama/) (para la gestión de colores en la terminal)

## Instalación

1. **Clona o descarga el repositorio:**

    ```bash
    git clone https://github.com/CodingJAndres/ip_locator.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd ip_locator
    ```

3. **Instala las dependencias necesarias:**

    ```bash
    pip install requests colorama
    ```

## Script

### `ip_locator.py`

Este script rastrea información sobre una dirección IP pública y genera un enlace de Google Maps utilizando la latitud y longitud. Puede rastrear tu propia IP o cualquier otra IP proporcionada.

#### Uso

1. **Para rastrear tu propia IP pública, ejecuta el script:**

    ```bash
    python3 ip_locator.py
    ```

2. **Para rastrear una IP específica, usa la opción `-i` seguida de la dirección IP:**

    ```bash
    python3 ip_locator.py -i <ip-address>
    ```

3. **Para rastrear una IP y guardar los resultados en un archivo, usa la opción `-o` seguida del nombre del archivo:**

    ```bash
    python3 ip_locator.py -i <ip-address> -o resultados.txt
    ```

#### Descripción de Opciones

- **`-i <ip-address>`**: Especifica la dirección IP que deseas rastrear. Si no se proporciona, se rastreará tu IP pública actual.
- **`-o <filename>`**: Guarda los resultados en un archivo de texto (`filename`).
- **`-h`**: Muestra el panel de ayuda con la descripción del uso y las opciones disponibles.

#### Información Mostrada

El script muestra y almacena la siguiente información sobre la IP rastreada:

- **IP**: Dirección IP rastreada.
- **País**: País de ubicación.
- **Ciudad**: Ciudad de ubicación.
- **Región**: Región o departamento.
- **Latitud**: Coordenada de latitud.
- **Longitud**: Coordenada de longitud.
- **ISP**: Proveedor de servicios de Internet.
- **Google Maps Link**: Enlace directo a Google Maps con la ubicación basada en la latitud y longitud obtenida.

#### Manejo de Errores

- **Error de Solicitud HTTP:** Muestra un mensaje de error si no se puede realizar la solicitud a la API de `ip-api.com`.
- **Error de IP no válida:** Muestra un mensaje si la IP proporcionada no devuelve información válida.

## Información Adicional

- **GitHub**: [https://github.com/CodingJAndres/ip_locator](https://github.com/CodingJAndres/ip_locator)
- **Autor**: @CodingJAndres

---

Utiliza este script para rastrear información geográfica y de ISP sobre direcciones IP de manera sencilla y generar enlaces para visualizar las ubicaciones en Google Maps.
