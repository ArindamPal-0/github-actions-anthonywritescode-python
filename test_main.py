"""Test main.py"""

import main

def test_main_function(capsys) -> None:
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"