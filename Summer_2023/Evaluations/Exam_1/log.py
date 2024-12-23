def log(function):
    def wrapper(*args, **kwargs):
        self = args[0]
        acier = args[1]
        caoutchouc = args[2]
        print(f"Une nouvelle auto a été créée de type {self.__class__} acier = {acier} caoutchouc = {caoutchouc}")
        result = function(*args, **kwargs)
        return result

    return wrapper
