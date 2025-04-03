# Maximum-likelihood genetic clustering using EM algorithm

```r
snapclust(
  x,
  k,
  pop.ini = "ward",
  max.iter = 100,
  n.start = 10,
  n.start.kmeans = 50,
  hybrids = FALSE,
  dim.ini = 100,
  hybrid.coef = NULL,
  parent.lab = c("A", "B"),
  ...
)
```

## Arguments

- `x`: a genind object
- `k`: the number of clusters to look for
- `pop.ini`: parameter indicating how the initial group membership should be found. If `NULL`, groups are chosen at random, and the algorithm will be run `n.start times`. If "kmeans", then the function `find.clusters` is used to define initial groups using the K-means algorithm. If "ward", then the function `find.clusters` is used to define initial groups using the Ward algorithm. Alternatively, a factor defining the initial cluster configuration can be provided.
- `max.iter`: the maximum number of iteration of the EM algorithm
- `n.start`: the number of times the EM algorithm is run, each time with different random starting conditions
- `n.start.kmeans`: the number of times the K-means algorithm is run to define the starting point of the ML-EM algorithm, each time with different random starting conditions
- `hybrids`: a logical indicating if hybrids should be modelled explicitely; this is currently implemented for 2 groups only.
- `dim.ini`: the number of PCA axes to retain in the dimension reduction step for `find.clusters`, if this method is used to define initial group memberships (see argument `pop.ini`).
- `hybrid.coef`: a vector of hybridization coefficients, defining the proportion of hybrid gene pool coming from the first parental population; this is symmetrized around 0.5, so that e.g. c(0.25, 0.5) will be converted to c(0.25, 0.5, 0.75)
- `parent.lab`: a vector of 2 character strings used to label the two parental populations; only used if hybrids are detected (see argument `hybrids`)
- `...`: further arguments passed on to `find.clusters`

## Returns

The function `snapclust` returns a list with the following components:

 * `$group` a factor indicating the maximum-likelihood assignment of individuals to groups; if identified, hybrids are labelled after hybridization coefficients, e.g. 0.5_A - 0.5_B for F1, 0.75_A - 0.25_B for backcross F1 / A, etc.
 * `$ll`: the log-likelihood of the model
 * `$proba`: a matrix of group membership probabilities, with individuals in rows and groups in columns; each value correspond to the probability that a given individual genotype was generated under a given group, under Hardy-Weinberg hypotheses.
 * `$converged` a logical indicating if the algorithm converged; if FALSE, it is doubtful that the result is an actual Maximum Likelihood estimate.
 * `$n.iter` an integer indicating the number of iterations the EM algorithm was run for.

## Description

This function implements the fast maximum-likelihood genetic clustering approach described in Beugin et al (2018). The underlying model is very close to the model implemented by STRUCTURE, but allows for much faster estimation of genetic clusters thanks to the use of the Expectation-Maximization (EM) algorithm. Optionally, the model can explicitely account for hybridization and detect different types of hybrids (see `hybrids` and `hybrid.coef` arguments). The method is fully documented in a dedicated tutorial which can be accessed using `adegenetTutorial("snapclust")`.

## Details

The method is described in Beugin et al (2018) A fast likelihood solution to the genetic clustering problem. Methods in Ecology and Evolution tools:::Rd_expr_doi("10.1111/2041-210X.12968") . A dedicated tutorial is available by typing `adegenetTutorial("snapclust")`.

## Examples

```r
## Not run:

data(microbov)

## try function using k-means initialization
grp.ini <- find.clusters(microbov, n.clust=15, n.pca=150)

## run EM algo
res <- snapclust(microbov, 15, pop.ini = grp.ini$grp)
names(res)
res$converged
res$n.iter

## plot result
compoplot(res)

## flag potential hybrids
to.flag <- apply(res$proba,1,max)<.9
compoplot(res, subset=to.flag, show.lab=TRUE,
                 posi="bottomleft", bg="white")


## Simulate hybrids F1
zebu <- microbov[pop="Zebu"]
salers <- microbov[pop="Salers"]
hyb <- hybridize(zebu, salers, n=30)
x <- repool(zebu, salers, hyb)

## method without hybrids
res.no.hyb <- snapclust(x, k=2, hybrids=FALSE)
compoplot(res.no.hyb, col.pal=spectral, n.col=2)

## method with hybrids
res.hyb <- snapclust(x, k=2, hybrids=TRUE)
compoplot(res.hyb, col.pal =
          hybridpal(col.pal = spectral), n.col = 2)


## Simulate hybrids backcross (F1 / parental)
f1.zebu <- hybridize(hyb, zebu, 20, pop = "f1.zebu")
f1.salers <- hybridize(hyb, salers, 25, pop = "f1.salers")
y <- repool(x, f1.zebu, f1.salers)

## method without hybrids
res2.no.hyb <- snapclust(y, k = 2, hybrids = FALSE)
compoplot(res2.no.hyb, col.pal = hybridpal(), n.col = 2)

## method with hybrids F1 only
res2.hyb <- snapclust(y, k = 2, hybrids = TRUE)
compoplot(res2.hyb, col.pal = hybridpal(), n.col = 2)

## method with back-cross
res2.back <- snapclust(y, k = 2, hybrids = TRUE, hybrid.coef = c(.25,.5))
compoplot(res2.back, col.pal = hybridpal(), n.col = 2)
## End(Not run)
```

## See Also

The function `snapclust.choose.k` to investigate the optimal value number of clusters 'k'.

## Author(s)

Thibaut Jombart thibautjombart@gmail.com and Marie-Pauline Beugin



