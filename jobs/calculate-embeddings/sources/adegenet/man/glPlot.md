UTF-8

# Plotting genlight objects

## Description

genlight object can be plotted using the function `glPlot`, which is also used as the dedicated `plot` method. These functions relie on `image` to represent SNPs data. More specifically, colors are used to represent the number of second allele for each locus and individual.

```r
glPlot(x, col=NULL, legend=TRUE, posi="bottomleft", bg=rgb(1,1,1,.5),...)

## S4 method for signature 'genlight'
plot(x, y=NULL, col=NULL, legend=TRUE, posi="bottomleft", bg=rgb(1,1,1,.5),...)
```

## Arguments

- `x`: a genlight object.
- `col`: an optional color vector; the first value corresponds to 0 alleles, the last value corresponds to the ploidy level of the data. Therefore, the vector should have a length of (`ploidy(x)+1`).
- `legend`: a logical indicating whether a legend should be added to the plot.
- `posi`: a character string indicating where the legend should be positioned. Can be any concatenation of "bottom"/"top" and "left"/"right".
- `bg`: a color used as a background for the legend; by default, transparent white is used; this may not be supported on some devices, and therefore background should be specified (e.g. `bg="white"`).
- ``...``: further arguments to be passed to `image`.
- `y`: ununsed argument, present for compatibility with the `plot` generic.

## See Also

- `genlight`: class of object for storing massive binary SNP data.

- `glSim`: a simple simulator for genlight

objects.

- `glPca`: PCA for genlight objects.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

## simulate data
x <- glSim(100, 1e3, n.snp.struc=100, ploid=2)

## default plot
glPlot(x)
plot(x) # identical plot

## disable legend
plot(x, leg=FALSE)

## use other colors
plot(x, col=heat.colors(3), bg="white")
## End(Not run)
```



