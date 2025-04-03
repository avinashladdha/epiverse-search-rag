UTF-8

# Pairwise distance plots

## Description

The function `pairDistPlot` extracts and plots pairwise distances between different groups (graphs use ggplot2). The function `pairDistPlot` does the same, without the graphs.

 `pairDistPlot` is a generic function with methods for the following types of objects:

- `dist`

- `matrix` (only numeric data)

- `genind` objects (genetic markers, individuals)

- `DNAbin` objects (DNA sequences)

```r
pairDist(x, ...)

pairDistPlot(x, ...)

## S3 method for class 'dist'
pairDistPlot(x, grp, within=FALSE, sep="-", data=TRUE,
             violin=TRUE, boxplot=TRUE, jitter=TRUE, ...)

## S3 method for class 'matrix'
pairDistPlot(x, grp, within=FALSE, sep="-", data=TRUE,
             violin=TRUE, boxplot=TRUE, jitter=TRUE, ...)

## S3 method for class 'genind'
pairDistPlot(x, grp, within=FALSE, sep="-", data=TRUE,
             violin=TRUE, boxplot=TRUE, jitter=TRUE, ...)

## S3 method for class 'DNAbin'
pairDistPlot(x, grp, within=FALSE, sep="-", data=TRUE,
             violin=TRUE, boxplot=TRUE, jitter=TRUE, ...)
```

## Arguments

- `x`: pairwise distances provided as a `dist` or a symmetric `matrix`, or `genind` or `DNAbin` object. For `genind` objects, pairwise squared Euclidean distances are computed from the allele data. For `DNAbin` objects, distances are computed uing `dist.dna`, and '...' is used to pass arguments to the function.
- `grp`: a factor defining a grouping of individuals.
- `within`: a logical indicating whether to keep within-group comparisons.
- `sep`: a character used as separator between group names
- `data`: a logical indicating whether data of the plot should be returned.
- `violin`: a logical indicating whether a violinplot should be generated.
- `boxplot`: a logical indicating whether a boxplot should be generated.
- `jitter`: a logical indicating whether a jitter-plot should be generated.
- ``...``: further arguments to be used by other functions; used for `DNAbin` object to pass argumetns to `dist.dna`.

## Returns

A list with different components, depending on the values of the arguments. Plots are returned as `ggplot2` objects.

## See Also

`gengraph` to identify connectivity based on distances.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk .

## Examples

```r
## Not run:


## use a subset of influenza data
data(H3N2)
set.seed(1)
dat <- H3N2[sample(1:nInd(H3N2), 100)]

## get pairwise distances
temp <- pairDistPlot(dat, other(dat)$epid)

## see raw data
head(temp$data)

## see plots
temp$boxplot
temp$violin
temp$jitter
## End(Not run)
```



