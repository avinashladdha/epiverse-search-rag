# Retrieve Antiviral Drug Names and Doses from Clinical Text

```r
av_from_text(
  text,
  type = c("drug", "dose", "administration"),
  collapse = NULL,
  translate_av = FALSE,
  thorough_search = NULL,
  info = interactive(),
  ...
)
```

## Arguments

- `text`: text to analyse
- `type`: type of property to search for, either `"drug"`, `"dose"` or `"administration"`, see **Examples**
- `collapse`: a character to pass on to `paste(, collapse = ...)` to only return one character per element of `text`, see **Examples**
- `translate_av`: if `type = "drug"`: a column name of the antivirals data set to translate the antibiotic abbreviations to, using `av_property()`. The default is `FALSE`. Using `TRUE` is equal to using "name".
- `thorough_search`: a logical to indicate whether the input must be extensively searched for misspelling and other faulty input values. Setting this to `TRUE` will take considerably more time than when using `FALSE`. At default, it will turn `TRUE` when all input elements contain a maximum of three words.
- `info`: a logical to indicate whether a progress bar should be printed - the default is `TRUE` only in interactive mode
- `...`: arguments passed on to `as.av()`

## Returns

A list , or a character if `collapse` is not `NULL`

## Description

Use this function on e.g. clinical texts from health care records. It returns a list with all antiviral drugs, doses and forms of administration found in the texts.

## Details

This function is also internally used by `as.av()`, although it then only searches for the first drug name and will throw a note if more drug names could have been returned. Note: the `as.av()` function may use very long regular expression to match brand names of antiviral drugs. This may fail on some systems.

### Argument `type`

 At default, the function will search for antiviral drug names. All text elements will be searched for official names, ATC codes and brand names. As it uses `as.av()` internally, it will correct for misspelling.

With `type = "dose"` (or similar, like "dosing", "doses"), all text elements will be searched for numeric values that are higher than 100 and do not resemble years. The output will be numeric . It supports any unit (g, mg, IE, etc.) and multiple values in one clinical text, see **Examples**.

With `type = "administration"` (or abbreviations, like "admin", "adm"), all text elements will be searched for a form of drug administration. It supports the following forms (including common abbreviations): buccal, implant, inhalation, instillation, intravenous, nasal, oral, parenteral, rectal, sublingual, transdermal and vaginal. Abbreviations for oral (such as 'po', 'per os') will become "oral", all values for intravenous (such as 'iv', 'intraven') will become "iv". It supports multiple values in one clinical text, see **Examples**.

### Argument `collapse`

 Without using `collapse`, this function will return a list . This can be convenient to use e.g. inside a `mutate()`):


`df %>% mutate(avx = av_from_text(clinical_text))`

The returned AV codes can be transformed to official names, groups, etc. with all `av_*` functions such as `av_name()` and `av_group()`, or by using the `translate_av` argument.

With using `collapse`, this function will return a character :


`df %>% mutate(avx = av_from_text(clinical_text, collapse = "|"))`

## Examples

```r
av_from_text("28/03/2020 valaciclovir po tid")
av_from_text("28/03/2020 valaciclovir po tid", type = "admin")
```



