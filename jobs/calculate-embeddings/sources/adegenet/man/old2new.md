# Convert objects with obsolete classes into new objects

```r
old2new_genind(object, donor = new("genind"))

old2new_genlight(object, donor = new("genlight"))

old2new_genpop(object, donor = new("genpop"))
```

## Arguments

- `object`: a genind or genlight object from version 1.4 or earlier.
- `donor`: a new object to place all the data into.

## Description

The genind and genlight objects have changed in Adegenet version 2.0. They have each gained strata and hierarchy slots. What's more is that the genind objects have been optimized for storage and now store the tab slot as integers instead of numerics. This function will convert old genind or genlight objects to new ones seamlessly.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

Zhian N. Kamvar kamvarz@science.oregonstate.edu



