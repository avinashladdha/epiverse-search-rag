UTF-8

# Spatial principal component analysis

## Description

 These functions implement the spatial principal component analysis (sPCA). The function `spca` is a generic with methods for:

 * `matrix`: only numeric values are accepted
 * `data.frame`: same as for matrices
 * `genind`: any genind object is accepted
 * `genpop`: any genpop object is accepted

The core computation use `multispati` from the `adespatial` package.

Besides the set of `spca` functions, other functions include:

 * `print.spca`: prints the spca content
 * `summary.spca`: gives variance and autocorrelation statistics
 * `plot.spca`: usefull graphics (connection network, 3 different representations of map of scores, eigenvalues barplot and decomposition)
 * `screeplot.spca`: decomposes spca eigenvalues into variance and autocorrelation
 * `colorplot.spca`: represents principal components of sPCA in space using the RGB system.

 A tutorial on sPCA can be opened using:

 `adegenetTutorial(which="spca")`.

```r
spca(...)

## Default S3 method:
spca(x, ...)

## S3 method for class 'matrix'
spca(x, xy = NULL, cn = NULL, matWeight = NULL,
            center = TRUE, scale = FALSE, scannf = TRUE,
            nfposi = 1, nfnega = 1,
            type = NULL, ask = TRUE,
            plot.nb = TRUE, edit.nb = FALSE,
            truenames = TRUE,
            d1 = NULL, d2 = NULL, k = NULL,
            a = NULL, dmin = NULL, ...)

## S3 method for class 'data.frame'
spca(x, xy = NULL, cn = NULL, matWeight = NULL,
            center = TRUE, scale = FALSE, scannf = TRUE,
            nfposi = 1, nfnega = 1,
            type = NULL, ask = TRUE,
            plot.nb = TRUE, edit.nb = FALSE,
            truenames = TRUE,
            d1 = NULL, d2 = NULL, k = NULL,
            a = NULL, dmin = NULL, ...)

## S3 method for class 'genind'
spca(obj, xy = NULL, cn = NULL, matWeight = NULL,
            scale = FALSE, scannf = TRUE,
            nfposi = 1, nfnega = 1,
            type = NULL, ask = TRUE,
            plot.nb = TRUE, edit.nb = FALSE,
            truenames = TRUE,
            d1 = NULL, d2 = NULL, k = NULL,
            a = NULL, dmin = NULL, ...)

## S3 method for class 'genpop'
spca(obj, xy = NULL, cn = NULL, matWeight = NULL,
            scale = FALSE, scannf = TRUE,
            nfposi = 1, nfnega = 1,
            type = NULL, ask = TRUE,
            plot.nb = TRUE, edit.nb = FALSE,
            truenames = TRUE,
            d1 = NULL, d2 = NULL, k = NULL,
            a = NULL, dmin = NULL, ...)


## S3 method for class 'spca'
print(x, ...)

## S3 method for class 'spca'
summary(object, ..., printres=TRUE)

## S3 method for class 'spca'
plot(x, axis = 1, useLag=FALSE, ...)

## S3 method for class 'spca'
screeplot(x, ..., main=NULL)

## S3 method for class 'spca'
colorplot(x, axes=1:ncol(x$li), useLag=FALSE, ...)
```

## Arguments

- `x`: a `matrix` or a `data.frame` of numeric values, with individuals in rows and variables in columns; categorical variables with a binary coding are acceptable too; for `print` and plotting functions, a spca object.
- `obj`: a `genind` or `genpop` object.
- `xy`: a matrix or data.frame with two columns for x and y coordinates. Seeked from obj$other$xy if it exists when xy is not provided. Can be NULL if a `nb` object is provided in `cn`.
    
    Longitude/latitude coordinates should be converted first by a given projection (see 'See Also' section).
