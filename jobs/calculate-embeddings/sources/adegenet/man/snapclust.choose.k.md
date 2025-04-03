# Choose the number of clusters for snapclust using AIC, BIC or AICc

```r
snapclust.choose.k(max, ..., IC = AIC, IC.only = TRUE)
```

## Arguments

- `max`: An integer indicating the maximum number of clusters to seek; `snapclust` will be run for all k from 2 to max.
- `...`: Arguments passed to `snapclust`.
- `IC`: A function computing the information criterion for `snapclust` objects. Available statistics are `AIC` (default), `AICc`, and `BIC`.
- `IC.only`: A logical (TRUE by default) indicating if IC values only should be returned; if `FALSE`, full `snapclust` objects are returned.

## Description

This function implements methods for investigating the optimal number of genetic clusters ('k') using the fast maximum-likelihood genetic clustering approach described in Beugin et al (2018). The method runs `snapclust` for varying values of 'k', and computes the requested summary statistics for each clustering solution to assess goodness of fit. The method is fully documented in a dedicated tutorial which can be accessed using `adegenetTutorial("snapclust")`.

## Details

The method is described in Beugin et al (2018) A fast likelihood solution to the genetic clustering problem. Methods in Ecology and Evolution tools:::Rd_expr_doi("10.1111/2041-210X.12968") . A dedicated tutorial is available by typing `adegenetTutorial("snapclust")`.

## See Also

`snapclust` to generate individual clustering solutions, and `BIC.snapclust` for computing BIC for `snapclust` objects.

## Author(s)

Thibaut Jombart thibautjombart@gmail.com



