 data

# Data Set with 521 Microorganisms In Species Groups

## Format

A tibble with 521 observations and 4 variables:

 * `mo_group`
   
   ID of the species group / microbiological complex
 * `mo`
   
   ID of the microorganism belonging in the species group / microbiological complex
 * `mo_group_name`
   
   Name of the species group / microbiological complex, as retrieved with `mo_name()`
 * `mo_name`
   
   Name of the microorganism belonging in the species group / microbiological complex, as retrieved with `mo_name()`

```r
microorganisms.groups
```

## Description

A data set containing species groups and microbiological complexes, which are used in the clinical breakpoints table .

## Details

Like all data sets in this package, this data set is publicly available for download in the following formats: R, MS Excel, Apache Feather, Apache Parquet, SPSS, SAS, and Stata. Please visit [our website for the download links](https://msberends.github.io/AMR/articles/datasets.html). The actual files are of course available on [our GitHub repository](https://github.com/msberends/AMR/tree/main/data-raw).

## Examples

```r
microorganisms.groups

# these are all species in the Bacteroides fragilis group, as per WHONET:
microorganisms.groups[microorganisms.groups$mo_group == "B_BCTRD_FRGL-C", ]
```

## See Also

`as.mo()` microorganisms



