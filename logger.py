import datetime

class Logger:
    def __init__(self, owner:str) -> None:
        self.__owner = owner

    def __log(self, type:str, msg:str) -> None:
        print("{} - [{}] {} : {}".format(
            datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S.%f"),
            self.__owner, type, msg))

    def info(self, msg:str) -> None:
        self.__log("INFO", msg)

    def warning(self, msg:str) -> None:
        self.__log("WARN", msg)

    def error(self, msg:str) -> None:
        self.__log("ERROR", msg)