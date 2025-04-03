UTF-8

methods

# Restore true labels of an object

## Description

The function `truenames` returns some elements of an object (genind or genpop ) using true names (as opposed to generic labels) for individuals, markers, alleles, and population.

Important: as of adegenet_2.0-0, these functions are deprecated as true labels are used whenever possible. Please use the function `tab` instead.

```r
## S4 method for signature 'genind'
truenames(x)
## S4 method for signature 'genpop'
truenames(x)
```

## Arguments

- `x`: a genind or a genpop object

## Returns

If x$pop is empty (NULL), a matrix similar to the x$tab slot but with true labels.

If x$pop exists, a list with this matrix ($tab) and a population vector with true names ($pop).

 

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## See Also

`tab`



