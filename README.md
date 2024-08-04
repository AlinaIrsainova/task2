# Logger

Этот класс Logger предоставляет простой механизм логирования, который контролирует вывод сообщений на основе временных интервалов. Он может сохранять сообщения с временными метками, предотвращать повторное логирование сообщений, если они повторяются в течение заданного временного интервала (10 секунд), а также поддерживает основные команды для взаимодействия.

# Возможности

Логирование сообщений с временными метками: Сохранение сообщений вместе с их временными метками.
Ограничение частоты: Предотвращение повторного логирования одного и того же сообщения более одного раза в течение 10 секунд.
Управление размером логов: Поддержка максимального размера логируемых сообщений (сброс при превышении).
Очистка логов: Очистка логгера, если за последние 10 секунд не было добавлено сообщений.

# Определение класса
## Logger

Класс __Logger__ содержит следующие методы:

__init__: Инициализация нового экземпляра логгера.

```__should_print_message(timestamp: int, message: str)__```: Определяет, следует ли логировать сообщение на основе его временной метки.

__add_message(timestamp: int, message: str) -> None__: Добавляет новое сообщение с его временной меткой.

__clean(timestamp: int) -> bool__: Очищает логгер, если выполнены условия (т.е. не было недавних сообщений).

__logger_size() -> int__: Возвращает текущее количество сообщений в логгере.

# Использование

Вы можете взаимодействовать с Logger через интерфейс командной строки. Вот как его использовать:

Запустите программу: Запустите скрипт, и вам будет предложено ввести команды.
Доступные команды:
__add__: Добавить новое сообщение с временной меткой.
__size__: Получить текущее количество сообщений в логгере.
__clean__: Очистить логгер, если за последние 10 секунд не было сообщений.
__quit__: Выйти из программы.
Пример взаимодействия#

