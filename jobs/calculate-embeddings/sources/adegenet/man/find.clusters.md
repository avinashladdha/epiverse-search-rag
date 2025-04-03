UTF-8

# find.cluster: cluster identification using successive K-means

## Description

 These functions implement the clustering procedure used in Discriminant Analysis of Principal Components (DAPC, Jombart et al. 2010). This procedure consists in running successive K-means with an increasing number of clusters (`k`), after transforming data using a principal component analysis (PCA). For each model, a statistical measure of goodness of fit (by default, BIC) is computed, which allows to choose the optimal `k`. See `details` for a description of how to select the optimal `k` and `vignette("adegenet-dapc")` for a tutorial.

Optionally, hierarchical clustering can be sought by providing a prior clustering of individuals (argument `clust`). In such case, clusters will be sought within each prior group.

The K-means procedure used in `find.clusters` is `kmeans` function from the `stats` package. The PCA function is `dudi.pca` from the `ade4` package, except for genlight objects which use the `glPca` procedure from adegenet. `find.clusters` is a generic function with methods for the following types of objects:

 

 * `data.frame` (only numeric data)
 * `matrix` (only numeric data)
 * `genind` objects (genetic markers)
 * `genlight` objects (genome-wide SNPs)

```r
## S3 method for class 'data.frame'
find.clusters(x, clust = NULL, n.pca = NULL, n.clust =
              NULL, method = c("kmeans", "ward"), stat = c("BIC","AIC", "WSS"),
              choose.n.clust = TRUE, criterion = c("diffNgroup", "min","goesup",
              "smoothNgoesup", "goodfit"), max.n.clust = round(nrow(x)/10),
              n.iter = 1e5, n.start = 10, center = TRUE, scale = FALSE,
              pca.select = c("nbEig","percVar"), perc.pca = NULL, ..., dudi =
              NULL)

## S3 method for class 'matrix'
find.clusters(x, ...)

## S3 method for class 'genind'
find.clusters(x, clust = NULL, n.pca = NULL, n.clust = NULL,
              method = c("kmeans", "ward"), stat = c("BIC","AIC", "WSS"),
              choose.n.clust = TRUE, criterion = c("diffNgroup", "min","goesup",
              "smoothNgoesup", "goodfit"), max.n.clust = round(nrow(x@tab)/10),
              n.iter = 1e5, n.start = 10, scale = FALSE, truenames = TRUE,
              ...)

## S3 method for class 'genlight'
find.clusters(x, clust = NULL, n.pca = NULL, n.clust = NULL,
              method = c("kmeans", "ward"), stat = c("BIC", "AIC", "WSS"),
              choose.n.clust = TRUE, criterion = c("diffNgroup",
              "min","goesup","smoothNgoesup", "goodfit"), max.n.clust =
              round(nInd(x)/10), n.iter = 1e5,n.start = 10, scale = FALSE,
              pca.select = c("nbEig","percVar"), perc.pca = NULL,glPca=NULL,
              ...)
```

## Arguments

- `x`: `a data.frame`, `matrix`, or `genind` object. For the `data.frame` and `matrix` arguments, only quantitative variables should be provided.
- `clust`: an optional `factor` indicating a prior group membership of individuals. If provided, sub-clusters will be sought within each prior group.
- `n.pca`: an `integer` indicating the number of axes retained in the Principal Component Analysis (PCA) step. If `NULL`, interactive selection is triggered.
- `n.clust`: an optinal `integer` indicating the number of clusters to be sought. If provided, the function will only run K-means once, for this number of clusters. If left as `NULL`, several K-means are run for a range of k (number of clusters) values.
- `method`: a `character` string indicating the type of clustering method to be used; "kmeans" (default) uses K-means clustering, and is the original implementation of `find.clusters`; "ward" is an alternative which uses Ward's hierarchical clustering; this latter method seems to be more reliable on some simulated datasets, but will be less computer-efficient for large numbers (thousands) of individuals.
- `stat`: a `character` string matching 'BIC', 'AIC', or 'WSS', which indicates the statistic to be computed for each model (i.e., for each value of `k`). BIC: Bayesian Information Criterion. AIC: Aikaike's Information Criterion. WSS: within-groups sum of squares, that is, residual variance.
- `choose.n.clust`: a `logical` indicating whether the number of clusters should be chosen by the user (TRUE, default), or automatically, based on a given criterion (argument `criterion`). It is HIGHLY RECOMMENDED to choose the number of clusters INTERACTIVELY, since i) the decrease of the summary statistics (BIC by default) is informative, and ii) no criteria for automatic selection is appropriate to all cases (see details).
- `criterion`: a `character` string matching "diffNgroup", "min","goesup", "smoothNgoesup", or "goodfit", indicating the criterion for automatic selection of the optimal number of clusters. See `details` for an explanation of these procedures.
- `max.n.clust`: an `integer` indicating the maximum number of clusters to be tried. Values of 'k' will be picked up between 1 and `max.n.clust`
- `n.iter`: an `integer` indicating the number of iterations to be used in each run of K-means algorithm. Corresponds to `iter.max` of `kmeans` function.
- `n.start`: an `integer` indicating the number of randomly chosen starting centroids to be used in each run of the K-means algorithm. Using more starting points ensures convergence of the algorithm. Corresponds to `nstart` of `kmeans` function.
- `center`: a `logical` indicating whether variables should be centred to mean 0 (TRUE, default) or not (FALSE). Always TRUE for genind
    
    objects.
