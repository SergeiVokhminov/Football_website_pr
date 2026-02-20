import socket
import platform


def get_first_local_ip_mac():
    """Возвращает первый локальный IP-адрес macOS или сообщение об ошибке."""

    system = platform.system()
    if system != "Darwin":
        return "Неподдерживаемая операционная система."

    # Попытка соединения через внешний маршрут
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            if ip and not ip.startswith("127."):
                return ip
    except Exception:
        pass

    return "Не удалось определить локальный IP-адрес."


if __name__ == "__main__":
    print(get_first_local_ip_mac())
