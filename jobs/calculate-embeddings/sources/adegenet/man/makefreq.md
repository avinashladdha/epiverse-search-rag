 methods

# Compute allelic frequencies

```r
makefreq(x, ...)

## S4 method for signature 'genind'
makefreq(x, quiet = FALSE, missing = NA, truenames = TRUE, ...)

## S4 method for signature 'genpop'
makefreq(x, quiet = FALSE, missing = NA, truenames = TRUE, ...)
```

## Arguments

- `x`: a genind or genpop object.
- `...`: further arguments (curently unused)
- `quiet`: logical stating whether a conversion message must be printed (TRUE,default) or not (FALSE).
- `missing`: treatment for missing values. Can be NA, 0 or "mean" (see details)
- `truenames`: deprecated; there for backward compatibility

## Returns

Returns a list with the following components: - **tab**: matrix of allelic frequencies (rows: populations; columns: alleles).

- **nobs**: number of observations (i.e. alleles) for each population x locus combinaison. - **call**: the matched call

## Description

The function `makefreq` is a generic to compute allele frequencies. These can be derived for genind or genpop objects. In the case of genind objects, data are kept at the individual level, but standardised so that allele frequencies sum up to 1.

## Details

There are 3 treatments for missing values:

- NA: kept as NA.

- 0: missing values are considered as zero. Recommended for a PCA on compositionnal data.

- "mean": missing values are given the mean frequency of the corresponding allele. Recommended for a centred PCA.

Note that this function is now a simple wrapper for the accessor `tab`.

## Examples

```r
## Not run:

data(microbov)
obj1 <- microbov
obj2 <- genind2genpop(obj1)

# perform a correspondance analysis on counts data
Xcount <- tab(obj2, NA.method="zero")
ca1 <- dudi.coa(Xcount,scannf=FALSE)
s.label(ca1$li,sub="Correspondance Analysis",csub=1.2)
add.scatter.eig(ca1$eig,nf=2,xax=1,yax=2,posi="topleft")

# perform a principal component analysis on frequency data
Xfreq <- makefreq(obj2, missing="mean")
Xfreq <- tab(obj2, NA.method="mean") # equivalent to line above
pca1 <- dudi.pca(Xfreq,scale=FALSE,scannf=FALSE)
s.label(pca1$li,sub="Principal Component Analysis",csub=1.2)
add.scatter.eig(pca1$eig,nf=2,xax=1,yax=2,posi="top")
## End(Not run)
```

## See Also

`genpop`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