- `scale`: a `logical` indicating whether variables should be scaled (TRUE) or not (FALSE, default). Scaling consists in dividing variables by their (estimated) standard deviation to account for trivial differences in variances. In allele frequencies, it comes with the risk of giving uninformative alleles more importance while downweighting informative alleles. Further scaling options are available for genind
    
    objects (see argument `scale.method`).
- `pca.select`: a `character` indicating the mode of selection of PCA axes, matching either "nbEig" or "percVar". For "nbEig", the user has to specify the number of axes retained (interactively, or via `n.pca`). For "percVar", the user has to specify the minimum amount of the total variance to be preserved by the retained axes, expressed as a percentage (interactively, or via `perc.pca`).
- `perc.pca`: a `numeric` value between 0 and 100 indicating the minimal percentage of the total variance of the data to be expressed by the retained axes of PCA.
- `truenames`: a `logical` indicating whether true (i.e., user-specified) labels should be used in object outputs (TRUE, default) or not (FALSE), in which case generic labels are used.
- ``: further arguments to be passed to other functions. For `find.clusters.matrix`, arguments are to match those of the `data.frame` method.
- `dudi`: optionally, a multivariate analysis with the class `dudi` (from the ade4 package). If provided, prior PCA will be ignored, and this object will be used as a prior step for variable orthogonalisation.
- `glPca`: an optional `glPca` object; if provided, dimension reduction is not performed (saving computational time) but taken directly from this object.

## Details

=== ON THE SELECTION OF K ===

(where K is the 'optimal' number of clusters)

So far, the analysis of data simulated under various population genetics models (see reference) suggested an ad hoc rule for the selection of the optimal number of clusters. First important result is that BIC seems more efficient than AIC and WSS to select the appropriate number of clusters (see example). The rule of thumb consists in increasing K until it no longer leads to an appreciable improvement of fit (i.e., to a decrease of BIC). In the most simple models (island models), BIC decreases until it reaches the optimal K, and then increases. In these cases, our rule amounts to choosing the lowest K. In other models such as stepping stones, the decrease of BIC often continues after the optimal K, but is much less steep.

An alternative approach is the automatic selection based on a fixed criterion. Note that, in any case, it is highly recommended to look at the graph of the BIC for different numbers of clusters as displayed during the interactive cluster selection. To use automated selection, set `choose.n.clust` to FALSE and specify the `criterion` you want to use, from the following values:

- "diffNgroup": differences between successive values of the summary statistics (by default, BIC) are splitted into two groups using a Ward's clustering method (see `?hclust`), to differentiate sharp decrease from mild decreases or increases. The retained K is the one before the first group switch. Appears to work well for island/hierarchical models, and decently for isolation by distance models, albeit with some unstability. Can be impacted by an initial, very sharp decrease of the test statistics. IF UNSURE ABOUT THE CRITERION TO USE, USE THIS ONE.

