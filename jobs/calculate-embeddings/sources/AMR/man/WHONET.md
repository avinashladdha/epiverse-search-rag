 data

# Data Set with 500 Isolates - WHONET Example

## Format

A tibble with 500 observations and 53 variables:

 * `Identification number`
   
   ID of the sample
 * `Specimen number`
   
   ID of the specimen
 * `Organism`
   
   Name of the microorganism. Before analysis, you should transform this to a valid microbial class, using `as.mo()`.
 * `Country`
   
   Country of origin
 * `Laboratory`
   
   Name of laboratory
 * `Last name`
   
   Fictitious last name of patient
 * `First name`
   
   Fictitious initial of patient
 * `Sex`
   
   Fictitious gender of patient
 * `Age`
   
   Fictitious age of patient
 * `Age category`
   
   Age group, can also be looked up using `age_groups()`
 * `Date of admission`
   
    Date of hospital admission
 * `Specimen date`
   
    Date when specimen was received at laboratory
 * `Specimen type`
   
   Specimen type or group
 * `Specimen type (Numeric)`
   
   Translation of `"Specimen type"`
 * `Reason`
   
   Reason of request with Differential Diagnosis
 * `Isolate number`
   
   ID of isolate
 * `Organism type`
   
   Type of microorganism, can also be looked up using `mo_type()`
 * `Serotype`
   
   Serotype of microorganism
 * `Beta-lactamase`
   
   Microorganism produces beta-lactamase?
 * `ESBL`
   
   Microorganism produces extended spectrum beta-lactamase?
 * `Carbapenemase`
   
   Microorganism produces carbapenemase?
 * `MRSA screening test`
   
   Microorganism is possible MRSA?
 * `Inducible clindamycin resistance`
   
   Clindamycin can be induced?
 * `Comment`
   
   Other comments
 * `Date of data entry`
   
    Date this data was entered in WHONET
 * `AMP_ND10:CIP_EE`
   
   28 different antibiotics. You can lookup the abbreviations in the antibiotics data set, or use e.g. `ab_name("AMP")` to get the official name immediately. Before analysis, you should transform this to a valid antibiotic class, using `as.sir()`.

```r
WHONET
```

## Description

This example data set has the exact same structure as an export file from WHONET. Such files can be used with this package, as this example data set shows. The antibiotic results are from our example_isolates data set. All patient names were created using online surname generators and are only in place for practice purposes.

## Details

Like all data sets in this package, this data set is publicly available for download in the following formats: R, MS Excel, Apache Feather, Apache Parquet, SPSS, SAS, and Stata. Please visit [our website for the download links](https://msberends.github.io/AMR/articles/datasets.html). The actual files are of course available on [our GitHub repository](https://github.com/msberends/AMR/tree/main/data-raw).

## Examples

```r
WHONET
```



