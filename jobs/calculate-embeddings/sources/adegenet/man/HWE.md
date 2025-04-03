UTF-8

# Hardy-Weinberg Equilibrium test for multilocus data

## Description

The function `HWE.test` is a generic function to perform Hardy-Weinberg Equilibrium tests defined by the `genetics` package. adegenet proposes a method for `genind` objects.

The output can be of two forms:

- a list of tests (class `htest`) for each locus-population combinaison

- a population x locus matrix containing p-values of the tests

```r
## S3 method for class 'genind'
HWE.test(x,pop=NULL,permut=FALSE,nsim=1999,hide.NA=TRUE,res.type=c("full","matrix"))
```

## Arguments

- `x`: an object of class `genind`.
- `pop`: a factor giving the population of each individual. If NULL, pop is seeked from x$pop.
- `permut`: a logical passed to `HWE.test` stating whether Monte Carlo version (TRUE) should be used or not (FALSE, default).
- `nsim`: number of simulations if Monte Carlo is used (passed to `HWE.test`).
- `hide.NA`: a logical stating whether non-tested loci (e.g., when an allele is fixed) should be hidden in the results (TRUE, default) or not (FALSE).
- `res.type`: a character or a character vector whose only first argument is considered giving the type of result to display. If "full", then a list of complete tests is returned. If "matrix", then a matrix of p-values is returned.

## Details

Monte Carlo procedure is quiet computer-intensive when large datasets are involved. For more precision on the performed test, read `HWE.test` documentation (`genetics` package).

## Returns

Returns either a list of tests or a matrix of p-values. In the first case, each test is designated by locus first and then by population. For instance if `res` is the "full" output of the function, then the test for population "PopA" at locus "Myloc" is given by res$Myloc$PopA. If `res` is a matrix of p-values, populations are in rows and loci in columns. P-values are given for the upper-tail: they correspond to the probability that an oberved chi-square statistic as high as or higher than the one observed occured under H0 (HWE).

In all cases, NA values are likely to appear in fixed loci, or entirely non-typed loci.

## See Also

`HWE.test` in the `genetics` package, `chisq.test`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

data(nancycats)
obj <- nancycats
if(require(genetics)){
obj.test <- HWE.test(obj)

# pvalues matrix to have a preview
HWE.test(obj,res.type="matrix")

#more precise view to...
obj.test$fca90$P10
}
## End(Not run)
```



