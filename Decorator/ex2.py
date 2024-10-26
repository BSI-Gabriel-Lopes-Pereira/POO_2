from datetime import datetime
class Logger:
    def log(self, message):
        raise NotImplementedError("Método log() deve ser implementado")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[INFO]: {message}")

class LoggerDecorator(Logger):
    def __init__(self, logger):
        self._logger = logger

    def log(self, message):
        self._logger.log(message)

class DateLogger(LoggerDecorator):
    def log(self, message):
        date_message = f"{datetime.now().isoformat()} - {message}"
        super().log(date_message)

class LevelLogger(LoggerDecorator):
    def __init__(self, logger, level):
        super().__init__(logger)
        self.level = level

    def log(self, message):
        level_message = f"[{self.level.upper()}] - {message}"
        super().log(level_message)

class FileLogger(LoggerDecorator):
    def __init__(self, logger, file_path):
        super().__init__(logger)
        self.file_path = file_path

    def log(self, message):
        super().log(message)
        with open(self.file_path, 'a') as f:
            f.write(message + '\n')

logger = ConsoleLogger()

logger = DateLogger(logger)
logger = LevelLogger(logger, "error")
logger = FileLogger(logger, "log.txt")

logger.log("Ocorreu um erro crítico no sistema.")
