# Funktionen

Funktionen ermöglichen es, Code zu strukturieren und wiederzuverwenden. Es sind Codeblöcke, die eine bestimmte Aufgabe erfüllen.

```python
# Funktion definiert
def hallo():
    print("Hallo")

# Funktion aufrufen
hallo()
```

Funktionen können **mit Parameter** angepasst werden.

```python
# Funktion definiert
def hallo(name):
    print("Hallo", name)

# Funktion aufrufen
hallo("Max")
hallo("Dani")
```

Funktionen können auch Ergebnisse zurückliefern. Die Rückgabe erfolgt mittles **return**.

```python
# funktionen-rueckgabe.py

def ueberpruefe_zugriff(benutzername, passwort):
    if benutzername == "admin" and passwort == "p":
        return True
    else:
        return False


zugriff = ueberpruefe_zugriff("a", "b")

print("Zugriff:", zugriff)
print("Zugriff:", ueberpruefe_zugriff("admin", "p"))
```