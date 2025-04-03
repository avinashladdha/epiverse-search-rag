# Monte Carlo test for sPCA

```r
spca_randtest(x, nperm = 499, p = 0.05)
```

## Arguments

- `x`: A `spca` object.
- `nperm`: The number of permutations to be used for the test.
- `p`: p value to use for Bonferroni correction.

## Returns

A list with two objects of the class 'randtest' (see `as.randtest`), the first one for 'global' structures (positivie autocorrelation) and the second for 'local' structures (negative autocorrelation).

## Description

The function `spca_randtest` implements Monte-Carlo tests for the presence of significant spatial structures in a sPCA object. Two tests are run, for global (positive autocorrelation) and local (negative autocorrelation) structures, respectively. The test statistics used are the sum of the absolute values of the corresponding eigenvalues.

## Examples

```r
## Not run:

## Load data
data(sim2pop)

## Make spca
spca1 <- spca(sim2pop, type = 1, scannf = FALSE, plot.nb = FALSE)

spca1
plot(spca1)

## run tests (use more permutations in practice, e.g. 999)
tests <- spca_randtest(spca1, nperm = 49)

## check results
tests
plot(tests[[1]]) # global structures
## End(Not run)
```

## Author(s)

Original code by Valeria Montano adapted by Thibaut Jombart.



