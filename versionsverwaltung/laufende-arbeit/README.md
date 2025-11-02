---
title: 'Laufende Arbeit'
---
# Laufende Arbeit

## Allgemeines

Wurde das Projekt bereits erfolgreich erstellt, so kann ab diesem Zeitpunkt jederzeit eine Datei (oder mehrere) zum Git-Repository hinzugefügt werden.

Beim Hinzufügen werden die Dateien in einem `staging`-Bereich gespeichert. Hierbei soll beachtet werden, dass sich logisch zusammenhängende Dateien im `staging`-Bereich befinden. Bei einem größeren Projekt werden alle Dateien für die Benutzerverwaltung gemeinsam bearbeitet und getrennt von zB einem Kontaktformular gespeichert.

Das Hinzufügen **einer einzigen Datei** erfolgt mit:

```
git add dateiname
```

Müssen **mehrere/alle Dateien in einem Ordner** gleichzeigt hinzugefügt werden, so erfolgt dies mit

```
git add .
```

Die Speicherung der logischen Gruppe (des `staging`-Bereichs) erfolgt mittels eines Commits mit einer sinnvollen Nachricht:

```
git commit -m "add firstname to contact form"
```

## Dateien/Ordner vom Repository ausschließen

Möchte man verhindern, dass bei einem `git add .` bestimmte Ordner/Dateien zum Repository hinzugefügt werden, so muss eine `.gitignore`-Datei erstellt werden. Diese Datei könnte zum Beispiel folgenden Inhalt aufweisen:

```
ordnername
dateiname
```

Die Datei `.gitignore` hat keinen Dateinamen (nur eine Erweiterung) und kann am einfachsten in einem Editor erstellt werden.

:::tip
Es können auch Platzhalter (`*`) verwendet werden (zB `*.py` schließt alle Python-Dateien aus).
:::

## Letzten Änderungen zwischenspeichern/verwerfen

Die zuletzt durchgeführen Veränderungen können zwischengespeichert werden. Dies erfolgt mittels

```
git stash
```

:::danger
Arbeitsauftrag!!!
Bitte in der Dokumentation den Vorgang mit `git stash` ... beschreiben und abbilden.
:::