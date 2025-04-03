 methods

# Access and manipulate the population hierarchy for genind or genlight objects.

```r
hier(x, formula = NULL, combine = TRUE, value)

hier(x) <- value
```

## Arguments

- `x`: a genind or genlight object
- `formula`: a nested formula indicating the order of the population hierarchy to be returned.
- `combine`: if `TRUE` (default), the levels will be combined according to the formula argument. If it is `FALSE`, the levels will not be combined.
- `value`: a formula specifying the full hierarchy of columns in the strata slot. (See Details below)

## Description

The following methods allow the user to quickly change the hierarchy or population of a genind or genlight object.

## Details

You must first specify your strata before you can specify your hierarchies. Hierarchies are special cases of strata in that the levels must be nested within each other. An error will occur if you specify a hierarchy that is not truly hierarchical.

 

### Details on Formulas

 The preferred use of these functions is with a `formula` object. Specifically, a hierarchical formula argument is used to name which strata are hierarchical. An example of a hierarchical formula would be:

||
|--:|
|`~Country/City/Neighborhood`|

This convention was chosen as it becomes easier to type and makes intuitive sense when defining a hierarchy. Note: it is important to use hierarchical formulas when specifying hierarchies as other types of formulas (eg. `~Country*City*Neighborhood`) will give incorrect results.

## Examples

```r
# let's look at the microbov data set:
data(microbov)
microbov

# We see that we have three vectors of different names in the 'other' slot. 
?microbov
# These are Country, Breed, and Species
names(other(microbov))

# Let's set the hierarchy
strata(microbov) <- data.frame(other(microbov))
microbov

# And change the names so we know what they are
nameStrata(microbov) <- ~Country/Breed/Species

# let's see what the hierarchy looks like by Species and Breed:
hier(microbov) <- ~Species/Breed
head(hier(microbov, ~Species/Breed))
```

## See Also

`strata` `genind` `as.genind`

## Author(s)

Zhian N. Kamvar



