from datetime import datetime


class TimeGreeting:
    """Класс для вывода приветствия в зависимости от времени."""

    @staticmethod
    def get_greeting():
        """Функция для определения текущего времени и вывода соответствующего приветствия."""

        now = datetime.now()
        hour = now.hour
        if 5 <= hour < 12:
            return "Доброе утро"
        elif 12 <= hour < 18:
            return "Добрый день"
        elif 18 <= hour < 23:
            return "Добрый вечер"
        else:
            return "Доброй ночи"
