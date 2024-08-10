# ip_locator

Este proyecto consta de un script en Python para rastrear información sobre direcciones IP públicas.

## Requisitos

- Python 3.x
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

### ip_locator

Este script rastrea información sobre una dirección IP pública. Puede rastrear tu propia IP o cualquier otra IP proporcionada.

#### Uso

1. **Para rastrear tu propia IP pública, ejecuta el script:**

    ```bash
    python ip_locator.py
    ```

2. **Para rastrear una IP específica, usa la opción `-i` seguida de la dirección IP:**

    ```bash
    python ip_locator.py -i <ip-address>
    ```

#### Descripción de Opciones

- **`-i <ip-address>`**: Especifica la dirección IP que deseas rastrear. Si no se proporciona, se rastreará tu IP pública actual.
- **`-h`**: Muestra el panel de ayuda con la descripción del uso y las opciones disponibles.

#### Manejo de Errores

- **Error de Solicitud HTTP:** Muestra un mensaje de error si no se puede realizar la solicitud a la API de `ip-api.com`.
- **Error de IP no válida:** Muestra un mensaje si la IP proporcionada no devuelve información válida.

## Información Adicional

- **GitHub**: [https://github.com/m4lal0/ipTracker](https://github.com/m4lal0/ipTracker)
- **Autor**: @m4lal0

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

Utiliza este script para rastrear información geográfica y de ISP sobre direcciones IP de manera sencilla.
