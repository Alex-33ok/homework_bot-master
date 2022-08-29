class AccessStatusError(Exception):
    """Ошибка статуса доступа к серверу."""

    pass


class EmptyHWList(Exception):
    """Ошибка списка ДЗ."""

    pass


class RequestError(Exception):
    """Исключение в запросе API."""

    pass


class SendingError(Exception):
    """Ошибка при отправке сообщения."""

    pass
