# Git-Repositorys

## Allgemeines

Ein Git-Repository unterscheidet grundsätzlich zwischen drei Bereichen:

- `working copy`
- `staging area`
- `local repository`

![Git-Repository](assets/basic-remote-workflow.png)[^1]

Im **working copy** befinden sich alle Dateien eines Verzeichnisses (zB README.md, index.html, Bilder, Word-Dateien, etc.). Möchte man den Inhalt eines Ordners versionieren ("unter Git stellen"), so müssen die Dateien zur **staging area** hinzugefügt werden (welche Dateien sollen verwaltet werden). Nach einem Commit werden die verwalteten Dateien in einem **repository** gespeichert.

## Repository erstellen

Ein Repository darf nur **ein einziges Mal** erstellt werden.

Lokal bedeutet dies, dass das Repository in einem zuvor erstellten Ordner mittels

```powershell
git init
```

erstellt wird.

Bei GitHub erfolgt die Initialisierung mittels **Erstellung einer zB README**-Datei.

![Init auf GitHub](assets/github-init.png)

:::danger
**Niemals** wird das Repository lokal mit `git init` und remote mit `Initialize this repository with ...` erstellt! Dies wären zwei unterschiedliche Repositorys!
:::

## Erstellung lokal und remote

:::danger
Der hier gezeigte Vorgang ist FALSCH!!!
:::

1. Repository wird lokal erstellt:

Im `Git`-Verzeichnis wird ein Ordner namens `falsch` erstellt und in diesem Ordner wird

```powershell
git init
```

aufgerufen.

2. Im Ordner `falsch` wird eine beliebige Datei erstellt und anschließnd werden folgende Befehle ausgeführt:

```powershell
git add .
git commit -m "add file"
```

3. In GitHub wird ein Repository namens "falsch" mit "Initialize this repository with ... README" erstellt und beim lokalen Repository als remote hinzugefügt:

![Repository online erstellt und initialisiert](assets/repository-online-initialisiert.png)

```powershell
git remote add origin git@github.com:perasser/falsch.git
```

4. Beim Versuch das lokale Repository zum Online-Repository hinzuzufügen, wird nun ein Fehler auftreten.

```powershell
git push
```

![Nicht zusammenpassende Repositorys](assets/repository-unrelated-history.png)

:::tip
Dieser Konflikt lässt sich standardmäßig auch mittels mehrmaligem `git pull` und `git push` nicht  lösen.
:::

[^1]: **SaaS.group GmbH**. Introduction to Remote Repositories. URL: https://www.git-tower.com/learn/git/ebook/en/command-line/remote-repositories/introduction, Datum: 6. Nov. 2024.
