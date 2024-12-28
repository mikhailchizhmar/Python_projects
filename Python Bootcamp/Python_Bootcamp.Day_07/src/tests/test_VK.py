import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import ex01.main as m


def test_load_questions():
    print()
    assert m.load_questions("") == []
    assert m.load_questions("empty.json") == []
    assert m.load_questions("../ex00/q_n_a.json") != []


def test_ask(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    assert m.ask(0) is True

    monkeypatch.setattr('builtins.input', lambda _: '4')
    with pytest.raises(ValueError, match="Answer must be between 1 and 3."):
        m.ask(1)

    monkeypatch.setattr('builtins.input', lambda _: 'five')
    with pytest.raises(ValueError, match="Answer must be between 1 and 3."):
        m.ask(3)


def test_validate_response(monkeypatch, capsys):
    inputs = iter(["15", "70", "4", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    stats = m.validate_response()
    assert stats == [15, 70, 4, 5]

    inputs = iter(["-1", "10", "70", "4", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    m.validate_response()
    captured = capsys.readouterr()
    assert "Respiration rate cannot be negative or larger than 499" in captured.out


def test_assess_response():
    stats = [15, 70, 4, 5]
    assert m.assess_response(stats) == 2

    stats = [13, 65, 2, 4]
    assert m.assess_response(stats) == 4


def test_main(monkeypatch, capsys):
    stats = ['13', '65', '2', '4'] * 10
    j = 0
    for i in range(0, 50, 5):
        stats.insert(i, str(m.right_answers[j]))
        j += 1

    inputs = iter(stats)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    m.main()
    captured = capsys.readouterr()
    assert "The subject is classified as: Human" in captured.out

    stats = ['15', '70', '4', '5'] * 10
    j = 0
    for i in range(0, 50, 5):
        stats.insert(i, str(m.right_answers[j]))
        j += 1

    inputs = iter(stats)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    m.main()
    captured = capsys.readouterr()
    assert "The subject is classified as: Replicant" in captured.out
