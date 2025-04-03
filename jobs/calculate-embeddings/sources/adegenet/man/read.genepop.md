# Reading data from Genepop

```r
read.genepop(file, ncode = 2L, quiet = FALSE)
```

## Arguments

- `file`: a character string giving the path to the file to convert, with the appropriate extension.
- `ncode`: an integer indicating the number of characters used to code an allele.
- `quiet`: logical stating whether a conversion message must be printed (TRUE,default) or not (FALSE).

## Returns

an object of the class `genind`

## Description

The function `read.genepop` reads Genepop data files (.gen) and convert them into a genind object.

## Details

Note: `read.genepop` is meant for DIPLOID DATA ONLY. Haploid data with the Genepop format can be read into R using `read.table` or `read.csv` after removing headers and 'POP' lines, and then converted using `df2genind`.

## Examples

```r
obj <- read.genepop(system.file("files/nancycats.gen",package="adegenet"))
obj
```

## References

Raymond M. & Rousset F, (1995). GENEPOP (version 1.2): population genetics software for exact tests and ecumenicism. **J. Heredity**, 86 :248-249

## See Also

`import2genind`, `df2genind`, `read.fstat`, `read.structure`, `read.genetix`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



