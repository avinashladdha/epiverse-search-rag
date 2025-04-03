# main function for argox

```r
argox_main(
  gt.folder,
  ili.folder,
  population.file,
  gft.file,
  mix,
  save.folder = NULL,
  NCORES = 8
)
```

## Arguments

- `gt.folder`: folder with Google Trends files, which should be thousands of csv file such as "US-MA_fever cough.csv" or "US-NY_cold or flu.csv"
- `ili.folder`: folder with ILINet data files: "ILINet_nat.csv" and "ILINet_regional.csv"
- `population.file`: file path to population csv file
- `gft.file`: file path to Google Flu Trends csv file
- `mix`: the weighted avarage mixing of raw state-level Google Trends data. Set to be 0 for stand-alone model. Set to be 1/3 for spatial-pooling model.
- `save.folder`: output folder to save graphics. If NULL then do not output graphics.
- `NCORES`: number of parallel cpu cores to be used.

## Description

Main function that reproduce the results in ARGOX paper. The datasets are available at Harvard Dataverse <doi:10.7910/DVN/2IVDGK>.

## References

Yang, S., Ning, S. & Kou, S.C. Use Internet search data to accurately track state level influenza epidemics. Sci Rep 11, 4023 (2021)



