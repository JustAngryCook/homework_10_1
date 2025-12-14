from src.decorators import log




def test_log_decorator_stdout(capsys):
    @log()
    def test_func(a,b):
        return a + b
    result = test_func(2,3)

    assert result == 5

    captured = capsys.readouterr()
    output = captured.out

    assert "test_func started" in output
    assert "test_func finished" in output
    assert "test_func ok" in output
    assert "error" not in output