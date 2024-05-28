import logging
from datetime import datetime

from pythonjsonlogger import jsonlogger

# Создаем логгер
logger = logging.getLogger("users.middleware")


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логируем информацию о входящем запросе
        logger.info(f"Incoming request: {request.method} {request.get_full_path()}")

        # Обрабатываем запрос
        response = self.get_response(request)

        # Логируем информацию об ответе
        logger.info(
            f"Outgoing response: {response.status_code} {response.reason_phrase}"
        )

        return response


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


formatter = CustomJsonFormatter("%(timestamp)s - %(levelname)s - %(message)s")
