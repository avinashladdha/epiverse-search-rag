# Reading data from GENETIX

```r
read.genetix(file = NULL, quiet = FALSE)
```

## Arguments

- `file`: a character string giving the path to the file to convert, with the appropriate extension.
- `quiet`: logical stating whether a conversion message must be printed (TRUE,default) or not (FALSE).

## Returns

an object of the class `genind`

## Description

The function `read.genetix` reads GENETIX data files (.gtx) and convert them into a genind object.

## Details

Note: `read.genetix` is meant for DIPLOID DATA ONLY. Haploid data with the GENETIX format can be read into R using `read.table` or `read.csv` after removing headers and 'POP' lines, and then converted using `df2genind`.

## Examples

```r
obj <- read.genetix(system.file("files/nancycats.gtx",package="adegenet"))
obj
```

## References

Belkhir K., Borsa P., Chikhi L., Raufaste N. & Bonhomme F. (1996-2004) GENETIX 4.05, logiciel sous Windows TM pour la genetique des populations. Laboratoire Genome, Populations, Interactions, CNRS UMR 5000, Universite de Montpellier II, Montpellier (France).

## See Also

`import2genind`, `df2genind`, `read.fstat`, `read.structure`, `read.genepop`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



