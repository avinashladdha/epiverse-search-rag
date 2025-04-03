# Parsing of raw data for regional ILI estimation

```r
load_reg_data(
  gt.folder,
  ili.folder,
  population.file,
  gft.file,
  gt.parser = gt.parser.pub.web
)
```

## Arguments

- `gt.folder`: folder with all Google Trends data
- `ili.folder`: folder with all ILI data
- `population.file`: csv file path with state population data
- `gft.file`: csv file path for Google Flu Trends
- `gt.parser`: Google Trends data parser function, could be `gt.parser.pub.web` or `gt.parser.pub.api`

## Description

Parsing of raw data for regional ILI estimation

## Examples

```r
download.file("https://scholar.harvard.edu/files/syang/files/gt2016-10-24.zip",
file.path(tempdir(), "gt2016-10-24.zip"))
unzip(file.path(tempdir(), "gt2016-10-24.zip"), exdir = tempdir())
gt.folder <- file.path(tempdir(), "2016-10-19")

data_parsed <- load_reg_data(
  gt.folder=gt.folder,
  ili.folder=system.file("regiondata", "ili20161121", package = "argo"),
  population.file=system.file("regiondata", "Population.csv", package = "argo"),
  gft.file=system.file("regiondata", "GFT.txt", package = "argo")
)
```

## References

Shaoyang Ning, Shihao Yang, S. C. Kou. Accurate Regional Influenza Epidemics Tracking Using Internet Search Data. Scientific Reports



