 data

# Data Set with 2 000 Example Isolates

## Format

A tibble with 2 000 observations and 46 variables:

 * `date`
   
   Date of receipt at the laboratory
 * `patient`
   
   ID of the patient
 * `age`
   
   Age of the patient
 * `gender`
   
   Gender of the patient, either "F" or "M"
 * `ward`
   
   Ward type where the patient was admitted, either "Clinical", "ICU", or "Outpatient"
 * `mo`
   
   ID of microorganism created with `as.mo()`, see also the microorganisms data set
 * `PEN:RIF`
   
   40 different antibiotics with class `sir` (see `as.sir()`); these column names occur in the antibiotics data set and can be translated with `set_ab_names()` or `ab_name()`

```r
example_isolates
```

## Description

A data set containing 2 000 microbial isolates with their full antibiograms. This data set contains randomised fictitious data, but reflects reality and can be used to practise AMR data analysis. For examples, please read [the tutorial on our website](https://msberends.github.io/AMR/articles/AMR.html).

## Details

Like all data sets in this package, this data set is publicly available for download in the following formats: R, MS Excel, Apache Feather, Apache Parquet, SPSS, SAS, and Stata. Please visit [our website for the download links](https://msberends.github.io/AMR/articles/datasets.html). The actual files are of course available on [our GitHub repository](https://github.com/msberends/AMR/tree/main/data-raw).

## Examples

```r
example_isolates
```



