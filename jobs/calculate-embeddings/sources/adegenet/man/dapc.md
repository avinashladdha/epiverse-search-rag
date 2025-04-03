UTF-8

# Discriminant Analysis of Principal Components (DAPC)

## Description

These functions implement the Discriminant Analysis of Principal Components (DAPC, Jombart et al. 2010). This method descibes the diversity between pre-defined groups. When groups are unknown, use `find.clusters` to infer genetic clusters. See 'details' section for a succint description of the method, and `vignette("adegenet-dapc")` for a tutorial. Graphical methods for DAPC are documented in `scatter.dapc` (see `?scatter.dapc`).

 `dapc` is a generic function performing the DAPC on the following types of objects:

- `data.frame` (only numeric data)

- `matrix` (only numeric data)

- `genind` objects (genetic markers)

- `genlight` objects (genome-wide SNPs)

These methods all return an object with class `dapc`.

Functions that can be applied to these objects are (the ".dapc" can be ommitted):

- `print.dapc`: prints the content of a `dapc` object.

- `summary.dapc`: extracts useful information from a `dapc` object.

- `predict.dapc`: predicts group memberships based on DAPC results.

- `xvalDapc`: performs cross-validation of DAPC using varying numbers of PCs (and keeping the number of discriminant functions fixed); it currently has methods for `data.frame` and `matrix`.

DAPC implementation calls upon `dudi.pca` from the `ade4` package (except for genlight objects) and `lda` from the `MASS` package. The `predict` procedure uses `predict.lda` from the `MASS` package.

 `as.lda` is a generic with a method for `dapc` object which converts these objects into outputs similar to that of `lda.default`.

```r
## S3 method for class 'data.frame'
dapc(x, grp, n.pca=NULL, n.da=NULL, center=TRUE,
     scale=FALSE, var.contrib=TRUE, var.loadings=FALSE, pca.info=TRUE,
     pca.select=c("nbEig","percVar"), perc.pca=NULL, ..., dudi=NULL)

## S3 method for class 'matrix'
dapc(x, ...)

## S3 method for class 'genind'
dapc(x, pop=NULL, n.pca=NULL, n.da=NULL, scale=FALSE,
     truenames=TRUE, var.contrib=TRUE, var.loadings=FALSE, pca.info=TRUE,
     pca.select=c("nbEig","percVar"), perc.pca=NULL, ...)

## S3 method for class 'genlight'
dapc(x, pop=NULL, n.pca=NULL, n.da=NULL,
   scale=FALSE, var.contrib=TRUE, var.loadings=FALSE, pca.info=TRUE,
   pca.select=c("nbEig", "percVar"), perc.pca=NULL, glPca=NULL, ...)

## S3 method for class 'dudi'
dapc(x, grp, ...)

## S3 method for class 'dapc'
print(x, ...)

## S3 method for class 'dapc'
summary(object, ...)

## S3 method for class 'dapc'
predict(object, newdata, prior = object$prior, dimen,
         method = c("plug-in", "predictive", "debiased"), ...)
```

## Arguments

