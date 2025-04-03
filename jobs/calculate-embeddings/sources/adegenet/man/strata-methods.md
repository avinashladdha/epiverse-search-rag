 methods

# Access and manipulate the population strata for genind or genlight objects.

```r
strata(x, formula = NULL, combine = TRUE, value)

strata(x) <- value

nameStrata(x, value)

nameStrata(x) <- value

splitStrata(x, value, sep = "_")

splitStrata(x, sep = "_") <- value

addStrata(x, value, name = "NEW")

addStrata(x, name = "NEW") <- value
```

## Arguments

- `x`: a genind or genlight object
- `formula`: a nested formula indicating the order of the population strata.
- `combine`: if `TRUE` (default), the levels will be combined according to the formula argument. If it is `FALSE`, the levels will not be combined.
- `value`: a data frame OR vector OR formula (see details).
- `sep`: a `character` indicating the character used to separate hierarchical levels. This defaults to "_".
- `name`: an optional name argument for use with addStrata if supplying a vector. Defaults to "NEW".

## Description

The following methods allow the user to quickly change the strata of a genind or genlight object.

## Details

### Function Specifics

 * strata() - Use this function to view or define population stratification of a genind or genlight object.
 * nameStrata() - View or rename the different levels of strata.
 * splitStrata() - Split strata that are combined with a common separator. This function should only be used once during a workflow.
   
    * **Rationale:** It is often difficult to import files with several levels of strata as most data formats do not allow unlimited population levels. This is circumvented by collapsing all population strata into a single population factor with a common separator for each observation.
 * addStrata() - Add levels to your population strata. This is ideal for adding groups defined by `find.clusters`. You can input a data frame or a vector, but if you put in a vector, you have the option to name it.

 

### Argument Specifics

 These functions allow the user to seamlessly carry all possible population stratification with their genind or genlight

object. Note that there are two ways of performing all methods:

 * modifying: `strata(myData) \<- myStrata`
 * preserving: `myNewData \<- strata(myData, value = myStrata)`

They essentially do the same thing except that the modifying assignment method (the one with the "`<-`") will modify the object in place whereas the non-assignment method will preserve the original object (unless you overwrite it). Due to convention, everything right of the assignment is termed `value`. To avoid confusion, here is a guide to the argument ‘value’ for each function:

 * strata() `value =`a `data.frame` that defines the strata for each individual in the rows.
 * nameStrata() `value =`a `vector` or a `formula` that will define the names.
 * splitStrata() `value =`a `formula` argument with the same number of levels as the strata you wish to split.
 * addStrata() `value =`a `vector` or `data.frame` with the same length as the number of individuals in your data.

 

### Details on Formulas

 The preferred use of these functions is with a `formula` object. Specifically, a hierarchical formula argument is used to assign the levels of the strata. An example of a hierarchical formula would be:

||
|--:|
|`~Country/City/Neighborhood`|

This convention was chosen as it becomes easier to type and makes intuitive sense when defining a hierarchy. Note: it is important to use hiearchical formulas when specifying hierarchies as other types of formulas (eg. `~Country*City*Neighborhood`) will give incorrect results.

## Examples

```r
# let's look at the microbov data set:
data(microbov)
microbov

# We see that we have three vectors of different names in the 'other' slot. 
# ?microbov
# These are Country, Breed, and Species
names(other(microbov))

# Let's set the strata
strata(microbov) <- data.frame(other(microbov))
microbov

# And change the names so we know what they are
nameStrata(microbov) <- ~Country/Breed/Species

## Not run:

# let's see what the strata looks like by Species and Breed:
head(strata(microbov, ~Breed/Species))

# If we didn't want the last column combined with the first, we can set
# combine = FALSE
head(strata(microbov, ~Breed/Species, combine = FALSE))

#### USING splitStrata ####

# For the sake of example, we'll imagine that we have imported our data set
# with all of the stratifications combined. 
setPop(microbov) <- ~Country/Breed/Species
strata(microbov) <- NULL

# This is what our data would look like after import.
microbov

# To set our strata here, we need to use the functions strata and splitStrata
strata(microbov) <- data.frame(x = pop(microbov))
microbov # shows us that we have "one" level of stratification
head(strata(microbov)) # all strata are separated by "_"

splitStrata(microbov) <- ~Country/Breed/Species
microbov # Now we have all of our strata named and split
head(strata(microbov)) # all strata are appropriately named and split.
## End(Not run)
```

## See Also

`setPop` `genind` `as.genind`

## Author(s)

Zhian N. Kamvar



