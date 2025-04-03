# Parsing of raw data

```r
load_data(type = "extdata", ili.weighted = TRUE)
```

## Arguments

- `type`: the type of the data to be loaded. If `type=="extdata"` it loads the data to reproduce the PNAS paper, and if `type=="athdata"` it loads the data to reproduce the CID(?) paper.
- `ili.weighted`: logical indicator to specify whether to load weighted ILI or not, if `FALSE` unweighted ILI is loaded.

## Returns

A list of following named xts objects if `type=="extdata"`

 * `GC10` Google Correlate trained with ILI available as of 2010. Google Correlate has been deprecated by Google as of Dec 2019 and is no longer publicly available.
 * `GC09` Google Correlate trained with ILI available as of 2009.
 * `GT` Google Trends data for search queries identified using Google Correlate. Not directly available online, you have to manually input query terms at [https://trends.google.com/trends/](https://trends.google.com/trends/)
 * `CDC` CDC's ILI dataset. Available online at [https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html](https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html)
 * `GFT` Google Flu Trend (historical predictions).

A list of following named xts objects if `type=="athdata"`

 * `GT` Google Trends data for search queries identified. Not directly available online, you have to manually input query terms at [https://trends.google.com/trends/](https://trends.google.com/trends/)
 * `CDC` CDC's ILI dataset. Available online at [https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html](https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html)
 * `ili_idx` the indexing information that includes the week number and year number, the date of ending Saturday, and the season number Available online at [https://www.cdc.gov/flu/weekly/](https://www.cdc.gov/flu/weekly/)
 * `ATH` Athenahealth data that includes the proportion of "Flu Visit", "ILI Visit", and "Unspecified Viral or ILI Visit" compared to total number of visit to the Athenahealth partner healthcare providers.
 * `ili_unrevised` Historical unrevised ILI activity level. The unrevised ILI published on week ZZ of season XXXX-YYYY is available at `www.cdc.gov/flu/weekly/weeklyarchivesXXXX-YYYY/data/senAllregtZZ.html` or `.htm`. For example, original ILI report for week 7 of season 2015-2016 is available at [https://www.cdc.gov/flu/weekly/weeklyarchives2015-2016/data/senAllregt07.html](https://www.cdc.gov/flu/weekly/weeklyarchives2015-2016/data/senAllregt07.html), and original ILI report for week 50 of season 2012-2013 is available at [https://www.cdc.gov/flu/weekly/weeklyarchives2012-2013/data/senAllregt50.htm](https://www.cdc.gov/flu/weekly/weeklyarchives2012-2013/data/senAllregt50.htm)

## Description

Data related to the PNAS paper. Accessed on Nov 14, 2015.

## Details

Parse and load CDC's ILI data, Google Flu Trend data, Google Correlate data trained with ILI as of 2010, Google Correlate data trained with ILI as of 2009, Google Trend data with search terms identified from Google Correlate (2010 version).

Each week ends on the Saturday indicated in the xts object

Google Correlate data is standardized by Google, and we rescale it to 0 -- 100 during parsing. Google Trends data is in the scale of 0 -- 100.

## Examples

```r
system.file("extdata", "correlate-Influenza_like_Illness_h1n1_CDC_.csv", package = "argo")
system.file("extdata", "correlate-Influenza_like_Illness_CDC_.csv", package = "argo")
system.file("extdata", "GFT.csv", package = "argo")
system.file("extdata", "ILINet.csv", package = "argo")
load_data()
```

## References

Yang, S., Santillana, M., & Kou, S. C. (2015). Accurate estimation of influenza epidemics using Google search data via ARGO. Proceedings of the National Academy of Sciences. <doi:10.1073/pnas.1515373112>.



