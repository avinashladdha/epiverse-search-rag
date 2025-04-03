# Genotype composition plot

```r
compoplot(x, ...)

## S3 method for class 'matrix'
compoplot(
  x,
  col.pal = funky,
  border = NA,
  subset = NULL,
  show.lab = FALSE,
  lab = rownames(x),
  legend = TRUE,
  txt.leg = colnames(x),
  n.col = 4,
  posi = NULL,
  cleg = 0.8,
  bg = transp("white"),
  ...
)

## S3 method for class 'dapc'
compoplot(x, only.grp = NULL, border = NA, ...)

## S3 method for class 'snapclust'
compoplot(x, border = NA, ...)
```

## Arguments

- `x`: an object to be used for plotting (see description)
- `...`: further arguments to be passed to `barplot`
- `col.pal`: a color palette to be used for the groups; defaults to `funky`
- `border`: a color for the border of the barplot; use `NA` to indicate no border.
- `subset`: a subset of individuals to retain
- `show.lab`: a logical indicating if individual labels should be displayed
- `lab`: a vector of individual labels; if NULL, row.names of the matrix are used
- `legend`: a logical indicating whether a legend should be provided for the colors
- `txt.leg`: a character vector to be used for the legend
- `n.col`: the number of columns to be used for the legend
- `posi`: the position of the legend
- `cleg`: a size factor for the legend
- `bg`: the background to be used for the legend
- `only.grp`: a subset of groups to retain

## Description

The compoplot uses a barplot to represent the group assignment probability of individuals to several groups. It is a generic with methods for the following objects:

## Details

 * `matrix`: a matrix with individuals in row and genetic clusters in column, each entry being an assignment probability of the corresponding individual to the corresponding group
 * `dapc`: the output of the `dapc` function; in this case, group assignments are based upon geometric criteria in the discriminant space
 * `snapclust`: the output of the `snapclust` function; in this case, group assignments are based upon the likelihood of genotypes belonging to their groups

## Author(s)

Thibaut Jombart thibautjombart@gmail.com



