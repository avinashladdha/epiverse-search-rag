UTF-8

# Cross-validation for Discriminant Analysis of Principal Components (DAPC)

## Description

The function `xvalDapc` performs stratified cross-validation of DAPC using varying numbers of PCs (and keeping the number of discriminant functions fixed); `xvalDapc` is a generic with methods for `data.frame` and `matrix`.

```r
xvalDapc(x, ...)

## Default S3 method:
xvalDapc(x, grp, n.pca.max = 300, n.da = NULL,
              training.set = 0.9, result = c("groupMean", "overall"),
              center = TRUE, scale = FALSE,
              n.pca=NULL, n.rep = 30, xval.plot = TRUE, ...)

## S3 method for class 'data.frame'
xvalDapc(x, grp, n.pca.max = 300, n.da = NULL,
              training.set = 0.9, result = c("groupMean", "overall"),
              center = TRUE, scale = FALSE,
              n.pca=NULL, n.rep = 30, xval.plot = TRUE, ...)

## S3 method for class 'matrix'
xvalDapc(x, grp, n.pca.max = 300, n.da = NULL,
              training.set = 0.9, result = c("groupMean", "overall"),
              center = TRUE, scale = FALSE,
              n.pca=NULL, n.rep = 30, xval.plot = TRUE, ...)

## S3 method for class 'genlight'
xvalDapc(x, ...)

## S3 method for class 'genind'
xvalDapc(x, ...)
```

## Arguments

- `x`: `a data.frame` or a `matrix` used as input of DAPC.
- `grp`: a `factor` indicating the group membership of individuals.
- `n.pca.max`: maximum number of PCA components to retain.
- `n.da`: an `integer` indicating the number of axes retained in the Discriminant Analysis step. If `NULL`, n.da defaults to 1 less than the number of groups.
- `training.set`: the proportion of data (individuals) to be used for the training set; defaults to 0.9 if all groups have >= 10 members; otherwise, training.set scales automatically to the largest proportion that still ensures all groups will be present in both training and validation sets.
- `result`: a character string; "groupMean" for group-wise assignment sucess, or "overall" for an overall mean assignment success; see details.
- `center`: a `logical` indicating whether variables should be centred to mean 0 (TRUE, default) or not (FALSE). Always TRUE for genind objects.
- `scale`: a `logical` indicating whether variables should be scaled (TRUE) or not (FALSE, default). Scaling consists in dividing variables by their (estimated) standard deviation to account for trivial differences in variances.
- `n.pca`: an `integer` vector indicating the number of different number of PCA axes to be retained for the cross validation; if `NULL`, this will be dertermined automatically.
- `n.rep`: the number of replicates to be carried out at each level of PC retention; defaults to 30.
- `xval.plot`: a logical indicating whether a plot of the cross-validation results should be generated.
- ``...``: further arguments to be passed to `boot`. see Details.

## Details

The Discriminant Analysis of Principal Components (DAPC) relies on dimension reduction of the data using PCA followed by a linear discriminant analysis. How many PCA axes to retain is often a non-trivial question. Cross validation provides an objective way to decide how many axes to retain: different numbers are tried and the quality of the corresponding DAPC is assessed by cross- validation: DAPC is performed on a training set, typically made of 90% of the observations (comprising 90% of the observations in each subpopulation) , and then used to predict the groups of the 10% of remaining observations. The current method uses the average prediction success per group (result="groupMean"), or the overall prediction success (result="overall"). The number of PCs associated with the lowest Mean Squared Error is then retained in the DAPC.

### Parallel Computing

The permutation of the data for cross-validation is performed in part by the function`boot`. If you have a modern computer, it is likely that you have multiple cores on your system. R by default utilizes only one of these cores unless you tell it otherwise. For details, please see the documentation of `boot`. Basically, if you want to use multiple cores, you need two arguments:

1. `parallel` - what R parallel system to use (see below)
2. `ncpus` - number of cores you want to use

If you are on a unix system (Linux or OSX), you will want to specify `parallel = "multicore"`. If you are on Windows, you will want to specify `parallel = "snow"`.

 

## Returns

A `list` containing seven items, and a `plot` of the results. The first is a `data.frame` with two columns, the first giving the number of PCs of PCA retained in the corresponding DAPC, and the second giving the proportion of successful group assignment for each replicate. The second item gives the mean and confidence interval for random chance. The third gives the mean successful assignment at each level of PC retention. The fourth indicates which number of PCs is associated with the highest mean success. The fifth gives the Root Mean Squared Error at each level of PC retention. The sixth indicates which number of PCs is associated with the lowest MSE. The seventh item contains the DAPC carried out with the optimal number of PCs, determined with reference to MSE.

If `xval.plot=TRUE` a scatterplot of the results of cross-validation will be displayed.

## References

Jombart T, Devillard S and Balloux F (2010) Discriminant analysis of principal components: a new method for the analysis of genetically structured populations. BMC Genetics11:94. doi:10.1186/1471-2156-11-94

## See Also

`dapc`

## Author(s)

Caitlin Collins caitlin.collins12@imperial.ac.uk , Thibaut Jombart t.jombart@imperial.ac.uk , Zhian N. Kamvar kamvarz@science.oregonstate.edu

## Examples

```r
## Not run:

## CROSS-VALIDATION ##
data(sim2pop)
xval <- xvalDapc(sim2pop@tab, pop(sim2pop), n.pca.max=100, n.rep=3)
xval

## 100 replicates ##

# Serial version (SLOW!)
system.time(xval <- xvalDapc(sim2pop@tab, pop(sim2pop), n.pca.max=100, n.rep=100))

# Parallel version (faster!)
system.time(xval <- xvalDapc(sim2pop@tab, pop(sim2pop), n.pca.max=100, n.rep=100, 
                             parallel = "multicore", ncpus = 2))
## End(Not run)
```



