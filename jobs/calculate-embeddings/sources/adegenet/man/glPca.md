UTF-8

# Principal Component Analysis for genlight objects

## Description

These functions implement Principal Component Analysis (PCA) for massive SNP datasets stored as genlight object. This implementation has the advantage of never representing to complete data matrix, therefore making huge economies in terms of rapid access memory (RAM). When the `parallel` package is available, `glPca` uses multiple-core ressources for more efficient computations. `glPca` returns lists with the class `glPca` (see 'value').

Other functions are defined for objects of this class:

- `print`: prints the content of a `glPca` object.

- `scatter`: produces scatterplots of principal components, with a screeplot of eigenvalues as inset.

- `loadingplot`: plots the loadings of the analysis for one given axis, using an adapted version of the generic function `loadingplot`.

```r
glPca(x, center = TRUE, scale = FALSE, nf = NULL, loadings = TRUE, 
    alleleAsUnit = FALSE, useC = TRUE, parallel = FALSE,
  n.cores = NULL, returnDotProd=FALSE, matDotProd=NULL)

## S3 method for class 'glPca'
print(x, ...)

## S3 method for class 'glPca'
scatter(x, xax = 1, yax = 2, posi = "bottomleft", bg = "white", 
    ratio = 0.3, label = rownames(x$scores), clabel = 1, xlim = NULL, 
    ylim = NULL, grid = TRUE, addaxes = TRUE, origin = c(0, 0), 
    include.origin = TRUE, sub = "", csub = 1, possub = "bottomleft", 
    cgrid = 1, pixmap = NULL, contour = NULL, area = NULL, ...)

## S3 method for class 'glPca'
loadingplot(x, at=NULL, threshold=NULL, axis=1,
    fac=NULL, byfac=FALSE, lab=rownames(x$loadings), cex.lab=0.7, cex.fac=1,
    lab.jitter=0, main="Loading plot", xlab="SNP positions",
    ylab="Contributions", srt = 90, adj = c(0, 0.5), ...)
```

## Arguments

- `x`: for `glPca`, a genlight object; for `print`, `scatter`, and `loadingplot`, a `glPca` object.
- `center`: a logical indicating whether the numbers of alleles should be centered; defaults to TRUE
- `scale`: a logical indicating whether the numbers of alleles should be scaled; defaults to FALSE
- `nf`: an integer indicating the number of principal components to be retained; if NULL, a screeplot of eigenvalues will be displayed and the user will be asked for a number of retained axes.
- `loadings`: a logical indicating whether loadings of the alleles should be computed (TRUE, default), or not (FALSE). Vectors of loadings are not always useful, and can take a large amount of RAM when millions of SNPs are considered.
- `alleleAsUnit`: a logical indicating whether alleles are considered as units (i.e., a diploid genotype equals two samples, a triploid, three, etc.) or whether individuals are considered as units of information.
- `useC`: a logical indicating whether compiled C code should be used for faster computations; this option cannot be used alongside parallel option.
- `parallel`: a logical indicating whether multiple cores -if available- should be used for the computations (TRUE), or not (FALSE, default); requires the package `parallel` to be installed (see details); this option cannot be used alongside useCoption.
- `n.cores`: if `parallel` is TRUE, the number of cores to be used in the computations; if NULL, then the maximum number of cores available on the computer is used.
- `returnDotProd`: a logical indicating whether the matrix of dot products between individuals should be returned (TRUE) or not (FALSE, default).
- `matDotProd`: an optional matrix of dot products between individuals, NULL by default. This option is used internally to speed up computation time when re-running the same PCA several times. Leave this argument as NULL unless you really know what you are doing.
- ``...``: further arguments to be passed to other functions.
- `xax,yax`: `integers` specifying which principal components should be shown in x and y axes.
- `posi,bg,ratio`: arguments used to customize the inset in scatterplots of `glPca` results. See `add.scatter` documentation in the ade4 package for more details.
- `label,clabel,xlim,ylim,grid,addaxes,origin,include.origin,sub,csub,possub,cgrid,pixmap,contour,area`: arguments passed to `s.class`; see `?s.label` for more information
- `at`: an optional numeric vector giving the abscissa at which loadings are plotted. Useful when variates are SNPs with a known position in an alignement.
- `threshold`: a threshold value above which values of x are identified. By default, this is the third quartile of x.
- `axis`: an integer indicating the column of x to be plotted; used only if x is a matrix-like object.
- `fac`: a factor defining groups of SNPs.
- `byfac`: a logical stating whether loadings should be averaged by groups of SNPs, as defined by `fac`.
- `lab`: a character vector giving the labels used to annotate values above the threshold.
- `cex.lab`: a numeric value indicating the size of annotations.
- `cex.fac`: a numeric value indicating the size of annotations for groups of observations.
- `lab.jitter`: a numeric value indicating the factor of randomisation for the position of annotations. Set to 0 (by default) implies no randomisation.
- `main`: the main title of the figure.
- `xlab`: the title of the x axis.
- `ylab`: the title of the y axis.
- `srt`: rotation of the labels; see ?text.
- `adj`: adjustment of the labels; see ?text.

## Details

=== Using multiple cores ===

Most recent machines have one or several processors with multiple cores. R processes usually use one single core. The package `parallel` allows for parallelizing some computations on multiple cores, which can decrease drastically computational time.

Lastly, note that using compiled C code (`useC=TRUE`)is an alternative for speeding up computations, but cannot be used together with the parallel option.

## Returns

=== glPca objects ===

The class `glPca` is a list with the following components:

 - **call**: the matched call.

 - **eig**: a numeric vector of eigenvalues.

 - **scores**: a matrix of principal components, containing the coordinates of each individual (in row) on each principal axis (in column).

 - **loadings**: (optional) a matrix of loadings, containing the loadings of each SNP (in row) for each principal axis (in column).

-

=== other outputs ===

Other functions have different outputs:

- `scatter` return the matched call.

- `loadingplot` returns information about the most contributing SNPs (see `loadingplot.default`)

## See Also

- `genlight`: class of object for storing massive binary SNP data.

- `glSim`: a simple simulator for genlight objects.

- `glPlot`: plotting genlight objects.

- `dapc`: Discriminant Analysis of Principal Components.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

## simulate a toy dataset
x <- glSim(50,4e3, 50, ploidy=2)
x
plot(x)

## perform PCA
pca1 <- glPca(x, nf=2)

## plot eigenvalues
barplot(pca1$eig, main="eigenvalues", col=heat.colors(length(pca1$eig)))

## basic plot
scatter(pca1, ratio=.2)

## plot showing groups
s.class(pca1$scores, pop(x), col=colors()[c(131,134)])
add.scatter.eig(pca1$eig,2,1,2)
## End(Not run)
```



