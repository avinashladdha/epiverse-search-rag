class

# Formal class "genlight"

## Description

The class `genlight` is a formal (S4) class for storing a genotypes of binary SNPs in a compact way, using a bit-level coding scheme. This storage is most efficient with haploid data, where the memory taken to represent data can be reduced more than 50 times. However, `genlight` can be used for any level of ploidy, and still remain an efficient storage mode.

A `genlight` object can be constructed from vectors of integers giving the number of the second allele for each locus and each individual (see 'Objects of the class genlight' below).

 `genlight` stores multiple genotypes. Each genotype is stored as a SNPbin object.

## Objects from the class genlight

`genlight` objects can be created by calls to `new("genlight", ...)`, where '...' can be the following arguments:

- **`gen`**: input genotypes, where each genotype is coded as a vector of numbers of the second allele. If a list, each slot of the list correspond to an individual; if a matrix or a data.frame, rows correspond to individuals and columns to SNPs. If individuals or loci are named in the input, these names will we stored in the produced object. All individuals are expected to have the same number of SNPs. Shorter genotypes are completed with NAs, issuing a warning.
- **`ploidy`**: an optional vector of integers indicating the ploidy of the genotypes. Genotypes can therefore have different ploidy. If not provided, ploidy will be guessed from the data (as the maximum number of second alleles in each individual).
- **`ind.names`**: an optional vector of characters giving the labels of the genotypes.
- **`loc.names`**: an optional vector of characters giving the labels of the SNPs.
- **`loc.all`**: an optional vector of characters indicating the alleles of each SNP; for each SNP, alleles must be coded by two letters separated by '/', e.g. 'a/t' is valid, but 'a t' or 'a |t' are not.
- **`chromosome`**: an optional factor indicating the chromosome to which each SNP belongs.
- **`position`**: an optional vector of integers indicating the position of the SNPs.
- **`other`**: an optional list storing miscellaneous information.

## Slots

The following slots are the content of instances of the class `genlight`; note that in most cases, it is better to retrieve information via accessors (see below), rather than by accessing the slots manually.

- **`gen`:**: a list of genotypes stored as SNPbin objects.
- **`n.loc`:**: an integer indicating the number of SNPs of the genotype.
- **`ind.names`:**: a vector of characters indicating the names of genotypes.
- **`loc.names`:**: a vector of characters indicating the names of SNPs.
- **`loc.all`:**: a vector of characters indicating the alleles of each SNP.
- **`chromosome`:**: an optional factor indicating the chromosome to which each SNP belongs.
- **`position`:**: an optional vector of integers indicating the position of the SNPs.
- **`ploidy`:**: a vector of integers indicating the ploidy of each individual.
- **`pop`:**: a factor indicating the population of each individual.
- **`strata`:**: a data frame containing different levels of population definition. (For methods, see `addStrata` and `setPop`)
- **`hierarchy`:**: a hierarchical `formula` defining the hierarchical levels in the `@@strata` slot.
- **`other`:**: a list containing other miscellaneous information.

## Methods

Here is a list of methods available for `genlight` objects. Most of these methods are accessors, that is, functions which are used to retrieve the content of the object. Specific manpages can exist for accessors with more than one argument. These are indicated by a '*' symbol next to the method's name. This list also contains methods for conversion from `genlight` to other classes.

