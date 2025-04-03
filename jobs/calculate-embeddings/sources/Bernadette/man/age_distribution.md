# Country-specific age distribution

```r
age_distribution(country, year)
```

## Arguments

- `country`: character; country identifier, following the List of United Nations Member States. See countries_un .
- `year`: numeric; calendar year.

## Returns

An object of class **data.frame** that contains the age distribution.

## Description

Function to extract the age distribution of a country for a given year, broken down by 5-year age bands and gender, following the United Nations 2019 Revision of World Population Prospects.

## Examples

```r
# Age distribution for Greece in 2020:
age_distr <- age_distribution(country = "Greece", year = 2020)
```

## References

United Nations, Department of Economic and Social Affairs, Population Division (2019). World Population Prospects 2019, Online Edition. Rev. 1.

Prem, K., van Zandvoort, K., Klepac, P. et al (2017). Projecting contact matrices in 177 geographical regions: an update and comparison with empirical data for the COVID-19 era. medRxiv 2020.07.22.20159772; doi: https://doi.org/10.1101/2020.07.22.20159772



