# Verzweigung

Unterscheidungen können mittels `if`, `elif` und `else` durchgeführt werden.

## Beispiel "Zahl überprüfen"

```python
# verzweigung.py

zahl = 10 # Zahl vom Benutzer

if zahl > 5:
    print("Die Zahl ist größer als 5.")
elif zahl == 5:
    print("Die Zahl ist 5.")
else:
    print("Die Zahl ist kleiner als 5.")
```

## Beispiel "Passwort überprüfen"

```python
passwort = "test2"

if passwort == "test":
    print("Das Passwort ist korrekt.")
else:
    print("Das Passwort ist falsch.")
```

## Beispiel "Passwort und Benutzername überprüfen"

```python
benutzername = "mmuster"
passwort = "test"

if passwort == "test" and benutzername == "mmuster":
    print("Das ist korrekt")
else:
    print("Das ist falsch")
```
