# Conversion to class "SNPbin"

## Description

The class SNPbin is a formal (S4) class for storing a genotype of binary SNPs in a compact way, using a bit-level coding scheme. New instances of this class are best created using `new`; see the manpage of SNPbin for more information on this point.

As a shortcut, conversion methods can be used to convert various objects into a SNPbin object. Conversions can be achieved using S3-style (`as.SNPbin(x)`) or S4-style (`as(x,"SNPbin"`) procedures. All of them call upon the constructor (`new`) of SNPbin objects.

Conversion is currently available from the following objects: - integer vectors - numeric vectors

## Author(s)

Thibaut Jombart (t.jombart@imperial.ac.uk )

## See Also

Related class:

- `SNPbin` - `genlight`, for storing multiple binary SNP genotypes.

## Examples

```r
## Not run:

## data to be converted
dat <- c(1,0,0,2,1,1,1,2,2,1,1,0,0,1)

## using the constructor
x1 <- new("SNPbin", dat)
x1

## using 'as' methods
x2 <- as.SNPbin(dat)
x3 <- as(dat, "SNPbin")

identical(x1,x2)
identical(x1,x3)
## End(Not run)
```



