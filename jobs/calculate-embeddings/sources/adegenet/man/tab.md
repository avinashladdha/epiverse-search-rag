 methods

# Access allele counts or frequencies

```r
tab(x, ...)

## S4 method for signature 'genind'
tab(x, freq = FALSE, NA.method = c("asis", "mean", "zero"), ...)

## S4 method for signature 'genpop'
tab(x, freq = FALSE, NA.method = c("asis", "mean", "zero"), ...)
```

## Arguments

- `x`: a genind or genpop object.
- `...`: further arguments passed to other methods.
- `freq`: a logical indicating if data should be transformed into relative frequencies (TRUE); defaults to FALSE.
- `NA.method`: a method to replace NA; asis: leave NAs as is; mean: replace by the mean allele frequencies; zero: replace by zero

## Returns

a matrix of integers or numeric

## Description

This accessor is used to retrieve a matrix of allele data. By default, a matrix of integers representing allele counts is returned. If `freq` is TRUE, then data are standardised as frequencies, so that for any individual and any locus the data sum to 1. The argument `NA.method` allows to replace missing data (NAs). This accessor replaces the previous function `truenames` as well as the function `makefreq`.

## Examples

```r
data(microbov)
head(tab(microbov))
head(tab(microbov,freq=TRUE))
```



