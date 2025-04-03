UTF-8

methods

# Separate data per locus

## Description

The function `seploc` splits an object (genind , genpop or genlight ) by marker. For genind and genpop objects, the method returns a list of objects whose components each correspond to a marker. For genlight objects, the methods returns blocks of SNPs.

```r
## S4 method for signature 'genind'
seploc(x,truenames=TRUE,res.type=c("genind","matrix"))
## S4 method for signature 'genpop'
seploc(x,truenames=TRUE,res.type=c("genpop","matrix"))
## S4 method for signature 'genlight'
seploc(x, n.block=NULL, block.size=NULL, random=FALSE,
       parallel=FALSE, n.cores=NULL)
```

## Arguments

- `x`: a genind or a genpop object.
- `truenames`: a logical indicating whether true names should be used (TRUE, default) instead of generic labels (FALSE).
- `res.type`: a character indicating the type of returned results, a genind or genpop object (default) or a matrix of data corresponding to the 'tab' slot.
- `n.block`: an integer indicating the number of blocks of SNPs to be returned.
- `block.size`: an integer indicating the size (in number of SNPs) of the blocks to be returned.
- `random`: should blocks be formed of contiguous SNPs, or should they be made or randomly chosen SNPs.
- `parallel`: a logical indicating whether multiple cores -if available- should be used for the computations (TRUE, default), or not (FALSE); requires the package `parallel` to be installed.
- `n.cores`: if `parallel` is TRUE, the number of cores to be used in the computations; if NULL, then the maximum number of cores available on the computer is used.

## Returns

The function `seploc` returns an list of objects of the same class as the initial object, or a list of matrices similar to x$tab.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## See Also

`seppop`, `repool`

## Examples

```r
## Not run:

## example on genind objects
data(microbov)

# separate all markers
obj <- seploc(microbov)
names(obj)

obj$INRA5


## example on genlight objects
x <- glSim(100, 1000, 0, ploidy=2) # simulate data
x <- x[,order(glSum(x))] # reorder loci by frequency of 2nd allele
glPlot(x, main="All data") # plot data
foo <- seploc(x, n.block=3) # form 3 blocks
foo
glPlot(foo[[1]], main="1st block") # plot 1st block
glPlot(foo[[2]], main="2nd block") # plot 2nd block
glPlot(foo[[3]], main="3rd block") # plot 3rd block

foo <- seploc(x, block.size=600, random=TRUE) # split data, randomize loci
foo # note the different block sizes
glPlot(foo[[1]])
## End(Not run)
```



