########################
## WIPO Latex-Vorlage ##
########################


## Vorbereitung ##

1) Installation der Hintergrundprogramme (https://de.wikibooks.org/wiki/LaTeX/_Installation)

2) Installation eines Editors, z.B.: TexStudio (https://de.wikipedia.org/wiki/TeXstudio)

	Wichtige Einstellungen:	* Standardcompiler: pdfLaTex
				* Standard Bibliographieprogramm: Biber
				* Encoding: UTF-8

3) Installation von JabRef zur Literaturverwaltung (https://de.wikibooks.org/wiki/LaTeX/_Installation)


## Get started ##

1) Öffnen der Hauptdatei ''00_Seminar_Abschlussarbeit''

2) Ausfüllen des gekennzeichneten Bereichs


## Seminararbeit ##

* Nutze die Datei ''03a_Seminar_work_main_text'' für die Seminararbeit.
* Die anderen include-Befehle (Einleitung, Kapitel 1 etc.) in der Hauptdatei können auskommentiert werden (müssen aber nicht -> funktioniert auch so)


## Abschlussarbeit ##

* Nutze die Datei ''03_Einleitung'', ''04_Kapitel_1'' etc. für die einzelnen Teile der Abschlussarbeit.
* Weitere Teile müssen ggf. erstellt und in der Hauptdatei über den \include-Befehl eingebunden werden.
* \include{03a_Seminar_work_main_text} in der Hauptdatei kann auskommentiert werden (muss aber nicht -> funktioniert auch so)


## Issues

* Zur Aktualisierung des Literaturverzeichnisses ist es mitunter notwendig die .bbl, .bak bzw. .aux Dateien zu löschen