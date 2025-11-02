# Wichtige Befehle

- `git status`: Es wird der Status des Repositorys ausgegeben (welche Dateien wurden noch nicht hinzugefügt, welche Dateien wurden gelöscht, etc.) und ein etwaiger Tipp ausgegeben.
- `git log`: Dieser Befehl zeigt die bestehenden Commits an. Es werden zusätzliche Details (Autor, Datum, Commit-ID, etc.) ausgegeben.
- `git log --oneline`: Eine verkürzte einzeilige Ausgabe des Befehls `git log`.
- `git rm --cached -r ORDNER`: Löscht einen Ordner aus dem Repository (Achtung, der Ordner ist in vorherigen Commits natürlich noch enthalten). Zum Beispiel `git rm --cached -r node_modules`.
- `git rm --cached FILE`: Löscht eine Datei aus dem Repository (zB `git rm --cached .env`).

