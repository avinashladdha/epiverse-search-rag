# Reading data from Fstat

```r
read.fstat(file, quiet = FALSE)
```

## Arguments

- `file`: a character string giving the path to the file to convert, with the appropriate extension.
- `quiet`: logical stating whether a conversion message must be printed (TRUE,default) or not (FALSE).

## Returns

an object of the class `genind`

## Description

The function `read.fstat` reads Fstat data files (.dat) and convert them into a genind object.

## Details

Note: `read.fstat` is meant for DIPLOID DATA ONLY. Haploid data with the Hierfstat format can be read into R using `read.table` or `read.csv` after removing headers and 'POP' lines, and then converted using `df2genind`.

## Examples

```r
obj <- read.fstat(system.file("files/nancycats.dat",package="adegenet"))
obj
```

## References

Fstat (version 2.9.3). Software by Jerome Goudet. http://www2.unil.ch/popgen/softwares/fstat.htm

## See Also

`import2genind`, `df2genind`, `read.genetix`, `read.structure`, `read.genepop`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



