import subprocess
import os

# Ustalamy ścieżkę do main.py
main_script_path = os.path.join(os.path.dirname(__file__), '..', '..', 'main.py')

def test_addition():
    result = subprocess.run(['python', main_script_path, '2', '+', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8').strip() == '5', "Błąd w dodawaniu"

def test_subtraction():
    result = subprocess.run(['python', main_script_path, '10', '-', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8').strip() == '7', "Błąd w odejmowaniu"

def test_multiplication():
    result = subprocess.run(['python', main_script_path, '6', 'x', '4'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8').strip() == '24', "Błąd w mnożeniu"

def test_division():
    result = subprocess.run(['python', main_script_path, '12', '/', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8').strip() == '4.0', "Błąd w dzieleniu"

def test_division_by_zero():
    result = subprocess.run(['python', main_script_path, '12', '/', '0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert "ZeroDivisionError" in result.stderr.decode('utf-8'), "Dzielenie przez zero nie zgłasza błędu"

def test_invalid_operator():
    result = subprocess.run(['python', main_script_path, '12', '$', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert "KeyError" in result.stderr.decode('utf-8'), "Niepoprawny operator nie zgłasza błędu"

def test_non_numeric_input():
    result = subprocess.run(['python', main_script_path, 'abc', '+', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert "ValueError" in result.stderr.decode('utf-8'), "Niepoprawny argument wejściowy nie zgłasza błędu"

def test_no_arguments():
    result = subprocess.run(['python', main_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert "not enough values to unpack" in result.stderr.decode('utf-8'), "Brak argumentów nie zgłasza błędu"
