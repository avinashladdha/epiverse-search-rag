 data

# Simulated data illustrating the DAPC

## Format

`dapcIllus` is list of 4 components being all genind objects.

## Source

Jombart, T., Devillard, S. and Balloux, F. Discriminant analysis of principal components: a new method for the analysis of genetically structured populations. Submitted to **BMC genetics**.

## Description

Datasets illustrating the Discriminant Analysis of Principal Components (DAPC, Jombart et al. submitted).

## Details

These data were simulated using various models using Easypop (2.0.1). The `dapcIllus` is a list containing the following genind

objects:

- "a": island model with 6 populations

- "b": hierarchical island model with 6 populations (3,2,1)

- "c": one-dimensional stepping stone with 2x6 populations, and a boundary between the two sets of 6 populations

- "d": one-dimensional stepping stone with 24 populations

See "source" for a reference providing simulation details.

## Examples

```r
## Not run:


data(dapcIllus)
attach(dapcIllus)
a # this is a genind object, like b, c, and d.


## FINS CLUSTERS EX NIHILO
clust.a <- find.clusters(a, n.pca=100, n.clust=6)
clust.b <- find.clusters(b, n.pca=100, n.clust=6)
clust.c <- find.clusters(c, n.pca=100, n.clust=12)
clust.d <- find.clusters(d, n.pca=100, n.clust=24)

## examin outputs
names(clust.a)
lapply(clust.a, head)


## PERFORM DAPCs
dapc.a <- dapc(a, pop=clust.a$grp, n.pca=100, n.da=5)
dapc.b <- dapc(b, pop=clust.b$grp, n.pca=100, n.da=5)
dapc.c <- dapc(c, pop=clust.c$grp, n.pca=100, n.da=11)
dapc.d <- dapc(d, pop=clust.d$grp, n.pca=100, n.da=23)


## LOOK AT ONE RESULT
dapc.a
summary(dapc.a)

## FORM A LIST OF RESULTS FOR THE 4 DATASETS
lres <- list(dapc.a, dapc.b, dapc.c, dapc.d)


## DRAW 4 SCATTERPLOTS
par(mfrow=c(2,2))
lapply(lres, scatter)


# detach data
detach(dapcIllus)
## End(Not run)
```

## References

Jombart, T., Devillard, S. and Balloux, F. Discriminant analysis of principal components: a new method for the analysis of genetically structured populations. Submitted to **Genetics**.

## See Also

- `dapc`: implements the DAPC.

- `eHGDP`: dataset illustrating the DAPC and `find.clusters`.

- `H3N2`: dataset illustrating the DAPC.

- `find.clusters`: to identify clusters without prior.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



