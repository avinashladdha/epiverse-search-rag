# Convert a genind object to a data.frame.

```r
genind2df(x, pop = NULL, sep = "", usepop = TRUE, oneColPerAll = FALSE)
```

## Arguments

- `x`: a genind object
- `pop`: an optional factor giving the population of each individual.
- `sep`: a character string separating alleles. See details.
- `usepop`: a logical stating whether the population (argument `pop` or `x@pop` should be used (TRUE, default) or not (FALSE)).
- `oneColPerAll`: a logical stating whether or not alleles should be split into columns (defaults to `FALSE`). This will only work with data with consistent ploidies.

## Returns

a data.frame of raw allelic data, with individuals in rows and loci in column

## Description

The function `genind2df` converts a genind back to a data.frame of raw allelic data.

## Examples

```r
## simple example
df <- data.frame(locusA=c("11","11","12","32"),
locusB=c(NA,"34","55","15"),locusC=c("22","22","21","22"))
row.names(df) <- .genlab("genotype",4)
df

obj <- df2genind(df, ploidy=2, ncode=1)
obj
obj@tab


## converting a genind as data.frame
genind2df(obj)
genind2df(obj, sep="/")
```

## See Also

`df2genind`, `import2genind`, `read.genetix`, `read.fstat`, `read.structure`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



