 methods

# genpop constructor

```r
## S4 method for signature 'genpop'
initialize(
  .Object,
  tab,
  prevcall = NULL,
  ploidy = 2L,
  type = c("codom", "PA"),
  ...
)

genpop(...)

as.genpop(...)
```

## Arguments

- `.Object`: prototyped object (generated automatically when calling 'new')
- `tab`: A matrix of integers corresponding to the @tab slot of a genpop object, with individuals in rows and alleles in columns, and containing either allele counts
- `prevcall`: an optional call to be stored in the object
- `ploidy`: an integer vector indicating the ploidy of the individual; each individual can have a different value; if only one value is provided, it is recycled to generate a vector of the right length.
- `type`: a character string indicating the type of marker: codominant ("codom") or presence/absence ("PA")
- `...`: further arguments passed to other methods (currently not used)

## Returns

a genpop object

## Description

The function `new` has a method for building genpop objects. See the class description of genpop for more information on this data structure. The functions `genpop` and `as.genpop` are aliases for `new("genpop", ...)`.

## Details

Most users do not need using the constructor, but merely to convert raw allele data using `genind2genpop`.

## See Also

the description of the genpop class; `df2genind` and related functions for reading raw allele data



