 methods

# Compute scaled allele frequencies

```r
scaleGen(x, ...)

## S4 method for signature 'genind'
scaleGen(
  x,
  center = TRUE,
  scale = TRUE,
  NA.method = c("asis", "mean", "zero"),
  truenames = TRUE
)

## S4 method for signature 'genpop'
scaleGen(
  x,
  center = TRUE,
  scale = TRUE,
  NA.method = c("asis", "mean", "zero"),
  truenames = TRUE
)
```

## Arguments

- `x`: a genind and genpop object
- `...`: further arguments passed to other methods.
- `center`: a logical stating whether alleles frequencies should be centred to mean zero (default to TRUE). Alternatively, a vector of numeric values, one per allele, can be supplied: these values will be substracted from the allele frequencies.
- `scale`: a logical stating whether alleles frequencies should be scaled (default to TRUE). Alternatively, a vector of numeric values, one per allele, can be supplied: these values will be substracted from the allele frequencies.
- `NA.method`: a method to replace NA; asis: leave NAs as is; mean: replace by the mean allele frequencies; zero: replace by zero
- `truenames`: no longer used; kept for backward compatibility

## Returns

A matrix of scaled allele frequencies with genotypes (genind ) or populations in (genpop ) in rows and alleles in columns.

## Description

The generic function `scaleGen` is an analogue to the `scale` function, but is designed with further arguments giving scaling options.

## Details

Methods are defined for genind and genpop

objects. Both return data.frames of scaled allele frequencies.

## Examples

```r
## Not run:

## load data
data(microbov)
obj <- genind2genpop(microbov)

## apply scaling
X1 <- scaleGen(obj)

## compute PCAs with and without scaling
pcaObj <- dudi.pca(obj, scale = FALSE, scannf = FALSE) # pca with no scaling
pcaX1  <- dudi.pca(X1, scale = FALSE, scannf = FALSE, nf = 100) # pca scaled using scaleGen()
pcaX2  <- dudi.pca(obj, scale = TRUE, scannf = FALSE, nf = 100) # pca scaled in-PCA

## get the loadings of alleles for the two scalings
U1 <- pcaObj$c1
U2 <- pcaX1$c1
U3 <- pcaX2$c1

## find an optimal plane to compare loadings
## use a procustean rotation of loadings tables
pro1 <- procuste(U1, U2, nf = 2)
pro2 <- procuste(U2, U3, nf = 2)
pro3 <- procuste(U1, U3, nf = 2)

## graphics
par(mfrow=c(2, 3))
# eigenvalues
barplot(pcaObj$eig, main = "Eigenvalues\n no scaling")
barplot(pcaX1$eig, main = "Eigenvalues\n scaleGen scaling")
barplot(pcaX2$eig, main = "Eigenvalues\n in-PCA scaling")
# differences between loadings of alleles
s.match(pro1$scorX, pro1$scorY, clab = 0,
        sub = "no scaling -> scaling (procustean rotation)")
s.match(pro2$scorX, pro2$scorY, clab = 0,
        sub = "scaling scaleGen -> in-PCA scaling")
s.match(pro3$scorX, pro3$scorY, clab = 0,
        sub = "no scaling -> in-PCA scaling")
## End(Not run)
```

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



