from trace_utils import logger


@logger(path_filename='C:/Users/konst/PycharmProjects/decorator_logger2/logfile.txt')  # Заменить на ваш путь к файлу
def plus_and_multiple(a, b, c):
    return (a + b) * c


if __name__ == '__main__':
    # Задание2
    plus_and_multiple(2, b=3, c=4)