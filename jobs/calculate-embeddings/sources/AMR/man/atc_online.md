# Get ATC Properties from WHOCC Website

## Source

[https://www.whocc.no/atc_ddd_alterations__cumulative/ddd_alterations/abbrevations/](https://www.whocc.no/atc_ddd_alterations__cumulative/ddd_alterations/abbrevations/)

```r
atc_online_property(
  atc_code,
  property,
  administration = "O",
  url = "https://www.whocc.no/atc_ddd_index/?code=%s&showdescription=no",
  url_vet = "https://www.whocc.no/atcvet/atcvet_index/?code=%s&showdescription=no"
)

atc_online_groups(atc_code, ...)

atc_online_ddd(atc_code, ...)

atc_online_ddd_units(atc_code, ...)
```

## Arguments

- `atc_code`: a character (vector) with ATC code(s) of antibiotics, will be coerced with `as.ab()` and `ab_atc()` internally if not a valid ATC code
- `property`: property of an ATC code. Valid values are `"ATC"`, `"Name"`, `"DDD"`, `"U"` (`"unit"`), `"Adm.R"`, `"Note"` and `groups`. For this last option, all hierarchical groups of an ATC code will be returned, see **Examples**.
- `administration`: type of administration when using `property = "Adm.R"`, see **Details**
- `url`: url of website of the WHOCC. The sign `%s` can be used as a placeholder for ATC codes.
- `url_vet`: url of website of the WHOCC for veterinary medicine. The sign `%s` can be used as a placeholder for ATC_vet codes (that all start with "Q").
- `...`: arguments to pass on to `atc_property`

## Description

Gets data from the WHOCC website to determine properties of an Anatomical Therapeutic Chemical (ATC) (e.g. an antibiotic), such as the name, defined daily dose (DDD) or standard unit.

## Details

Options for argument `administration`:

 * `"Implant"` = Implant
 * `"Inhal"` = Inhalation
 * `"Instill"` = Instillation
 * `"N"` = nasal
 * `"O"` = oral
 * `"P"` = parenteral
 * `"R"` = rectal
 * `"SL"` = sublingual/buccal
 * `"TD"` = transdermal
 * `"V"` = vaginal

Abbreviations of return values when using `property = "U"` (unit):

 * `"g"` = gram
 * `"mg"` = milligram
 * `"mcg"` = microgram
 * `"U"` = unit
 * `"TU"` = thousand units
 * `"MU"` = million units
 * `"mmol"` = millimole
 * `"ml"` = millilitre (e.g. eyedrops)

N.B. This function requires an internet connection and only works ifthe following packages are installed: ‘curl’, ‘rvest’, ‘xml2’. 

## Examples

```r
if (requireNamespace("curl") && requireNamespace("rvest") && requireNamespace("xml2")) {
  # oral DDD (Defined Daily Dose) of amoxicillin
  atc_online_property("J01CA04", "DDD", "O")
  atc_online_ddd(ab_atc("amox"))

  # parenteral DDD (Defined Daily Dose) of amoxicillin
  atc_online_property("J01CA04", "DDD", "P")

  atc_online_property("J01CA04", property = "groups") # search hierarchical groups of amoxicillin
}
```



