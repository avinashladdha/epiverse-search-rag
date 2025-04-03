UTF-8

# Analyse the position of polymorphic sites

## Description

These functions are used to describe the distribution of polymorphic sites (SNPs) in an alignment.

The function `snpposi.plot` plots the positions and density of SNPs in the alignment.

The function `snpposi.test` tests whether SNPs are randomly distributed in the genome, the alternative hypothesis being that they are clustered. This test is based on the distances of each SNP to the closest SNP. This provides one measure of clustering for each SNP. Different statistics can be used to summarise these values (argument `stat`), but by default the statistics used is the median.

 `snpposi.plot` and `snpposi.test` are generic functions with methods for vectors of integers or numeric (indicating SNP position), and for `DNAbin` objects.

```r
snpposi.plot(...)

## S3 method for class 'integer'
snpposi.plot(x, genome.size, smooth=0.1,
              col="royalblue", alpha=.2, codon=TRUE, start.at=1, ...)

## S3 method for class 'numeric'
snpposi.plot(x, ...)

## S3 method for class 'DNAbin'
snpposi.plot(x, ...)


snpposi.test(...)

## S3 method for class 'integer'
snpposi.test(x, genome.size, n.sim=999, stat=median, ...)

## S3 method for class 'numeric'
snpposi.test(x, ...)

## S3 method for class 'DNAbin'
snpposi.test(x, ...)
```

## Arguments

- `x`: a vector of integers or numerics containing SNP positions, or a set of aligned sequences in a `DNAbin` object.
- `genome.size`: an integer indicating the length of genomes.
- `smooth`: a smoothing parameter for the density estimation; smaller values will give more local peaks; values have to be positive but can be less than 1.
- `col`: the color to be used for the plot; ignored if codon positions are represented.
- `alpha`: the alpha level to be used for transparency (density curve).
- `codon`: a logical indicating if codon position should be indicated (TRUE, default) or not.
- `start.at`: an integer indicating at which base of a codon the alignment starts (defaults to 1); values other than 1, 2 and 3 will be ignored.
- `n.sim`: an integer indicating the number of randomizations to be used in the Monte Carlo test.
- `stat`: a function used to summarize the measure of physical proximity between SNPs; by default, the median is used.
- ``...``: further arguments to be passed to the `integer` method.

## Returns

A Monte Carlo test of the class `randtest`.

## See Also

The `fasta2DNAbin` to read fasta alignments with minimum RAM use.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk .

## Examples

```r
if(require(ape)){
data(woodmouse)
snpposi.plot(woodmouse, codon=FALSE)
snpposi.plot(woodmouse)

## Not run:

snpposi.test(c(1,3,4,5), 100)
snpposi.test(woodmouse)
## End(Not run)

}
```



