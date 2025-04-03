# Italicise Taxonomic Families, Genera, Species, Subspecies

```r
italicise_taxonomy(string, type = c("markdown", "ansi"))

italicize_taxonomy(string, type = c("markdown", "ansi"))
```

## Arguments

- `string`: a character (vector)
- `type`: type of conversion of the taxonomic names, either "markdown" or "ansi", see **Details**

## Description

According to the binomial nomenclature, the lowest four taxonomic levels (family, genus, species, subspecies) should be printed in italics. This function finds taxonomic names within strings and makes them italic.

## Details

This function finds the taxonomic names and makes them italic based on the microorganisms data set.

The taxonomic names can be italicised using markdown (the default) by adding `*` before and after the taxonomic names, or using ANSI colours by adding `\033[3m` before and `\033[23m` after the taxonomic names. If multiple ANSI colours are not available, no conversion will occur.

This function also supports abbreviation of the genus if it is followed by a species, such as "E. coli" and "K. pneumoniae ozaenae".

## Examples

```r
italicise_taxonomy("An overview of Staphylococcus aureus isolates")
italicise_taxonomy("An overview of S. aureus isolates")

cat(italicise_taxonomy("An overview of S. aureus isolates", type = "ansi"))
```



