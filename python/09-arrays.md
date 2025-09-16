# Arrays (Listen)

In Variablen können standardmäßig nur einzelne Werte gespeichert werden. Möchte mehrere Werte speichern, so benötigt man **Arrays** bzw. **Listen**.

:::note
**Listen** sind geordnete Sammlungen von Elementen, die nicht unbedingt vom selben Datentyp sein müssen. (Dies gilt nicht für alle Programmiersprachen - viele Programmiersprachen erlauben nur einen Datentyp.)
:::

```python
# arrays-listen.py

fruits = ["Apfel", "Banane", "Kirsche"]
fruits.append("Birne")

print(fruits)
```

Der Zugriff auf ein Array erfolgt beginnend mit der Position 0 bis zur Position (n - 1) also Anzahl der Elemente - 1.

```python
print(fruits[0]) # das erste Element im Array/in der Liste
```

## Hausübung

Bitte die folgenden Funktionen dokumentieren:

- `insert()`
- `pop()`
- `remove()`
- `len()`
- Teilbereiche (slicing)

