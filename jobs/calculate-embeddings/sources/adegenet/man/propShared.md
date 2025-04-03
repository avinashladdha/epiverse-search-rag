UTF-8

# Compute proportion of shared alleles

## Description

The function `propShared` computes the proportion of shared alleles in a set of genotypes (i.e. from a genind

object). Current implementation works for any level of ploidy.

```r
propShared(obj)
```

## Arguments

- `obj`: a genind object.

 

## Details

Computations of the numbers of shared alleles are done in C. Proportions are computed from all available data, i.e. proportion can be computed as far as there is at least one typed locus in common between two genotypes.

## Returns

Returns a matrix of proportions

## See Also

`dist.genpop`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

## make a small object
data(microbov)
obj <- microbov[1:5, loc = locNames(microbov)[1:2]]

## verify results
propShared(obj)
genind2df(obj,sep="|")

## Use this similarity measure inside a PCoA
##  ! This is for illustration only !
## the distance should be rendered Euclidean before
## (e.g. using cailliez from package ade4).
matSimil <- propShared(microbov)
matDist <- exp(-matSimil)
D <- cailliez(as.dist(matDist))
pcoa1 <- dudi.pco(D,scannf=FALSE,nf=3)
s.class(pcoa1$li,microbov$pop,lab=popNames(microbov))
## End(Not run)
```



