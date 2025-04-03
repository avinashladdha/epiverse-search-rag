# Compute minor allele frequency

```r
minorAllele(x)
```

## Arguments

- `x`: a genind object

## Description

This function computes the minor allele frequency for each locus in a genind object. To test if loci are polymorphic, see the function `isPoly`.

## Examples

```r
## Not run:


## LOAD DATA
data(nancycats)

## COMPUTE ALLELE FREQUENCIES
x <- nancycats
apply(tab(x, freq=TRUE),2,mean, na.rm=TRUE)

## GET MINOR ALLELE FREQUENCY
m.freq <- minorAllele(x)
m.freq
## End(Not run)
```

## See Also

`isPoly`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



