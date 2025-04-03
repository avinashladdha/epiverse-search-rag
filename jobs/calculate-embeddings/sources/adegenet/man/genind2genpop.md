# Conversion from a genind to a genpop object

```r
genind2genpop(
  x,
  pop = NULL,
  quiet = FALSE,
  process.other = FALSE,
  other.action = mean
)
```

## Arguments

- `x`: an object of class `genind`.
- `pop`: a factor giving the population of each genotype in 'x' OR a formula specifying which strata are to be used when converting to a genpop object. If none provided, population factors are sought in x@pop, but if given, the argument prevails on x@pop.
- `quiet`: logical stating whether a conversion message must be printed (TRUE,default) or not (FALSE).
- `process.other`: a logical indicating whether the `@other` slot should be processed (see details).
- `other.action`: a function to be used when processing the `@other` slot. By default, 'mean' is used.

## Returns

A genpop object. The component @other in 'x' is passed to the created genpop object.

## Description

The function `genind2genpop` converts genotypes data (genind) into alleles counts per population (genpop).

## Details

=== 'missing' argument ===

The values of the 'missing' argument in `genind2genpop` have the following effects:

- "NA": if all genotypes of a population for a given allele are missing, count value will be NA

- "0": if all genotypes of a population for a given allele are missing, count value will be 0

- "chi2": if all genotypes of a population for a given allele are missing, count value will be that of a theoretical count in of a Chi-squared test. This is obtained by the product of the margins sums divided by the total number of alleles.

=== processing the `@other` slot ===

Essentially, `genind2genpop` is about aggregating data per population. The function can do the same for all numeric items in the `@other` slot provided they have the same length (for vectors) or the same number of rows (matrix-like objects) as the number of genotypes. When the case is encountered and if `process.other` is TRUE, then these objects are processed using the function defined in `other.action` per population. For instance, spatial coordinates of genotypes would be averaged to obtain population coordinates.

## Examples

```r
## simple conversion
data(nancycats)
nancycats
catpop <- genind2genpop(nancycats)
catpop
summary(catpop)

## processing the @other slot
data(sim2pop)
sim2pop$other$foo <- letters
sim2pop
dim(sim2pop$other$xy) # matches the number of genotypes
sim2pop$other$foo # does not match the number of genotypes

obj <- genind2genpop(sim2pop, process.other=TRUE)
obj$other # the new xy is the populations' centre

pch <- as.numeric(pop(sim2pop))
col <- pop(sim2pop)
levels(col) <- c("blue","red")
col <- as.character(col)
plot(sim2pop$other$xy, pch=pch, col=col)
text(obj$other$xy, lab=row.names(obj$other$xy), col=c("blue","red"), cex=2, font=2)
## Not run:

data(microbov)
strata(microbov) <- data.frame(other(microbov))
summary(genind2genpop(microbov)) # Conversion based on population factor
summary(genind2genpop(microbov, ~coun)) # Conversion based on country
summary(genind2genpop(microbov, ~coun/spe)) # Conversion based on country and species
## End(Not run)
```

## See Also

genind , genpop

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



