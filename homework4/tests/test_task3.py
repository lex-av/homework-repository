# -*- coding: utf-8 -*-


from ..pack_task3.module_task3 import my_precious_logger


def test_my_precious_logger_stderr(capsys):
    my_precious_logger('Error: !!!')
    captured = capsys.readouterr()
    message = captured[1]
    assert message == 'Error: !!!\n'


def test_my_precious_logger_stdout(capsys):
    my_precious_logger('OK')
    captured = capsys.readouterr()
    message = captured[0]
    assert message == 'OK\n'
