UTF-8

methods

# Accessors for adegenet objects

## Description

An accessor is a function that allows to interact with slots of an object in a convenient way. Several accessors are available for genind or genpop objects. The operator "$" and "$<-" are used to access the slots, being equivalent to "@" and "@<-".

The operator "[" is a flexible way to subset data by individuals, populations, alleles, and loci. When using a matrix-like syntax, subsetting will apply to the dimensios of the @tab slot. In addition, specific arguments `loc` and `pop` can be used to indicate subsets of loci and populations. The argument `drop` is a logical indicating if alleles becoming non-polymorphic in a new dataset should be removed (default: FALSE). Examples:

 

 * "obj[i,j]" returns "obj" with a subset 'i' of individuals and 'j' of alleles.
 * "obj[1:10,]" returns an object with only the first 10 genotypes (if "obj" is a genind ) or the first 10 populations (if "obj" is a genpop )
 * "obj[1:10, 5:10]" returns an object keeping the first 10 entities and the alleles 5 to 10.
 * "obj[loc=c(1,3)]" returns an object keeping only the 1st and 3rd loci, using `locNames(obj)` as reference; logicals, or named loci also work; this overrides other subsetting of alleles.
 * "obj[pop=2:4]" returns an object keeping only individuals from the populations 2, 3 and 4, using `popNames(obj)` as reference; logicals, or named populations also work; this overrides other subsetting of individuals.
 * "obj[i=1:2, drop=TRUE]" returns an object keeping only the first two individuals (or populations), dropping the alleles no longer present in the data.

The argument `treatOther` handles the treatment of objects in the `@other` slot (see details). The argument `drop` can be set to TRUE to drop alleles that are no longer represented in the subset.

## Methods

- **nInd**: returns the number of individuals in the `genind` object
- **nLoc**: returns the number of loci
- **nAll**: returns the number of observed alleles in each locus
- **nPop**: returns the number of populations
- **pop**: returns a factor assigning individuals to populations.
- **pop<-**: replacement method for the `@pop` slot of an object.
- **popNames**: returns the names of populations.
- **popNames<-**: sets the names of populations using a vector of length `nPop(x)`.
- **indNames**: returns the names of individuals.
- **indNames<-**: sets the names of individuals using a vector of length `nInd(x)`.
- **locNames**: returns the names of markers and/or alleles.
- **locNames<-**: sets the names of markers using a vector of length `nLoc(x)`.
- **locFac**: returns a factor that defines which locus each column of the `@tab` slot belongs to
- **ploidy**: returns the ploidy of the data.
- **ploidy<-**: sets the ploidy of the data using an integer.
- **alleles**: returns the alleles of each locus.
- **alleles<-**: sets the alleles of each locus using a list with one character vector for each locus.
- **other**: returns the content of the `@other` slot (misc. information); returns `NULL` if the slot is onlyObserved or of length zero.
- **other<-**: sets the content of the `@other` slot (misc. information); the provided value needs to be a list; it not, provided value will be stored within a list.

```r
nInd(x, ...)
nLoc(x, ...)
nAll(x, onlyObserved = FALSE, ...)
nPop(x, ...)
pop(x)
indNames(x, ...)
## S4 method for signature 'genind'
indNames(x, ...)
locNames(x, ...)
## S4 method for signature 'genind'
locNames(x, withAlleles=FALSE, ...)
## S4 method for signature 'genpop'
locNames(x, withAlleles=FALSE, ...)
popNames(x, ...)
## S4 method for signature 'genind'
popNames(x, ...)
popNames(x, ...)
## S4 method for signature 'genpop'
popNames(x, ...)
ploidy(x, ...)
## S4 method for signature 'genind'
ploidy(x, ...)
## S4 method for signature 'genpop'
ploidy(x, ...)
## S4 method for signature 'genind'
other(x, ...)
## S4 method for signature 'genpop'
other(x, ...)
```

## Arguments

- `x`: a genind or a genpop object.
- `onlyObserved`: a logical indicating whether the allele count should also include the alleles with onlyObserved columns in the matrix. Defaults to `FALSE`, which will report only the observed alleles in the given population. `onlyObserved = TRUE` will be the equivalent of `table(locFac(x))`, but faster.
- `withAlleles`: a logical indicating whether the result should be of the form [locus name].[allele name], instead of [locus name].
- ``...``: further arguments to be passed to other methods (currently not used).

## Returns

A genind or genpop object.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Details

The "[" operator can treat elements in the `@other` slot as well. For instance, if `obj@other$xy` contains spatial coordinates, the `obj[1:3, ]@other$xy` will contain the spatial coordinates of the genotypes (or population) 1,2 and 3. This is handled through the argument `treatOther`, a logical defaulting to TRUE. If set to FALSE, the `@other` returned unmodified.

Note that only matrix-like, vector-like and lists can be proceeded in `@other`. Other kind of objects will issue a warning an be returned as they are, unless the argument `quiet` is left to TRUE, its default value.

The `drop` argument can be set to TRUE to retain only alleles that are present in the subset. To achieve better control of polymorphism of the data, see `isPoly`.

 `nAll()` reflects the number of columns per locus present in the current gen object. If `onlyObserved = TRUE`, then the number of columns with at least one non-missing allele is shown.

## Examples

```r
data(nancycats)
nancycats
pop(nancycats) # get the populations
indNames(nancycats) # get the labels of individuals
locNames(nancycats) # get the labels of the loci
alleles(nancycats)  # get the alleles
nAll(nancycats)     # count the number of alleles

head(tab(nancycats)) # get allele counts

# get allele frequencies, replace NAs
head(tab(nancycats, freq = TRUE, NA.method = "mean")) 

# let's isolate populations 4 and 8
popNames(nancycats)
obj <- nancycats[pop=c(4, 8)]
obj
popNames(obj)
pop(obj)
nAll(obj, onlyObserved = TRUE) # count number of alleles among these two populations
nAll(obj) # count number of columns in the data
all(nAll(obj, onlyObserved = TRUE) == lengths(alleles(obj))) # will be FALSE since drop = FALSE
all(nAll(obj) == lengths(alleles(obj))) # will be FALSE since drop = FALSE

# let's isolate two markers, fca23 and fca90
locNames(nancycats)
obj <- nancycats[loc=c("fca23","fca90")]
obj
locNames(obj)

# illustrate pop
obj <- nancycats[sample(1:100, 10)]
pop(obj)
pop(obj) <- rep(c('b', 'a'), each = 5)
pop(obj)

# illustrate locNames
locNames(obj)
locNames(obj, withAlleles = TRUE)
locNames(obj)[1] <- "newLocus"
locNames(obj)
locNames(obj, withAlleles=TRUE)

# illustrate how 'other' slot is handled
data(sim2pop)
nInd(sim2pop)
other(sim2pop[1:6]) # xy is subsetted automatically
other(sim2pop[1:6, treatOther=FALSE]) # xy is left as is
```