- "min": the model with the minimum summary statistics (as specified by `stat` argument, BIC by default) is retained. Is likely to work for simple island model, using BIC. It is likely to fail in models relating to stepping stones, where the BIC always decreases (albeit by a small amount) as K increases. In general, this approach tends to over-estimate the number of clusters.

- "goesup": the selected model is the K after which increasing the number of clusters leads to increasing the summary statistics. Suffers from inaccuracy, since i) a steep decrease might follow a small 'bump' of increase of the statistics, and ii) increase might never happen, or happen after negligible decreases. Is likely to work only for clear-cut island models.

- "smoothNgoesup": a variant of "goesup", in which the summary statistics is first smoothed using a lowess approach. Is meant to be more accurate than "goesup" as it is less prone to stopping to small 'bumps' in the decrease of the statistics.

- "goodfit": another criterion seeking a good fit with a minimum number of clusters. This approach does not rely on differences between successive statistics, but on absolute fit. It selects the model with the smallest K so that the overall fit is above a given threshold.

## Returns

The class `find.clusters` is a list with the following components:

 - **Kstat**: a `numeric` vector giving the values of the summary statistics for the different values of K. Is NULL if `n.clust` was specified.

 - **stat**: a `numeric` value giving the value of the summary statistics for the retained model

 - **grp**: a `factor` giving group membership for each individual.

 - **size**: an `integer` vector giving the size of the different clusters.

## References

Jombart T, Devillard S and Balloux F (2010) Discriminant analysis of principal components: a new method for the analysis of genetically structured populations. BMC Genetics 11:94. doi:10.1186/1471-2156-11-94

## See Also

- `dapc`: implements the DAPC.

- `scatter.dapc`: graphics for DAPC.

- `dapcIllus`: dataset illustrating the DAPC and `find.clusters`.

- `eHGDP`: dataset illustrating the DAPC and `find.clusters`.

- `kmeans`: implementation of K-means in the stat package.

- `dudi.pca`: implementation of PCA in the ade4 package.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

## THIS ONE TAKES A FEW MINUTES TO RUN ## 
data(eHGDP)

## here, n.clust is specified, so that only on K value is used
grp <- find.clusters(eHGDP, max.n=30, n.pca=200, scale=FALSE,
n.clust=4) # takes about 2 minutes
names(grp)
grp$Kstat
grp$stat


## to try different values of k (interactive)
grp <- find.clusters(eHGDP, max.n=50, n.pca=200, scale=FALSE)

## and then, to plot BIC values:
plot(grp$Kstat, type="b", col="blue")



## ANOTHER SIMPLE EXAMPLE ## 
data(sim2pop) # this actually contains 2 pop

## DETECTION WITH BIC (clear result)
foo.BIC <- find.clusters(sim2pop, n.pca=100, choose=FALSE)
plot(foo.BIC$Kstat, type="o", xlab="number of clusters (K)", ylab="BIC",
col="blue", main="Detection based on BIC")
points(2, foo.BIC$Kstat[2], pch="x", cex=3)
mtext(3, tex="'X' indicates the actual number of clusters")


## DETECTION WITH AIC (less clear-cut)
foo.AIC <- find.clusters(sim2pop, n.pca=100, choose=FALSE, stat="AIC")
plot(foo.AIC$Kstat, type="o", xlab="number of clusters (K)",
ylab="AIC", col="purple", main="Detection based on AIC")
points(2, foo.AIC$Kstat[2], pch="x", cex=3)
mtext(3, tex="'X' indicates the actual number of clusters")


## DETECTION WITH WSS (less clear-cut)
foo.WSS <- find.clusters(sim2pop, n.pca=100, choose=FALSE, stat="WSS")
plot(foo.WSS$Kstat, type="o", xlab="number of clusters (K)", ylab="WSS
(residual variance)", col="red", main="Detection based on WSS")
points(2, foo.WSS$Kstat[2], pch="x", cex=3)
mtext(3, tex="'X' indicates the actual number of clusters")


## TOY EXAMPLE FOR GENLIGHT OBJECTS ##
x <- glSim(100,500,500)
x
plot(x)
grp <- find.clusters(x, n.pca = 100, choose = FALSE, stat = "BIC")
plot(grp$Kstat, type = "o", xlab = "number of clusters (K)",
     ylab = "BIC",
     main = "find.clusters on a genlight object\n(two groups)")
## End(Not run)
```



