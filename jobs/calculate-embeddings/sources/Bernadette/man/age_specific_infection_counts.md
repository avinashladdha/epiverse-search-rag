 data

# Age distribution of new reported infections for Greece

## Format

A data frame with 210 rows and 8 variables:

- **Index**: integer; a sequence of integer numbers from 1 to 210
- **Right**: numeric; Index + 1
- **Date**: Date, format; date in the format "2020-08-31"
- **Week_ID**: numeric; index of the week that each day falls into. A week is assumed to have 7 days
- **Total_Cases**: numeric; count of total reported infections on a given date
- **0-39**: numeric; count of reported infections on a given date for the age group "0-39"
- **40-64**: numeric; count of reported infections on a given date for the age group "40-64"
- **65+**: numeric; count of reported infections on a given date for the age group "65+"

## Source

[https://github.com/Sandbird/covid19-Greece/](https://github.com/Sandbird/covid19-Greece/)

```r
data(age_specific_infection_counts)
```

## Returns

A data.frame object with 210 rows and 8 variables.

## Description

A dataset containing the age distribution of new reported infections in Greece from 2020-08-31 to 2021-03-28 (30 weeks). The dataset has been extracted from the Hellenic National Public Health Organization database.

## References

 Sandbird (2022). Daily regional statistics for covid19 cases in Greece.



