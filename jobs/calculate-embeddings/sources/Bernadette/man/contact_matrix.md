# Country-specific contact matrix

```r
contact_matrix(country)
```

## Arguments

- `country`: A character indicating the country identifier. See country_contact_matrices .

## Returns

An object of class "data.frame".

## Description

A 16 by 16 contact matrix whose row i of a column j corresponds to the number of contacts made by an individual in group i with an individual in group j.

## Examples

```r
conmat <- contact_matrix(country = "GRC")
```

## References

Prem, K., van Zandvoort, K., Klepac, P. et al (2020). Projecting contact matrices in 177 geographical regions: an update and comparison with empirical data for the COVID-19 era. medRxiv 2020.07.22.20159772; doi: https://doi.org/10.1101/2020.07.22.20159772



