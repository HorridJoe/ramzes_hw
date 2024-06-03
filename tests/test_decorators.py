from src.decorators import log


def test_log_to_console_success(capsys):
    @log()
    def my_func(x, y):
        return x + y
    my_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'my_func ok\n'

def test_log_to_console_failure(capsys):
    @log()
    def my_func():
        raise Exception('Shit happens')
    my_func()
    captured = capsys.readouterr()
    assert captured.out == 'my_func error: Shit happens. Inputs: (), {}\n'

def test_log_to_file_success():
    @log('.\mylog.txt')
    def my_func(x, y):
        return x + y
    my_func(1, 2)
    with open('.\mylog.txt') as file:
        result = file.readline()
    assert result == 'my_func ok'

def test_log_to_file_failure():
    @log('mylog.txt')
    def my_func():
        raise Exception('Shit happens')
    my_func()
    with open('mylog.txt') as file:
        result = file.readline()
    assert result == 'my_func error: Shit happens. Inputs: (), {}'
