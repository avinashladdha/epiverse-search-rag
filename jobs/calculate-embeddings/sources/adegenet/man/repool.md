# Pool several genotypes into a single dataset

```r
repool(..., list = FALSE)
```

## Arguments

- `...`: a list of genind objects, or a series of genind objects separated by commas
- `list`: a logical indicating whether a list of objects with matched alleles shall be returned (TRUE), or a single genind object (FALSE, default).

## Description

The function `repool` allows to merge genotypes from different genind objects into a single 'pool' (i.e. a new genind ). The markers have to be the same for all objects to be merged, but there is no constraint on alleles.

## Details

This function can be useful, for instance, when hybrids are created using `hybridize`, to merge hybrids with their parent population for further analyses. Note that `repool` can also reverse the action of `seppop`.

## Examples

```r
## Not run:

## use the cattle breeds dataset
data(microbov)
temp <- seppop(microbov)
names(temp)
## hybridize salers and zebu -- nasty cattle
zebler <- hybridize(temp$Salers, temp$Zebu, n=40)
zebler
## now merge zebler with other cattle breeds
nastyCattle <- repool(microbov, zebler)
nastyCattle
## End(Not run)
```

## See Also

`seploc`, `seppop`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



