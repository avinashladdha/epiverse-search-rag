UTF-8

# Web servers for adegenet

## Description

The function `adegenetServer` opens up a web page providing a simple user interface for some of the functionalities implemented in adegenet. These servers have been developed using the package `shiny`.

Currently available servers include:

 * `DAPC`: a server for the Discriminant Analysis of Principal Components (see ?dapc)

## See Also

dapc

```r
adegenetServer(what=c("DAPC"))
```

## Arguments

- `what`: a character string indicating which server to start; currently accepted values are: "DAPC"

## Returns

The function invisibly returns NULL.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

Caitlin Collins

## Examples

```r
## Not run:

## this opens a web page for DAPC
adegenetServer()
## End(Not run)
```



