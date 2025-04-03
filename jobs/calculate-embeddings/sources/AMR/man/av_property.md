# Get Properties of an Antiviral Drug

```r
av_name(x, language = get_AMR_locale(), tolower = FALSE, ...)

av_cid(x, ...)

av_synonyms(x, ...)

av_tradenames(x, ...)

av_group(x, language = get_AMR_locale(), ...)

av_atc(x, ...)

av_loinc(x, ...)

av_ddd(x, administration = "oral", ...)

av_ddd_units(x, administration = "oral", ...)

av_info(x, language = get_AMR_locale(), ...)

av_url(x, open = FALSE, ...)

av_property(x, property = "name", language = get_AMR_locale(), ...)
```

## Arguments

- `x`: any (vector of) text that can be coerced to a valid antiviral drug code with `as.av()`
- `language`: language of the returned text - the default is system language (see `get_AMR_locale()`) and can also be set with the package option `AMR_locale`. Use `language = NULL` or `language = ""` to prevent translation.
- `tolower`: a logical to indicate whether the first character of every output should be transformed to a lower case character .
- `...`: other arguments passed on to `as.av()`
- `administration`: way of administration, either `"oral"` or `"iv"`
- `open`: browse the URL using `utils::browseURL()`
- `property`: one of the column names of one of the antivirals data set: `vector_or(colnames(antivirals), sort = FALSE)`.

## Returns

 * An integer in case of `av_cid()`
 * A named list in case of `av_info()` and multiple `av_atc()`/`av_synonyms()`/`av_tradenames()`
 * A double in case of `av_ddd()`
 * A character in all other cases

## Description

Use these functions to return a specific property of an antiviral drug from the antivirals data set. All input values will be evaluated internally with `as.av()`.

## Details

All output will be translated where possible.

The function `av_url()` will return the direct URL to the official WHO website. A warning will be returned if the required ATC code is not available.

## Source

 World Health Organization (WHO) Collaborating Centre for Drug Statistics Methodology: [https://www.whocc.no/atc_ddd_index/](https://www.whocc.no/atc_ddd_index/)

European Commission Public Health PHARMACEUTICALS - COMMUNITY REGISTER: [https://ec.europa.eu/health/documents/community-register/html/reg_hum_atc.htm](https://ec.europa.eu/health/documents/community-register/html/reg_hum_atc.htm)

## Reference Data Publicly Available

 All data sets in this `AMR` package (about microorganisms, antibiotics, SIR interpretation, EUCAST rules, etc.) are publicly and freely available for download in the following formats: R, MS Excel, Apache Feather, Apache Parquet, SPSS, SAS, and Stata. We also provide tab-separated plain text files that are machine-readable and suitable for input in any software program, such as laboratory information systems. Please visit [our website for the download links](https://msberends.github.io/AMR/articles/datasets.html). The actual files are of course available on [our GitHub repository](https://github.com/msberends/AMR/tree/main/data-raw).

## Examples

```r
# all properties:
av_name("ACI")
av_atc("ACI")
av_cid("ACI")
av_synonyms("ACI")
av_tradenames("ACI")
av_group("ACI")
av_url("ACI")

# lowercase transformation
av_name(x = c("ACI", "VALA"))
av_name(x = c("ACI", "VALA"), tolower = TRUE)

# defined daily doses (DDD)
av_ddd("ACI", "oral")
av_ddd_units("ACI", "oral")
av_ddd("ACI", "iv")
av_ddd_units("ACI", "iv")

av_info("ACI") # all properties as a list

# all av_* functions use as.av() internally, so you can go from 'any' to 'any':
av_atc("ACI")
av_group("J05AB01")
av_loinc("abacavir")
av_name("29113-8")
av_name(135398513)
av_name("J05AB01")
```

## See Also

antivirals



