# Global and local tests

## Description

These two Monte Carlo tests are used to assess the existence of global and local spatial structures. They can be used as an aid to interprete global and local components of spatial Principal Component Analysis (sPCA).

They rely on the decomposition of a data matrix X into global and local components using multiple regression on Moran's Eigenvector Maps (MEMs). They require a data matrix (X) and a list of weights derived from a connection network. X is regressed onto global MEMs (U+) in the global test and on local ones (U-) in the local test. One mean `R^2`

is obtained for each MEM, the k highest being summed to form the test statistic.

The reference distribution of these statistics are obtained by randomly permuting the rows of X.

```r
global.rtest(X, listw, k = 1, nperm = 499)
local.rtest(X, listw, k = 1, nperm = 499)
```

## Arguments

- `X`: a data matrix, with variables in columns
- `listw`: a list of weights of class `listw`. Can be obtained easily using the function `chooseCN`.
- `k`: integer: the number of highest `R^2` summed to form the test statistics
- `nperm`: integer: the number of randomisations to be performed.

## Details

This test is purely R code. A C or C++ version will be developped soon.

## Returns

An object of class `randtest`.

## References

Jombart, T., Devillard, S., Dufour, A.-B. and Pontier, D. Revealing cryptic spatial patterns in genetic variability by a new multivariate method. **Heredity**, 101 , 92--103.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## See Also

`chooseCN`, `spca`, `monmonier`

## Examples

```r
## Not run:

 data(sim2pop)
if(require(spdep)){
cn <- chooseCN(sim2pop@other$xy,ask=FALSE,type=1,plot=FALSE,res="listw")

# global test
Gtest <- global.rtest(sim2pop@tab,cn)
Gtest

# local test
Ltest <- local.rtest(sim2pop@tab,cn)
Ltest
}
## End(Not run)
```