- `cn`: a connection network of the class 'nb' (package spdep). Can be NULL if xy is provided. Can be easily obtained using the function chooseCN (see details).
- `matWeight`: a square matrix of spatial weights, indicating the spatial proximities between entities. If provided, this argument prevails over `cn` (see details).
- `center`: a logical indicating whether data should be centred to a mean of zero; used implicitely for genind or genpop objects.
- `scale`: a logical indicating whether data should be scaled to unit variance (TRUE) or not (FALSE, default).
- `scannf`: a logical stating whether eigenvalues should be chosen interactively (TRUE, default) or not (FALSE).
- `nfposi`: an integer giving the number of positive eigenvalues retained ('global structures').
- `nfnega`: an integer giving the number of negative eigenvalues retained ('local structures').
- `type`: an integer giving the type of graph (see details in `chooseCN` help page). If provided, `ask` is set to FALSE.
- `ask`: a logical stating whether graph should be chosen interactively (TRUE,default) or not (FALSE).
- `plot.nb`: a logical stating whether the resulting graph should be plotted (TRUE, default) or not (FALSE).
- `edit.nb`: a logical stating whether the resulting graph should be edited manually for corrections (TRUE) or not (FALSE, default).
- `truenames`: a logical stating whether true names should be used for 'obj' (TRUE, default) instead of generic labels (FALSE)
- `d1`: the minimum distance between any two neighbours. Used if `type=5.`
- `d2`: the maximum distance between any two neighbours. Used if `type=5`.
- `k`: the number of neighbours per point. Used if `type=6`.
- `a`: the exponent of the inverse distance matrix. Used if `type=7`.
- `dmin`: the minimum distance between any two distinct points. Used to avoid infinite spatial proximities (defined as the inversed spatial distances). Used if `type=7`.
- `object`: a `spca` object.
- `printres`: a logical stating whether results should be printed on the screen (TRUE, default) or not (FALSE).
- `axis`: an integer between 1 and (nfposi+nfnega) indicating which axis should be plotted.
- `main`: a title for the screeplot; if NULL, a default one is used.
- ``...``: further arguments passed to other methods.
- `axes`: the index of the columns of X to be represented. Up to three axes can be chosen.
- `useLag`: a logical stating whether the lagged components (`x$ls`) should be used instead of the components (`x$li`).

## Details

The spatial principal component analysis (sPCA) is designed to investigate spatial patterns in the genetic variability. Given multilocus genotypes (individual level) or allelic frequency (population level) and spatial coordinates, it finds individuals (or population) scores maximizing the product of variance and spatial autocorrelation (Moran's I). Large positive and negative eigenvalues correspond to global and local structures.

Spatial weights can be obtained in several ways, depending how the arguments `xy`, `cn`, and `matWeight` are set.

When several acceptable ways are used at the same time, priority is as follows:

 `matWeight` > `cn` > `xy`

## Returns

The class `spca` are given to lists with the following components:

 - **eig**: a numeric vector of eigenvalues.

 - **nfposi**: an integer giving the number of global structures retained.

 - **nfnega**: an integer giving the number of local structures retained.

 - **c1**: a data.frame of alleles loadings for each axis.

 - **li**: a data.frame of row (individuals or populations) coordinates onto the sPCA axes.

 - **ls**: a data.frame of lag vectors of the row coordinates; useful to clarify maps of global scores .

 - **as**: a data.frame giving the coordinates of the PCA axes onto the sPCA axes.

 - **call**: the matched call.

 - **xy**: a matrix of spatial coordinates.

 - **lw**: a list of spatial weights of class `listw`.

Other functions have different outputs:

- `summary.spca` returns a list with 3 components: `Istat` giving the null, minimum and maximum Moran's I values; `pca` gives variance and I statistics for the principal component analysis; `spca` gives variance and I statistics for the sPCA.

- `plot.spca` returns the matched call.

- `screeplot.spca` returns the matched call.

## References

Jombart, T., Devillard, S., Dufour, A.-B. and Pontier, D. Revealing cryptic spatial patterns in genetic variability by a new multivariate method. **Heredity**, 101 , 92--103.

Wartenberg, D. E. (1985) Multivariate spatial correlation: a method for exploratory geographical analysis. **Geographical Analysis**, 17 , 263--283.

Moran, P.A.P. (1948) The interpretation of statistical maps. **Journal of the Royal Statistical Society, B**

10 , 243--251.

Moran, P.A.P. (1950) Notes on continuous stochastic phenomena. **Biometrika**, 37 , 17--23.

de Jong, P. and Sprenger, C. and van Veen, F. (1984) On extreme values of Moran's I and Geary's c. **Geographical Analysis**, 16 , 17--24.

## See Also

`spcaIllus` and `rupica` for datasets illustrating the sPCA

 `global.rtest` and `local.rtest`

 `chooseCN`, `multispati`

 `convUL`, from the package 'PBSmapping' to convert longitude/latitude to UTM coordinates.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## data(spcaIllus) illustrates the sPCA
## see ?spcaIllus
##
## Not run:

example(spcaIllus)
example(rupica)
## End(Not run)
```



