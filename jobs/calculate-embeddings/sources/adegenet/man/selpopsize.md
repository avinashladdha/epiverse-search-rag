UTF-8

methods

# Select genotypes of well-represented populations

## Description

The function `selPopSize` checks the sample size of each population in a genind object and keeps only genotypes of populations having a given minimum size.

```r
## S4 method for signature 'genind'
selPopSize(x,pop=NULL,nMin=10)
```

## Arguments

- `x`: a genind object
- `pop`: a vector of characters or a factor giving the population of each genotype in 'x'. If not provided, seeked from x$pop.
- `nMin`: the minimum sample size for a population to be retained. Samples sizes strictly less than `nMin` will be discarded, those equal to or greater than `nMin` are kept.

## Returns

A genind object.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## See Also

`seploc`, `repool`

## Examples

```r
## Not run:

data(microbov)

table(pop(microbov))
obj <- selPopSize(microbov, n=50)

obj
table(pop(obj))
## End(Not run)
```