- `x`: `a data.frame`, `matrix`, or `genind` object. For the `data.frame` and `matrix` arguments, only quantitative variables should be provided.
- `grp,pop`: a `factor` indicating the group membership of individuals; for `scatter`, an optional grouping of individuals.
- `n.pca`: an `integer` indicating the number of axes retained in the Principal Component Analysis (PCA) step. If `NULL`, interactive selection is triggered.
- `n.da`: an `integer` indicating the number of axes retained in the Discriminant Analysis step. If `NULL`, interactive selection is triggered.
- `center`: a `logical` indicating whether variables should be centred to mean 0 (TRUE, default) or not (FALSE). Always TRUE for genind objects.
- `scale`: a `logical` indicating whether variables should be scaled (TRUE) or not (FALSE, default). Scaling consists in dividing variables by their (estimated) standard deviation to account for trivial differences in variances.
- `var.contrib`: a `logical` indicating whether the contribution of original variables (alleles, for genind objects) should be provided (TRUE, default) or not (FALSE). Such output can be useful, but can also create huge matrices when there is a lot of variables.
- `var.loadings`: a `logical` indicating whether the loadings of original variables (alleles, for genind objects) should be provided (TRUE) or not (FALSE, default). Such output can be useful, but can also create huge matrices when there is a lot of variables.
- `pca.info`: a `logical` indicating whether information about the prior PCA should be stored (TRUE, default) or not (FALSE). This information is required to predict group membership of new individuals using `predict`, but makes the object slightly bigger.
- `pca.select`: a `character` indicating the mode of selection of PCA axes, matching either "nbEig" or "percVar". For "nbEig", the user has to specify the number of axes retained (interactively, or via `n.pca`). For "percVar", the user has to specify the minimum amount of the total variance to be preserved by the retained axes, expressed as a percentage (interactively, or via `perc.pca`).
- `perc.pca`: a `numeric` value between 0 and 100 indicating the minimal percentage of the total variance of the data to be expressed by the retained axes of PCA.
- ``: further arguments to be passed to other functions. For `dapc.matrix`, arguments are to match those of `dapc.data.frame`; for `dapc.genlight`, arguments passed to `glPca`
- `glPca`: an optional `glPca` object; if provided, dimension reduction is not performed (saving computational time) but taken directly from this object.
- `object`: a `dapc` object.
- `truenames`: a `logical` indicating whether true (i.e., user-specified) labels should be used in object outputs (TRUE, default) or not (FALSE).
- `dudi`: optionally, a multivariate analysis with the class `dudi` (from the ade4 package). If provided, prior PCA will be ignored, and this object will be used as a prior step for variable orthogonalisation.
- `newdata`: an optional dataset of individuals whose membership is seeked; can be a data.frame, a matrix, a genind or a genlight object, but object class must match the original ('training') data. In particular, variables must be exactly the same as in the original data. For genind
    
    objects, see `repool` to ensure matching of alleles.
- `prior,dimen,method`: see `?predict.lda`.

## Details

The Discriminant Analysis of Principal Components (DAPC) is designed to investigate the genetic structure of biological populations. This multivariate method consists in a two-steps procedure. First, genetic data are transformed (centred, possibly scaled) and submitted to a Principal Component Analysis (PCA). Second, principal components of PCA are submitted to a Linear Discriminant Analysis (LDA). A trivial matrix operation allows to express discriminant functions as linear combination of alleles, therefore allowing one to compute allele contributions. More details about the computation of DAPC are to be found in the indicated reference.

DAPC does not infer genetic clusters ex nihilo; for this, see the `find.clusters` function.

## Returns

=== dapc objects ===

The class `dapc` is a list with the following components:

 - **call**: the matched call.

 - **n.pca**: number of PCA axes retained

 - **n.da**: number of DA axes retained

 - **var**: proportion of variance conserved by PCA principal components

 - **eig**: a numeric vector of eigenvalues.

 - **grp**: a factor giving prior group assignment

 - **prior**: a numeric vector giving prior group probabilities

 - **assign**: a factor giving posterior group assignment

 - **tab**: matrix of retained principal components of PCA

 - **loadings**: principal axes of DAPC, giving coefficients of the linear combination of retained PCA axes.

 - **ind.coord**: principal components of DAPC, giving the coordinates of individuals onto principal axes of DAPC; also called the discriminant functions.

 - **grp.coord**: coordinates of the groups onto the principal axes of DAPC.

 - **posterior**: a data.frame giving posterior membership probabilities for all individuals and all clusters.

 - **var.contr**: (optional) a data.frame giving the contributions of original variables (alleles in the case of genetic data) to the principal components of DAPC.

 - **var.load**: (optional) a data.frame giving the loadings of original variables (alleles in the case of genetic data) to the principal components of DAPC.

 - **match.prp**: a list, where each item is the proportion of individuals correctly matched to their original population in cross-validation.

=== other outputs ===

Other functions have different outputs:

- `summary.dapc` returns a list with 6 components: `n.dim` (number of retained DAPC axes), `n.pop` (number of groups/populations), `assign.prop` (proportion of overall correct assignment), `assign.per.pop` (proportion of correct assignment per group), `prior.grp.size` (prior group sizes), and `post.grp.size` (posterior group sizes), `xval.dapc`, `xval.genind` and `xval` (all return a list of four lists, each one with as many items as cross-validation runs. The first item is a list of `assign` components, the secon is a list of `posterior` components, the thirs is a list of `ind.score` components and the fourth is a list of `match.prp` items, i.e. the prortion of the validation set correctly matched to its original population)

