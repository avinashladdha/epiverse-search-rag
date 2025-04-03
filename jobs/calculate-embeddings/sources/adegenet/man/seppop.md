UTF-8

methods

# Separate genotypes per population

## Description

The function `seppop` splits a genind or a genlight object by population, returning a list of objects whose components each correspond to a population.

For genind objects, the output can either be a list of genind (default), or a list of matrices corresponding to the `@tab` slot.

```r
## S4 method for signature 'genind'
seppop(x,pop=NULL,truenames=TRUE,res.type=c("genind","matrix"),
  drop=FALSE, treatOther=TRUE, keepNA = FALSE, quiet=TRUE)

## S4 method for signature 'genlight'
seppop(x,pop=NULL, treatOther=TRUE, keepNA = FALSE, quiet=TRUE, ...)
```

## Arguments

- `x`: a genind object
- `pop`: a factor giving the population of each genotype in 'x' OR a formula specifying which strata are to be used when converting to a genpop object. If none provided, population factors are sought in x@pop, but if given, the argument prevails on x@pop.
- `truenames`: a logical indicating whether true names should be used (TRUE, default) instead of generic labels (FALSE); used if res.type is "matrix".
- `res.type`: a character indicating the type of returned results, a list of genind object (default) or a matrix of data corresponding to the 'tab' slots.
- `drop`: a logical stating whether alleles that are no longer present in a subset of data should be discarded (TRUE) or kept anyway (FALSE, default).
- `treatOther`: a logical stating whether elements of the `@other` slot should be treated as well (TRUE), or not (FALSE). See details in accessor documentations (`pop`).
- `keepNA`: If there are individuals with missing population information, should they be pooled into a separate population (TRUE), or excluded (FALSE, default).
- `quiet`: a logical indicating whether warnings should be issued when trying to subset components of the `@other` slot (TRUE), or not (FALSE, default).
- ``...``: further arguments passed to the genlight constructor.

## Returns

According to 'res.type': a list of genind object (default) or a matrix of data corresponding to the 'tab' slots.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## See Also

`seploc`, `repool`

## Examples

```r
## Not run:

data(microbov)
strata(microbov) <- data.frame(other(microbov))

obj <- seppop(microbov)
names(obj)

obj$Salers

### example using strata
obj2 <- seppop(microbov, ~coun/spe)
names(obj2)

obj2$AF_BI

#### example for genlight objects ####
x <- new("genlight", list(a=rep(1,1e3),b=rep(0,1e3),c=rep(1, 1e3)))
x

pop(x) # no population info
pop(x) <- c("pop1","pop2", "pop1") # set population memberships
pop(x)
seppop(x)
as.matrix(seppop(x)$pop1)[,1:20]
as.matrix(seppop(x)$pop2)[,1:20,drop=FALSE]
## End(Not run)
```



