# Simulation of genealogies of haplotypes

## Description

The function `haploGen` implements simulations of genealogies of haplotypes. This forward-time, individual-based simulation tool allows haplotypes to replicate and mutate according to specified parameters, and keeps track of their genealogy.

Simulations can be spatially explicit or not (see `geo.sim` argument). In the first case, haplotypes are assigned to locations on a regular grip. New haplotypes disperse from their ancestor's location according to a random Poisson diffusion, or alternatively according to a pre-specified migration scheme. This tool does not allow for simulating selection or linkage disequilibrium.

Produced objects are lists with the class `haploGen`; see 'value' section for more information on this class. Other functions are available to print, plot, subset, sample or convert `haploGen` objects. A seqTrack method is also provided for analysing `haploGen` objects.

Note that for simulation of outbreaks, the new tool `simOutbreak` in the `outbreaker` package should be used.

```r
haploGen(seq.length=1e4, mu.transi=1e-4, mu.transv=mu.transi/2, t.max=20,
         gen.time=function(){1+rpois(1,0.5)},
         repro=function(){rpois(1,1.5)}, max.nb.haplo=200,
         geo.sim=FALSE, grid.size=10, lambda.xy=0.5,
         mat.connect=NULL,
         ini.n=1, ini.xy=NULL)
## S3 method for class 'haploGen'
print(x, ...)
## S3 method for class 'haploGen'
as.igraph(x, col.pal=redpal, ...)
## S3 method for class 'haploGen'
plot(x, y=NULL, col.pal=redpal, ...)
## S3 method for class 'haploGen'
x[i, j, drop=FALSE]
## S3 method for class 'haploGen'
labels(object, ...)
## S3 method for class 'haploGen'
as.POSIXct(x, tz="", origin=as.POSIXct("2000/01/01"), ...)
## S3 method for class 'haploGen'
seqTrack(x, best=c("min","max"), prox.mat=NULL, ...)
as.seqTrack.haploGen(x)
plotHaploGen(x, annot=FALSE, date.range=NULL, col=NULL, bg="grey", add=FALSE, ...)
sample.haploGen(x, n)
```

## Arguments

- `seq.length`: an integer indicating the length of the simulated haplotypes, in number of nucleotides.
- `mu.transi`: the rate of transitions, in number of mutation per site and per time unit.
- `mu.transv`: the rate of transversions, in number of mutation per site and per time unit.
- `t.max`: an integer indicating the maximum number of time units to run the simulation for.
- `gen.time`: an integer indicating the generation time, in number of time units. Can be a (fixed) number or a function returning a number (then called for each reproduction event).
- `repro`: an integer indicating the number of descendents per haplotype. Can be a (fixed) number or a function returning a number (then called for each reproduction event).
- `max.nb.haplo`: an integer indicating the maximum number of haplotypes handled at any time of the simulation, used to control the size of the produced object. Larger number will lead to slower simulations. If this number is exceeded, the genealogy is prunded to as to keep this number of haplotypes.
- `geo.sim`: a logical stating whether simulations should be spatially explicit (TRUE) or not (FALSE, default). Spatially-explicit simulations are slightly slower than their non-spatial counterpart.
- `grid.size`: the size of the square grid of possible locations for spatial simulations. The total number of locations will be this number squared.
- `lambda.xy`: the parameter of the Poisson distribution used to determine dispersion in x and y axes.
- `mat.connect`: a matrix of connectivity describing migration amongts all pairs of locations. `mat.connect[i,j]` indicates the probability, being in 'i', to migrate to 'j'. The rows of this matrix thus sum to 1. It has as many rows and columns as there are locations, with row 'i' / column 'j' corresponding to locations number 'i' and 'j'. Locations are numbered as in a matrix in which rows and columns are respectively x and y coordinates. For instance, in a 5x5 grid, locations are numbered as in `matrix(1:25,5,5)`.
- `ini.n`: an integer specifying the number of (identical) haplotypes to initiate the simulation
- `ini.xy`: a vector of two integers giving the x/y coordinates of the initial haplotype.
- `x,object`: `haploGen` objects.
- `y`: unused argument, for compatibility with 'plot'.
- `col.pal`: a color palette to be used to represent weights using colors on the edges of the graph. See `?num2col`. Note that the palette is inversed by default.
- `i,j, drop`: `i` is a vector used for subsetting the object. For instance, `i=1:3` will retain only the first three haplotypes of the genealogy. `j` and `drop` are only provided for compatibility, but not used.
- `best, prox.mat`: arguments to be passed to the `seqTrack` function. See documentation of `seqTrack` for more information.
- `annot,date.range,col,bg,add`: arguments to be passed to `plotSeqTrack`.
- `n`: an integer indicating the number of haplotypes to be retained in the sample





- `tz, origin`: aguments to be passed to `as.POSIXct` (see ?as.POSIXct)
- ``...``: further arguments to be passed to other methods; for 'plot', arguments are passed to `plot.igraph`.







## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## References

Jombart T, Eggo R, Dodd P, Balloux F (2010) Reconstructing disease outbreaks from genetic data: a graph approach. Heredity. doi: 10.1038/hdy.2010.78.

## Returns

=== haploGen class ===

 `haploGen` objects are lists containing the following slots:

- seq: DNA sequences in the DNAbin matrix format

- dates: dates of appearance of the haplotypes

- ances: a vector of integers giving the index of each haplotype's ancestor

- id: a vector of integers giving the index of each haplotype

- xy: (optional) a matrix of spatial coordinates of haplotypes

- call: the matched call

=== misc functions ===

- as.POSIXct: returns a vector of dates with POSIXct format

- labels: returns the labels of the haplotypes

- as.seqTrack: returns a seqTrack object. Note that this object is not a proper seqTrack analysis, but just a format conversion convenient for plotting `haploGen` objects.

## Details

=== Dependencies with other packages ===

- ape package is required as it implements efficient handling of DNA sequences used in `haploGen` objects. To install this package, simply type:

 `install.packages("ape")`

- for various purposes including plotting, converting genealogies to graphs can be useful. From adegenet version 1.3-5 onwards, this is achieved using the package `igraph`. See below.

=== Converting haploGen objects to graphs ===

 `haploGen` objects can be converted to `igraph` objects (package `igraph`), which can in turn be plotted and manipulated using classical graph tools. Simply use 'as.igraph(x)' where 'x' is a `haploGen` object. This functionality requires the `igraph` package. Graphs are time oriented (top=old, bottom=recent).

## See Also

`simOutbreak` in the package 'outbreaker' for simulating disease outbreaks under a realistic epidemiological model.

## Examples

```r
## Not run:

if(require(ape) && require(igraph)){
## PERFORM SIMULATIONS
x <- haploGen(geo.sim=TRUE)
x

## PLOT DATA
plot(x)

## PLOT SPATIAL SPREAD
plotHaploGen(x, bg="white")
title("Spatial dispersion")


## USE SEQTRACK RECONSTRUCTION
x.recons <- seqTrack(x)
mean(x.recons$ances==x$ances, na.rm=TRUE) # proportion of correct reconstructions

g <- as.igraph(x)
g
plot(g)
plot(g, vertex.size=0)


}
## End(Not run)
```



