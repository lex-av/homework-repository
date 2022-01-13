# -*- coding: utf-8 -*-


from homework4.pack_task3.module_task3 import my_precious_logger


def test_my_precious_logger_stderr(capsys):
    my_precious_logger("Error: !!!")
    captured_error_msg = capsys.readouterr()
    message = captured_error_msg[1]
    assert message == "Error: !!!\n"


def test_my_precious_logger_stdout(capsys):
    my_precious_logger("OK")
    captured_stdout_msg = capsys.readouterr()
    message = captured_stdout_msg[0]
    assert message == "OK\n"
