# main function for argo2

```r
argo2_main(
  gt.folder,
  ili.folder,
  population.file,
  gft.file,
  save.folder = NULL
)
```

## Arguments

- `gt.folder`: folder with Google Trends files, which should be thousands of csv file such as "US-MA_fever cough.csv" or "US-NY_cold or flu.csv"
- `ili.folder`: folder with ILINet data files: "ILINet_nat.csv" and "ILINet_regional.csv"
- `population.file`: file path to population csv file
- `gft.file`: file path to Google Flu Trends csv file
- `save.folder`: output folder to save graphics. If NULL then do not output graphics.

## Description

main function that reproduce the results in ARGO2 paper

## Examples

```r
## Not run:

download.file("https://scholar.harvard.edu/files/syang/files/gt2016-10-24.zip",
file.path(tempdir(), "gt2016-10-24.zip"))
unzip(file.path(tempdir(), "gt2016-10-24.zip"), exdir = tempdir())
gt.folder <- file.path(tempdir(), "2016-10-19")
argo2_main(
  gt.folder=gt.folder,
  ili.folder=system.file("regiondata", "ili20161121", package = "argo"),
  population.file=system.file("regiondata", "Population.csv", package = "argo"),
  gft.file=system.file("regiondata", "GFT.txt", package = "argo")
)
## End(Not run)
```

## References

Shaoyang Ning, Shihao Yang, S. C. Kou. Accurate Regional Influenza Epidemics Tracking Using Internet Search Data. Scientific Reports



