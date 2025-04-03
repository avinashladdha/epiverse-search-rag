UTF-8

# Importing data from an alignement of sequences to a genind object

## Description

These functions take an alignement of sequences and translate SNPs into a genind object. Note that only polymorphic loci are retained.

Currently, accepted sequence formats are:

- DNAbin (ape package): function DNAbin2genind

- alignment (seqinr package): function alignment2genind

```r
DNAbin2genind(x, pop=NULL, exp.char=c("a","t","g","c"), polyThres=1/100)

alignment2genind(x, pop=NULL, exp.char=c("a","t","g","c"), na.char="-",
                 polyThres=1/100)
```

## Arguments

- `x`: an object containing aligned sequences.
- `pop`: an optional factor giving the population to which each sequence belongs.
- `exp.char`: a vector of single character providing expected values; all other characters will be turned to NA.
- `na.char`: a vector of single characters providing values that should be considered as NA. If not NULL, this is used instead of `exp.char`.
- `polyThres`: the minimum frequency of a minor allele for a locus to be considered as polymorphic (defaults to 0.01).

## Returns

an object of the class genind

## See Also

`import2genind`, `read.genetix`, `read.fstat`, `read.structure`, `read.genepop`, `DNAbin`, `as.alignment`.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

data(woodmouse)
x <- DNAbin2genind(woodmouse)
x
genind2df(x)
## End(Not run)


if(require(seqinr)){
mase.res   <- read.alignment(file=system.file("sequences/test.mase",package="seqinr"),
format = "mase")
mase.res
x <- alignment2genind(mase.res)
x
locNames(x) # list of polymorphic sites
genind2df(x)

## look at Euclidean distances
D <- dist(tab(x))
D

## summarise with a PCoA
pco1 <- dudi.pco(D, scannf=FALSE,nf=2)
scatter(pco1, posi="bottomright")
title("Principal Coordinate Analysis\n-based on proteic distances-")

}
```



