methods

# Assess polymorphism in genind/genpop objects

## Description

The simple function `isPoly` can be used to check which loci are polymorphic, or alternatively to check which alleles give rise to polymorphism.

```r
## S4 method for signature 'genind'
isPoly(x, by=c("locus","allele"), thres=1/100)
## S4 method for signature 'genpop'
isPoly(x, by=c("locus","allele"), thres=1/100)
```

## Arguments

- `x`: a genind and genpop object
- `by`: a character being "locus" or "allele", indicating whether results should indicate polymorphic loci ("locus"), or alleles giving rise to polymorphism ("allele").
- `thres`: a numeric value giving the minimum frequency of an allele giving rise to polymorphism (defaults to 0.01).

 

## Returns

A vector of logicals.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

data(nancycats)
isPoly(nancycats,by="loc", thres=0.1)
isPoly(nancycats[1:3],by="loc", thres=0.1)
genind2df(nancycats[1:3])
## End(Not run)
```



