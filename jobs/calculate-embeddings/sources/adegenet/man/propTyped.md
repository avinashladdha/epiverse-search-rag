methods

# Compute the proportion of typed elements

## Description

The generic function `propTyped` is devoted to investigating the structure of missing data in adegenet objects.

Methods are defined for genind and genpop

objects. They can return the proportion of available (i.e. non-missing) data per individual/population, locus, or the combination of both in with case the matrix indicates which entity (individual or population) was typed on which locus.

```r
## S4 method for signature 'genind'
propTyped(x,  by=c("ind","loc","both"))
## S4 method for signature 'genpop'
propTyped(x,  by=c("pop","loc","both"))
```

## Arguments

- `x`: a genind and genpop object
- `by`: a character being "ind","loc", or "both" for genind object and "pop","loc", or "both" for genpop object. It specifies whether proportion of typed data are provided by entity ("ind"/"pop"), by locus ("loc") or both ("both"). See details.

 

## Returns

A vector of proportion (when `by` equals "ind", "pop", or "loc"), or a matrix of binary data (when `by` equals "both")

## Details

When `by` is set to "both", the result is a matrix of binary data with entities in rows (individuals or populations) and markers in columns. The values of the matrix are 1 for typed data, and 0 for NA.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

data(nancycats)
propTyped(nancycats,by="loc")
propTyped(genind2genpop(nancycats),by="both")
## End(Not run)
```



