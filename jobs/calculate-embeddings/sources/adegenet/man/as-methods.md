methods

# Converting genind/genpop objects to other classes

## Description

These S3 and S4 methods are used to coerce genind and genpop objects to matrix-like objects. In most cases, this is equivalent to calling the `@tab` slot. An exception to this is the convertion to `ktab` objects used in the ade4 package as inputs for K-tables methods (e.g. Multiple Coinertia Analysis).

## Usage

`as(object, Class)`

## Arguments

- **`object`**: a genind or a genpop object.
- **`Class`**: the name of the class to which the object should be coerced, for instance `"data.frame"` or `"matrix"`.

## Methods

- **coerce**: from one object class to another using `as(object,"Class")`, where the `object` is of the old class and the returned object is of the new class `"Class"`.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

data(microbov)
x <- tab(microbov,NA.method="mean")
as(x[1:3],"data.frame")

## dudi functions attempt to convert their first argument
## to a data.frame; so they can be used on genind/genpop objects.
## perform a PCA
pca1 <- dudi.pca(x, scale=FALSE, scannf=FALSE)
pca1

x <- genind2genpop(microbov,miss="chi2")
x <- as(x,"ktab")
class(x)
## perform a STATIS analysis
statis1 <- statis(x, scannf=FALSE)
statis1
plot(statis1)
## End(Not run)
```



