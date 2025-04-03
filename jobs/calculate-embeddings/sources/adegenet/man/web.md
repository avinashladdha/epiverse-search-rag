# Functions to access online resources for adegenet

```r
adegenetWeb()

adegenetTutorial(
  which = c("basics", "spca", "dapc", "genomics", "strata", "snapclust")
)

adegenetIssues()
```

## Arguments

- `which`: a character string indicating which tutorial to open (see details)

## Description

These functions simply open websites or documents available online providing resources for adegenet.

## Details

 * adegenetWeb opens adegenet's website
 * adegenetTutorial opens adegenet tutorials
 * adegenetIssues opens the issue page on github; this is used to report a bug or post a feature request.

Available tutorials are:

 * 'basics': general introduction to adegenet; covers basic data structures, import/export, handling, and a number of population genetics methods
 * 'spca': spatial genetic structures using the spatial Principal Component Analysis
 * 'dapc': population structure using the Discriminant Analysis of Principal Components
 * 'genomics': handling large genome-wide SNP data using adegenet
 * 'strata': introduction to hierarchical population structure in adegenet
 * 'snapclust': introduction to fast maximum-likelihood genetic clustering using snapclust



