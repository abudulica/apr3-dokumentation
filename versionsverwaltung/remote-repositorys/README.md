# Remote-Repositorys

## Allgemeines

Bei einem Git-Repository kann auch ein entferntes Repository hinzugefügt werden. Dieses Remote-Repository kann zum Beispiel bei GitHub (https://www.github.com) gespeichert werden.

GitHub unterstützt die Erstellung von **privaten** und **öffentlichen** Repositorys. Private Repositorys können nur von den berechtigten Personen verwaltet werden bzw. können nur berechtigte Personen den Inhalt verändern. Öffentliche Repositorys sind für **alle** lesbar.

:::danger
Falls in einem Repository sensible Daten gespeichert wurden, können diese auch in älteren Commits ersichtlich sein.
:::

## Lokales Repository vorhanden

Falls bereits ein lokales Repository besteht, so kann mittels

```
git remote add origin ssh-url.git
```

ein entferntes Repository hinzugefügt werden (zB git@github.com:perasser/apr2.git).

![Remote-Adresse](assets/ssh-link.png)

:::tip
Da ein `SSH`-Schlüssel verwendet wird, muss der SSH-Link hinzugefügt werden. 
:::

Das Remote-Repository muss nur einmal hinzugefügt werden. Mittels `git remote -v` können die vorhandenen Remote-Repositorys angezeigt werden.

Alle **vorhandenen Commits** werden mittels `git push` zum Remote-Repository übertragen. Ein "leeres Repository" (ohne Commits) wird nicht übertragen, daher muss ein Commit erstellt werden. Der erste `Push`-Vorgang wird mittels `git push -u origin main` durchgeführt - anschließend ist ein `git push` ausreichend.

Man kann lokal beim Repositoy arbeiten und beliebig oft ein `Push` durchführen (zB am Ende der Arbeit).

## Remote-Repository vorhanden

Bei einem vorhandenen Remote-Repository wird der `SSH-Link` kopiert und mittels

```
git clone ssh-url.git
```

das Repository im akutellen Ordner als Unterordner mit dem Namen des Repositorys erstellt. Wird also eine Eingabeaufforderung im Ordner `Git` geöffnet und anschließend der Befehl `git clone git@github.com:perasser/apr2.git` aufgerufen, so wird ein Unterverzeichnis namens apr2 im Ordner Git erstellt.

Möchte man einen anderen Ordner wählen, so muss der `clone`-Befehl folgendermaßen abgesendet werden:

```
git clone git@github.com:perasser/apr2.git doku
```

Dadurch wird im Ordner Git ein Unterordner namens doku erstellt.

## Commits synchronisieren

Die Commits werden mittels `git push` hinaufgeladen und mittels `git pull` heruntergeladen.

Wenn in einem Repository entfernt und lokal Dateien verändert wurden, müssen diese Veränderungen zusammengeführt werden. Bei der Veränderung von unterschiedlichen Dateien kann mittels `git pull` und `git push` eine Synchronisation erfolgen. Wurden jedoch **gleiche** Datein verändert, so tritt ein **Merge-Konflikt** auf (auf der Eingabeaufforderung ist das Wort `CONFLICT` ersichtlich). Git gibt den Hinweis auf den Befehl `git merge` aus.

Ein Merge-Konflikt kann in einem Merge-Editor (in `VS Code` im Bereich `Source Control`) gelöst werden. Man entscheidet sich für die entfernte oder die lokale Veränderung. Ohne Merge-Editor kann die Datei auch selbst bearbeitet werden, es muss auf die `>>>>>>>>>>` bzw. `<<<<<<<<<<` entsprechend geachtet werden.

