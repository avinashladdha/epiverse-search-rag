# Export analysis for mvmapper visualisation

```r
export_to_mvmapper(x, ...)

## Default S3 method:
export_to_mvmapper(x, ...)

## S3 method for class 'dapc'
export_to_mvmapper(x, info, write_file = TRUE, out_file = NULL, ...)

## S3 method for class 'dudi'
export_to_mvmapper(x, info, write_file = TRUE, out_file = NULL, ...)

## S3 method for class 'spca'
export_to_mvmapper(x, info, write_file = TRUE, out_file = NULL, ...)
```

## Arguments

- `x`: The analysis to be exported. Can be a `dapc`, `spca`, or a `dudi` object.
- `...`: Further arguments to pass to other methods.
- `info`: A `data.frame` with additional information containing at least the following columns: `key` (unique individual identifier), `lat` (latitude), and `lon` (longitude). Other columns will be exported as well, but are optional.
- `write_file`: A `logical` indicating if the output should be written out to a .csv file. Defaults to `TRUE`.
- `out_file`: A character string indicating the file to which the output should be written. If NULL, the file used will be named `'mvmapper_data_[date and time].csv'`

## Returns

A `data.frame` which can serve as input to `mvmapper`, containing at least the following columns:

 * `key`: unique individual identifiers
 * `PC1`: first principal component; further principal components are optional, but if provided will be numbered and follow `PC1`.
 * `lat`: latitude for each individual
 * `lon`: longitude for each individual

In addition, specific information is added for some analyses:

 * `spca`: `Lag_PC` columns contain the lag-vectors of the principal components; the lag operator computes, for each individual, the average score of neighbouring individuals; it is useful for clarifying patches and clines.
 * `dapc`: `grp` is the group used in the analysis; `assigned_grp` is the group assignment based on the discriminant functions; `support` is the statistical support (i.e. assignment probability) for `assigned_grp`.

## Description

`mvmapper` is an interactive tool for visualising outputs of a multivariate analysis on a map from a web browser. The function `export_to_mvmapper` is a generic with methods for several standard classes of analyses in `adegenet` and `ade4`. Information on individual locations, as well as any other relevant data, is passed through the second argument `info`. By default, the function returns a formatted `data.frame` and writes the output to a .csv file.

## Details

`mvmapper` can be found at: [https://popphylotools.github.io/mvMapper/](https://popphylotools.github.io/mvMapper/)

## Examples

```r
# An example using the microsatellite dataset of Dupuis et al. 2016 (781
# individuals, 10 loci, doi: 10.1111/jeb.12931)

# Reading input file from adegenet

input_data <- system.file("data/swallowtails.rda", package="adegenet")
data(swallowtails)


# conducting a DAPC (n.pca determined using xvalDapc, see ??xvalDapc)

dapc1 <- dapc(swallowtails, n.pca=40, n.da=200)


# read in swallowtails_loc.csv, which contains "key", "lat", and "lon"
# columns with column headers (this example contains additional columns
# containing species identifications, locality descriptions, and COI
# haplotype clades)

input_locs <- system.file("files/swallowtails_loc.csv", package = "adegenet")
loc <- read.csv(input_locs, header = TRUE)


# generate mvmapper input file, automatically write the output to a csv, and
# name the output csv "mvMapper_Data.csv"
out_dir <- tempdir()
out_file <- file.path(out_dir, "mvMapper_Data.csv")

out <- export_to_mvmapper(dapc1, loc, write_file = TRUE, out_file = out_file)
```

## See Also

`mvmapper` is available at: [https://popphylotools.github.io/mvMapper/](https://popphylotools.github.io/mvMapper/)

## Author(s)

Thibaut Jombart thibautjombart@gmail.com



