# Get Properties of an Antibiotic

```r
ab_name(x, language = get_AMR_locale(), tolower = FALSE, ...)

ab_cid(x, ...)

ab_synonyms(x, ...)

ab_tradenames(x, ...)

ab_group(x, language = get_AMR_locale(), ...)

ab_atc(x, only_first = FALSE, ...)

ab_atc_group1(x, language = get_AMR_locale(), ...)

ab_atc_group2(x, language = get_AMR_locale(), ...)

ab_loinc(x, ...)

ab_ddd(x, administration = "oral", ...)

ab_ddd_units(x, administration = "oral", ...)

ab_info(x, language = get_AMR_locale(), ...)

ab_url(x, open = FALSE, ...)

ab_property(x, property = "name", language = get_AMR_locale(), ...)

set_ab_names(
  data,
  ...,
  property = "name",
  language = get_AMR_locale(),
  snake_case = NULL
)
```

## Arguments

- `x`: any (vector of) text that can be coerced to a valid antibiotic drug code with `as.ab()`
- `language`: language of the returned text - the default is the current system language (see `get_AMR_locale()`) and can also be set with the package option `AMR_locale`. Use `language = NULL` or `language = ""` to prevent translation.
- `tolower`: a logical to indicate whether the first character of every output should be transformed to a lower case character . This will lead to e.g. "polymyxin B" and not "polymyxin b".
- `...`: in case of `set_ab_names()` and `data` is a data.frame : columns to select (supports tidy selection such as `column1:column4`), otherwise other arguments passed on to `as.ab()`
- `only_first`: a logical to indicate whether only the first ATC code must be returned, with giving preference to J0-codes (i.e., the antimicrobial drug group)
- `administration`: way of administration, either `"oral"` or `"iv"`
- `open`: browse the URL using `utils::browseURL()`
- `property`: one of the column names of one of the antibiotics data set: `vector_or(colnames(antibiotics), sort = FALSE)`.
- `data`: a data.frame of which the columns need to be renamed, or a character vector of column names
- `snake_case`: a logical to indicate whether the names should be in so-called [snake case](https://en.wikipedia.org/wiki/Snake_case): in lower case and all spaces/slashes replaced with an underscore (`_`)

## Returns

 * An integer in case of `ab_cid()`
 * A named list in case of `ab_info()` and multiple `ab_atc()`/`ab_synonyms()`/`ab_tradenames()`
 * A double in case of `ab_ddd()`
 * A data.frame in case of `set_ab_names()`
 * A character in all other cases

## Description

Use these functions to return a specific property of an antibiotic from the antibiotics data set. All input values will be evaluated internally with `as.ab()`.

## Details

All output will be translated where possible.

The function `ab_url()` will return the direct URL to the official WHO website. A warning will be returned if the required ATC code is not available.

The function `set_ab_names()` is a special column renaming function for data.frame s. It renames columns names that resemble antimicrobial drugs. It always makes sure that the new column names are unique. If `property = "atc"` is set, preference is given to ATC codes from the J-group.

## Source

 World Health Organization (WHO) Collaborating Centre for Drug Statistics Methodology: [https://www.whocc.no/atc_ddd_index/](https://www.whocc.no/atc_ddd_index/)

European Commission Public Health PHARMACEUTICALS - COMMUNITY REGISTER: [https://ec.europa.eu/health/documents/community-register/html/reg_hum_atc.htm](https://ec.europa.eu/health/documents/community-register/html/reg_hum_atc.htm)

## Reference Data Publicly Available

 All data sets in this `AMR` package (about microorganisms, antibiotics, SIR interpretation, EUCAST rules, etc.) are publicly and freely available for download in the following formats: R, MS Excel, Apache Feather, Apache Parquet, SPSS, SAS, and Stata. We also provide tab-separated plain text files that are machine-readable and suitable for input in any software program, such as laboratory information systems. Please visit [our website for the download links](https://msberends.github.io/AMR/articles/datasets.html). The actual files are of course available on [our GitHub repository](https://github.com/msberends/AMR/tree/main/data-raw).

## Examples

```r
# all properties:
ab_name("AMX")
ab_atc("AMX")
ab_cid("AMX")
ab_synonyms("AMX")
ab_tradenames("AMX")
ab_group("AMX")
ab_atc_group1("AMX")
ab_atc_group2("AMX")
ab_url("AMX")

# smart lowercase transformation
ab_name(x = c("AMC", "PLB"))
ab_name(x = c("AMC", "PLB"), tolower = TRUE)

# defined daily doses (DDD)
ab_ddd("AMX", "oral")
ab_ddd_units("AMX", "oral")
ab_ddd("AMX", "iv")
ab_ddd_units("AMX", "iv")

ab_info("AMX") # all properties as a list

# all ab_* functions use as.ab() internally, so you can go from 'any' to 'any':
ab_atc("AMP")
ab_group("J01CA01")
ab_loinc("ampicillin")
ab_name("21066-6")
ab_name(6249)
ab_name("J01CA01")

# spelling from different languages and dyslexia are no problem
ab_atc("ceftriaxon")
ab_atc("cephtriaxone")
ab_atc("cephthriaxone")
ab_atc("seephthriaaksone")

# use set_ab_names() for renaming columns
colnames(example_isolates)
colnames(set_ab_names(example_isolates))
colnames(set_ab_names(example_isolates, NIT:VAN))

if (require("dplyr")) {
  example_isolates %>%
    set_ab_names()

  # this does the same:
  example_isolates %>%
    rename_with(set_ab_names)

  # set_ab_names() works with any AB property:
  example_isolates %>%
    set_ab_names(property = "atc")

  example_isolates %>%
    set_ab_names(where(is.sir)) %>%
    colnames()

  example_isolates %>%
    set_ab_names(NIT:VAN) %>%
    colnames()
}
```

## See Also

antibiotics



