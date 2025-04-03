# Reading data from STRUCTURE

```r
read.structure(
  file,
  n.ind = NULL,
  n.loc = NULL,
  onerowperind = NULL,
  col.lab = NULL,
  col.pop = NULL,
  col.others = NULL,
  row.marknames = NULL,
  NA.char = "-9",
  pop = NULL,
  sep = NULL,
  ask = TRUE,
  quiet = FALSE
)
```

## Arguments

- `file`: a character string giving the path to the file to convert, with the appropriate extension.
- `n.ind`: an integer giving the number of genotypes (or 'individuals') in the dataset
- `n.loc`: an integer giving the number of markers in the dataset
- `onerowperind`: a STRUCTURE coding option: are genotypes coded on a single row (TRUE), or on two rows (FALSE, default)
- `col.lab`: an integer giving the index of the column containing labels of genotypes. '0' if absent.
- `col.pop`: an integer giving the index of the column containing population to which genotypes belong. '0' if absent.
- `col.others`: an vector of integers giving the indexes of the columns containing other informations to be read. Will be available in @other of the created object.
- `row.marknames`: an integer giving the index of the row containing the names of the markers. '0' if absent.
- `NA.char`: the character string coding missing data. "-9" by default. Note that in any case, series of zero (like "000") are interpreted as NA too.
- `pop`: an optional factor giving the population of each individual.
- `sep`: a character string used as separator between alleles.
- `ask`: a logical specifying if the function should ask for optional informations about the dataset (TRUE, default), or try to be as quiet as possible (FALSE).
- `quiet`: logical stating whether a conversion message must be printed (TRUE,default) or not (FALSE).

## Returns

an object of the class `genind`

## Description

The function `read.structure` reads STRUCTURE data files (.str ou .stru) and convert them into a genind object. By default, this function is interactive and asks a few questions about data content. This can be disabled (for optional questions) by turning the 'ask' argument to FALSE. However, one has to know the number of genotypes, of markers and if genotypes are coded on a single or on two rows before importing data.

## Details

Note: `read.structure` is meant for DIPLOID DATA ONLY. Haploid data with the STRUCTURE format can easily be read into R using `read.table` or `read.csv` and then converted using `df2genind`.

## Examples

```r
obj <- read.structure(system.file("files/nancycats.str",package="adegenet"),
  onerowperind=FALSE, n.ind=237, n.loc=9, col.lab=1, col.pop=2, ask=FALSE)

obj
```

## References

Pritchard, J.; Stephens, M. & Donnelly, P. (2000) Inference of population structure using multilocus genotype data. **Genetics**, 155 : 945-959

## See Also

`import2genind`, `df2genind`, `read.fstat`, `read.genetix`, `read.genepop`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