## References

Jombart T, Devillard S and Balloux F (2010) Discriminant analysis of principal components: a new method for the analysis of genetically structured populations. BMC Genetics11:94. doi:10.1186/1471-2156-11-94

## See Also

 * `xvalDapc`: selection of the optimal numbers of PCA axes retained in DAPC using cross-validation.
 * `scatter.dapc`, `assignplot`, `compoplot`: graphics for DAPC.
 * `find.clusters`: to identify clusters without prior.
 * `dapcIllus`: a set of simulated data illustrating the DAPC
 * `eHGDP`, `H3N2`: empirical datasets illustrating DAPC

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## data(dapcIllus), data(eHGDP), and data(H3N2) illustrate the dapc
## see ?dapcIllus, ?eHGDP, ?H3N2
##
## Not run:

example(dapcIllus)
example(eHGDP)
example(H3N2)
## End(Not run)


## H3N2 EXAMPLE ##
data(H3N2)
pop(H3N2) <- factor(H3N2$other$epid)
dapc1 <- dapc(H3N2, var.contrib=FALSE, scale=FALSE, n.pca=150, n.da=5)

## remove internal segments and ellipses, different pch, add MStree
scatter(dapc1, cell=0, pch=18:23, cstar=0, mstree=TRUE, lwd=2, lty=2)

## label individuals at the periphery
# air = 2 is a measure of how much space each label needs
# pch = NA suppresses plotting of points
scatter(dapc1, label.inds = list(air = 2, pch = NA))

## only ellipse, custom labels
scatter(dapc1, cell=2, pch="", cstar=0, posi.da="top",
        label=paste("year\n",2001:2006), axesel=FALSE, col=terrain.colors(10))


## SHOW COMPOPLOT ON MICROBOV DATA ##
data(microbov)
dapc1 <- dapc(microbov, n.pca=20, n.da=15)
compoplot(dapc1, lab="")




## Not run:

## EXAMPLE USING GENLIGHT OBJECTS ##
## simulate data
x <- glSim(50,4e3-50, 50, ploidy=2)
x
plot(x)

## perform DAPC
dapc1 <- dapc(x, n.pca=10, n.da=1)
dapc1

## plot results
scatter(dapc1, scree.da=FALSE)

## SNP contributions
loadingplot(dapc1$var.contr)
loadingplot(tail(dapc1$var.contr, 100), main="Loading plot - last 100 SNPs")



## USE "PREDICT" TO PREDICT GROUPS OF NEW INDIVIDUALS ##
## load data
data(sim2pop)

## we make a dataset of:
## 30 individuals from pop A
## 30 individuals from pop B
## 30 hybrids

## separate populations and make F1
temp <- seppop(sim2pop)
temp <- lapply(temp, function(e) hybridize(e,e,n=30)) # force equal popsizes

## make hybrids
hyb <- hybridize(temp[[1]], temp[[2]], n=30)

## repool data - needed to ensure allele matching
newdat <- repool(temp[[1]], temp[[2]], hyb)
pop(newdat) <- rep(c("pop A", "popB", "hyb AB"), c(30,30,30))

## perform the DAPC on the first 2 pop (60 first indiv)
dapc1 <- dapc(newdat[1:60],n.pca=5,n.da=1)

## plot results
scatter(dapc1, scree.da=FALSE)

## make prediction for the 30 hybrids
hyb.pred <- predict(dapc1, newdat[61:90])
hyb.pred

## plot the inferred coordinates (circles are hybrids)
points(hyb.pred$ind.scores, rep(.1, 30))

## look at assignment using assignplot
assignplot(dapc1, new.pred=hyb.pred)
title("30 indiv popA, 30 indiv pop B, 30 hybrids")

## image using compoplot
compoplot(dapc1, new.pred=hyb.pred, ncol=2)
title("30 indiv popA, 30 indiv pop B, 30 hybrids")

## CROSS-VALIDATION ##
data(sim2pop)
xval <- xvalDapc(sim2pop@tab, pop(sim2pop), n.pca.max=100, n.rep=3)
xval
boxplot(xval$success~xval$n.pca, xlab="Number of PCA components",
ylab="Classification succes", main="DAPC - cross-validation")
## End(Not run)
```



