# Conversion to class "genlight"

## Description

The class `genlight` is a formal (S4) class for storing a genotypes of binary SNPs in a compact way, using a bit-level coding scheme. New instances of this class are best created using `new`; see the manpage of genlight for more information on this point.

As a shortcut, conversion methods can be used to convert various objects into a genlight object. Conversions can be achieved using S3-style (`as.genlight(x)`) or S4-style (`as(x,"genlight"`) procedures. All of them call upon the constructor (`new`) of genlight objects.

Conversion is currently available from the following objects: - matrix of type integer/numeric - data.frame with integer/numeric data - list of vectors of integer/numeric type

## Author(s)

Thibaut Jombart (t.jombart@imperial.ac.uk )

## See Also

Related class:

- `SNPbin`, for storing individual genotypes of binary SNPs

- `genind`

## Examples

```r
## Not run:

## data to be converted
dat <- list(toto=c(1,1,0,0,2,2,1,2,NA), titi=c(NA,1,1,0,1,1,1,0,0), tata=c(NA,0,3, NA,1,1,1,0,0))

## using the constructor
x1 <- new("genlight", dat)
x1

## using 'as' methods
x2 <- as.genlight(dat)
x3 <- as(dat, "genlight")

identical(x1,x2)
identical(x1,x3)
## End(Not run)
```



