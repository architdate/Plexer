# A script to rename movies and animes into Plex-friendly names

E.g `Series Name - SxxExx.mkv`

## Parameters

Specify First Split Point - Your first split point for getting the episode number.

Specify Second Split Point - Your second split point for getting the episode number.

Specify Series Name - Name of the series you want to rename to.

Specify Path (Be sure to escape special characters!!) - Path to the files you want to rename. 
This has two options -
1. Single Directory - When you only specify one directory path. E.g.
```
C:\Path\To\Series\
```
2. Muliple Directory - When you specify mulitple directory paths. E.g. 
```
C:\Path\To\Series\Season 1
C:\Path\To\Series\Season 2
```

Specify final episode - When only one directory is specified. Enter the episode number where you want the script to end renaming.

Specify where to cut the episodes - Episode number at which a new season will start. 

Specify Starting Season Number - Season number to start renaming from. Default is from S00

## Example - Single directory
```
C:\Path\To\Series\series.name.CRCNUM.EP01.SOME.INFO.mkv
C:\Path\To\Series\series.name.CRCNUM.EP02.SOME.INFO.mkv
C:\Path\To\Series\series.name.CRCNUM.EP03.SOME.INFO.mkv
C:\Path\To\Series\series.name.CRCNUM.EP04.SOME.INFO.mkv
C:\Path\To\Series\series.name.CRCNUM.EP05.SOME.INFO.mkv
C:\Path\To\Series\series.name.CRCNUM.EP06.SOME.INFO.mkv
```
Season 1 - EP01 & EP02

Season 2 - EP03 & EP04

Season 3 - EP05 & EP06

Specify First Split Point - EP

Specify Second Split Point - .S

Specify Series Name - series name

Specify Path - C:\\Path\\To\\Series

Specify final episode - 6

Specify where to cut the episodes - 3,5

Specify Starting Season Number - 1

## Example - Muliple directory
```
C:\Path\To\Series\Season 1\series.name.CRCNUM.EP01.SOME.INFO.mkv
C:\Path\To\Series\Season 1\series.name.CRCNUM.EP02.SOME.INFO.mkv
C:\Path\To\Series\Season 2\series.name.CRCNUM.EP03.SOME.INFO.mkv
C:\Path\To\Series\Season 2\series.name.CRCNUM.EP04.SOME.INFO.mkv
C:\Path\To\Series\Season 3\series.name.CRCNUM.EP05.SOME.INFO.mkv
C:\Path\To\Series\Season 3\series.name.CRCNUM.EP06.SOME.INFO.mkv
```

Specify First Split Point - EP

Specify Second Split Point - .S

Specify Series Name - series name

Specify Path - C:\\Path\\To\\Series\\Season 1, C:\\Path\\To\\Series\\Season 2, C:\\Path\\To\\Series\\Season 3

Specify where to cut the episodes - 3,5

Specify Starting Season Number - 1
