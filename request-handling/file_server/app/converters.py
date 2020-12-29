from datetime import datetime, date


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value: datetime) -> str:
        return datetime.strftime(value, '%Y-%m-%d')