- **[**: `signature(x = "genlight")`: usual method to subset objects in R. Is to be applied as if the object was a matrix where genotypes were rows and SNPs were columns. Indexing can be done via vectors of signed integers or of logicals. See details for extra supported arguments.
- **show**: `signature(x = "genlight")`: printing of the object.
- **$**: `signature(x = "genlight")`: similar to the @ operator; used to access the content of slots of the object.
- **$<-**: `signature(x = "genlight")`: similar to the @ operator; used to replace the content of slots of the object.
- **tab**: `signature(x = "genlight")`: returns a table of allele counts (see `tab`; additional arguments are `freq`, a logical stating if relative frequencies should be returned (use for varying ploidy), and `NA.method`, a character indicating if missing values should be replaced by the mean frequency("mean"), or left as is ("asis").
- **nInd**: `signature(x = "genlight")`: returns the number of individuals in the object.
- **nPop**: `signature(x = "genlight")`: returns the number of populations in the object.
- **nLoc**: `signature(x = "genlight")`: returns the number of SNPs in the object.
- **dim**: `signature(x = "genlight")`: returns the number of individuals and SNPs in the object, respectively.
- **names**: `signature(x = "genlight")`: returns the names of the slots of the object.
- **indNames**: `signature(x = "genlight")`: returns the names of the individuals, if provided when the object was constructed.
- **indNames<-**: `signature(x = "genlight")`: sets the names of the individuals using a character vector of length `nInd(x)`.
- **popNames**: `signature(x = "genlight")`: returns the names of the populations, if provided when the object was constructed.
- **popNames<-**: `signature(x = "genlight")`: sets the names of the populations using a character vector of length `nPop(x)`.
- **locNames**: `signature(x = "genlight")`: returns the names of the loci, if provided when the object was constructed.
- **locNames<-**: `signature(x = "genlight")`: sets the names of the SNPs using a character vector of length `nLoc(x)`.
- **ploidy**: `signature(x = "genlight")`: returns the ploidy of the genotypes.
- **ploidy<-**: `signature(x = "genlight")`: sets the ploidy of the individuals using a vector of integers of size `nInd(x)`; if a single value is provided, the same ploidy is assumed for all individuals.
- **NA.posi**: `signature(x = "genlight")`: returns the indices of missing values (NAs) as a list with one vector of integer for each individual.
- **alleles**: `signature(x = "genlight")`: returns the names of the alleles of each SNPs, if provided when the object was constructed.
- **alleles<-**: `signature(x = "genlight")`: sets the names of the alleles of each SNPs using a character vector of length `nLoc(x)`; for each SNP, two alleles must be provided, separated by a "/", e.g. 'a/t', 'c/a', etc.
- **chromosome**: `signature(x = "genlight")`: returns a factor indicating the chromosome of each SNPs, or NULL if the information is missing.
- **chromosome<-**: `signature(x = "genlight")`: sets the chromosome to which SNPs belong using a factor of length `nLoc(x)`.
- **chr**: `signature(x = "genlight")`: shortcut for `chromosome`.
- **chr<-**: `signature(x = "genlight")`: shortcut for `chromosome<-`.
- **position**: `signature(x = "genlight")`: returns an integer vector indicating the position of each SNPs, or NULL if the information is missing.
- **position<-**: `signature(x = "genlight")`: sets the positions of the SNPs using an integer vector of length `nLoc(x)`.
- **pop**: `signature(x = "genlight")`: returns a factor indicating the population of each individual, if provided when the object was constructed.
- **pop<-**: `signature(x = "genlight")`: sets the population of each individual using a factor of length `nInd(x)`.
- **other**: `signature(x = "genlight")`: returns the content of the slot `@other`.
- **other<-**: `signature(x = "genlight")`: sets the content of the slot `@other`.
- **as.matrix**: `signature(x = "genlight")`: converts a `genlight` object into a matrix of integers, with individuals in rows and SNPs in columns. The S4 method 'as' can be used as well (e.g. as(x, "matrix")).
- **as.data.frame**: `signature(x = "genlight")`: same as `as.matrix`.
- **as.list**: `signature(x = "genlight")`: converts a `genlight` object into a list of genotypes coded as vector of integers (numbers of second allele). The S4 method 'as' can be used as well (e.g. as(x, "list")).
- **cbind**: `signature(x = "genlight")`: merges several genlight objects by column, i.e. regroups data of identical individuals genotyped for different SNPs.
- **rbind**: `signature(x = "genlight")`: merges several genlight objects by row, i.e. regroups data of different individuals genotyped for the same SNPs.

## Details

=== On the subsetting using `[` ===

The function `[` accepts the following extra arguments:

- **treatOther**: a logical stating whether elements of the `@other` slot should be treated as well (TRUE), or not (FALSE). If treated, elements of the list are examined for a possible match of length (vectors, lists) or number of rows (matrices, data frames) with the number of individuals. Those who match are subsetted accordingly. Others are left as is, issuing a warning unless the argument `quiet` is set to TRUE.
- **quiet**: a logical indicating whether warnings should be issued when trying to subset components of the `@other` slot which do not match the number of individuals (TRUE), or not (FALSE, default).
- **`...`**: further arguments passed to the genlight constructor.

## Author(s)

Thibaut Jombart (t.jombart@imperial.ac.uk )

Zhian N. Kamvar (kamvarz@science.oregonstate.edu )

## See Also

Related class:

- `SNPbin`, for storing individual genotypes of binary SNPs

- `genind`, for storing other types of genetic markers.

## Examples

```r
## Not run:

## TOY EXAMPLE ##
## create and convert data
dat <- list(toto=c(1,1,0,0), titi=c(NA,1,1,0), tata=c(NA,0,3, NA))
x <- new("genlight", dat)
x

## examine the content of the object
names(x)
x@gen
x@gen[[1]]@snp # bit-level coding for first individual

## conversions
as.list(x)
as.matrix(x)

## round trips - must return TRUE
identical(x, new("genlight", as.list(x))) # list
identical(x, new("genlight", as.matrix(x))) # matrix
identical(x, new("genlight", as.data.frame(x))) # data.frame

## test subsetting
x[c(1,3)] # keep individuals 1 and 3
as.list(x[c(1,3)])
x[c(1,3), 1:2] # keep individuals 1 and 3, loci 1 and 2
as.list(x[c(1,3), 1:2])
x[c(TRUE,FALSE), c(TRUE,TRUE,FALSE,FALSE)] # same, using logicals
as.list(x[c(TRUE,FALSE), c(TRUE,TRUE,FALSE,FALSE)])


## REAL-SIZE EXAMPLE ##
## 50 genotypes of 1,000,000 SNPs
dat <- lapply(1:50, function(i) sample(c(0,1,NA), 1e6, prob=c(.5, .49, .01), replace=TRUE))
names(dat) <- paste("indiv", 1:length(dat))
print(object.size(dat), unit="aut") # size of the original data

x <- new("genlight", dat) # conversion
x
print(object.size(x), unit="au") # size of the genlight object
object.size(dat)/object.size(x) # conversion efficiency



#### cbind, rbind ####
a <- new("genlight", list(toto=rep(1,10), tata=rep(c(0,1), each=5), titi=c(NA, rep(1,9)) ))

ara <- rbind(a,a)
ara
as.matrix(ara)

aca <- cbind(a,a)
aca
as.matrix(aca)


#### subsetting @other ####
x <- new("genlight", list(a=1,b=0,c=1), other=list(1:3, letters,data.frame(2:4)))
x
other(x)
x[2:3]
other(x[2:3])
other(x[2:3, treatOther=FALSE])


#### seppop ####
pop(x) # no population info
pop(x) <- c("pop1","pop1", "pop2") # set population memberships
pop(x)
seppop(x)
## End(Not run)
```



