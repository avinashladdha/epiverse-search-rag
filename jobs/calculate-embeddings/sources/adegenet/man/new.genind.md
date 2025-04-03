 methods

# genind constructor

```r
## S4 method for signature 'genind'
initialize(
  .Object,
  tab,
  pop = NULL,
  prevcall = NULL,
  ploidy = 2L,
  type = c("codom", "PA"),
  strata = NULL,
  hierarchy = NULL,
  ...
)

genind(...)

as.genind(...)
```

## Arguments

- `.Object`: prototyped object (generated automatically when calling 'new')
- `tab`: A matrix of integers corresponding to the @tab slot of a genind object, with individuals in rows and alleles in columns, and containing either allele counts (if type="codom") or allele presence/absence (if type="PA")
- `pop`: an optional factor with one value per row in `tab` indicating the population of each individual
- `prevcall`: an optional call to be stored in the object
- `ploidy`: an integer vector indicating the ploidy of the individual; each individual can have a different value; if only one value is provided, it is recycled to generate a vector of the right length.
- `type`: a character string indicating the type of marker: codominant ("codom") or presence/absence ("PA")
- `strata`: a data frame containing population hierarchies or stratifications in columns. This must be the same length as the number of individuals in the data set.
- `hierarchy`: a hierarchical formula defining the columns of the strata slot that are hierarchical. Defaults to NULL.
- `...`: further arguments passed to other methods (currently not used)

## Returns

a genind object

## Description

The function `new` has a method for building genind objects. See the class description of genind for more information on this data structure. The functions `genind` and `as.genind` are aliases for `new("genind", ...)`.

## Details

Most users do not need using the constructor, but merely to convert raw allele data using `df2genind` and related functions.

## See Also

the description of the genind class; `df2genind`



