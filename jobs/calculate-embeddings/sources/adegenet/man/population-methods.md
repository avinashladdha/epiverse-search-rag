 methods

# Manipulate the population factor of genind objects.

```r
setPop(x, formula = NULL)

setPop(x) <- value
```

## Arguments

- `x`: a genind or genlight object
- `formula`: a nested formula indicating the order of the population strata.
- `value`: same as formula

## Description

The following methods allow the user to quickly change the population of a genind object.

## Examples

```r
data(microbov)

strata(microbov) <- data.frame(other(microbov))

# Currently set on just 
head(pop(microbov)) 

# setting the strata to both Pop and Subpop
setPop(microbov) <- ~coun/breed 
head(pop(microbov))

## Not run:


# Can be used to create objects as well.
microbov.old <- setPop(microbov, ~spe) 
head(pop(microbov.old))
## End(Not run)
```

## Author(s)

Zhian N. Kamvar



