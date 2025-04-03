UTF-8

# adegenet formal class (S4) for individual genotypes

## Description

The S4 class `genind` is used to store individual genotypes.

It contains several components described in the 'slots' section).

The `summary` of a `genind` object invisibly returns a list of component. The function `.valid.genind` is for internal use. The function `genind` creates a genind object from a valid table of alleles corresponding to the `@tab` slot. Note that as in other S4 classes, slots are accessed using @ instead of $.

## Slots

- **`tab`:**: (accessor: ‘tab’)
       
       matrix integers containing genotypes data for individuals (in rows) for all alleles (in columns). The table differs depending on the `@type` slot:
       
       - 'codom': values are numbers of alleles, summing up to the individuals' ploidies.
       
       - 'PA': values are presence/absence of alleles.
       
       In all cases, rows and columns are given generic names.
- **`loc.fac`:**: (accessor: ‘locFac’) locus factor for the columns of `tab`
- **`loc.n.all`:**: (accessor: ‘nAll’) integer vector giving the number of observed alleles per locus (see note)
- **`all.names`:**: (accessor: ‘alleles’) list having one component per locus, each containing a character vector of allele names
- **`ploidy`:**: (accessor: ‘ploidy’) an integer vector indicating the degree of ploidy of the genotypes. Beware: 2 is not an integer, but 2L or as.integer(2) is.
- **`type`:**: a character string indicating the type of marker: 'codom' stands for 'codominant' (e.g. microstallites, allozymes); 'PA' stands for 'presence/absence' (e.g. AFLP).
- **`call`:**: the matched call
- **`strata`:**: (accessor: ‘strata’) (optional) data frame giving levels of population stratification for each individual
- **`hierarchy`:**: (accessor: ‘hier’) (optional, currently unused) a hierarchical `formula` defining the hierarchical levels in the `@@strata` slot.
- **`pop`:**: (accessor: ‘pop’) (optional) factor giving the population of each individual
- **`other`:**: (accessor: ‘other’) (optional) a list containing other information

## Note:

The `loc.n.all` slot will reflect the number of columns per locus that contain at least one observation. This means that the sum of the this vector will not necessarily equal the number of columns in the data unless you use `drop = TRUE` when subsetting.

## Extends

Class `"gen"`, directly. Class `"indInfo"`, directly.

## Methods

- **names**: `signature(x = "genind")`: give the names of the components of a genind object
- **print**: `signature(x = "genind")`: prints a genind object
- **show**: `signature(object = "genind")`: shows a genind object (same as print)
- **summary**: `signature(object = "genind")`: summarizes a genind object, invisibly returning its content or suppress printing of auxiliary information by specifying `verbose = FALSE`

## See Also

`as.genind`, `genind2genpop`, `genpop`, `import2genind`, `read.genetix`, `read.genepop`, `read.fstat`

Related classes:

- genpop for storing data per populations

- genlight for an efficient storage of binary SNPs genotypes

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
showClass("genind")

obj <- read.genetix(system.file("files/nancycats.gtx",package="adegenet"))
obj
validObject(obj)
summary(obj)

## Not run:

# test inter-colonies structuration
if(require(hierfstat)){
gtest <- gstat.randtest(obj,nsim=99)
gtest
plot(gtest)
}

# perform a between-class PCA
pca1 <- dudi.pca(scaleGen(obj, NA.method="mean"),scannf=FALSE,scale=FALSE)
pcabet1 <- between(pca1,obj@pop,scannf=FALSE)
pcabet1

s.class(pcabet1$ls,obj@pop,sub="Inter-class PCA",possub="topleft",csub=2)
add.scatter.eig(pcabet1$eig,2,xax=1,yax=2)
## End(Not run)
```



