 package

utf-8

# The adegenet package

## Description

This package is devoted to the multivariate analysis of genetic markers data. These data can be codominant markers (e.g. microsatellites) or presence/absence data (e.g. AFLP), and have any level of ploidy. 'adegenet' defines three formal (S4) classes:

- genind : a class for data of individuals ("genind" stands for genotypes-individuals).

- genpop : a class for data of groups of individuals ("genpop" stands for genotypes-populations)

- genlight : a class for genome-wide SNP data

## Details

For more information about these classes, type "class ? genind", "class ? genpop", or "?genlight".

Essential functionalities of the package are presented througout 4 tutorials, accessible using `adegenetTutorial(which="name-below")`:

- `basics`: introduction to the package.

- `spca`: multivariate analysis of spatial genetic patterns.

- `dapc`: population structure and group assignment using DAPC.

- `genomics`: introduction to the class genlight for the handling and analysis of genome-wide SNP data.

Note: In older versions of adegenet, these tutorials were avilable as vignettes, accessible through the function `vignette("name-below", package="adegenet")`:

- `adegenet-basics`.

- `adegenet-spca`.

- `adegenet-dapc`.

- `adegenet-genomics`.

Important functions are also summarized below.

=== IMPORTING DATA ===

= TO GENIND OBJECTS =

 `adegenet` imports data to genind object from the following softwares:

- STRUCTURE: see `read.structure`

- GENETIX: see `read.genetix`

- FSTAT: see `read.fstat`

- Genepop: see `read.genepop`

To import data from any of these formats, you can also use the general function `import2genind`.

In addition, it can extract polymorphic sites from nucleotide and amino-acid alignments:

- DNA files: use `read.dna` from the ape package, and then extract SNPs from DNA alignments using `DNAbin2genind`.

- protein sequences alignments: polymorphic sites can be extracted from protein sequences alignments in `alignment` format (package `seqinr`, see `as.alignment`) using the function `alignment2genind`.

The function `fasta2DNAbin` allows for reading fasta files into DNAbin object with minimum RAM requirements.

It is also possible to read genotypes coded by character strings from a data.frame in which genotypes are in rows, markers in columns. For this, use `df2genind`. Note that `df2genind` can be used for any level of ploidy.

= TO GENLIGHT OBJECTS =

SNP data can be read from the following formats:

- PLINK: see function `read.PLINK`

- .snp (adegenet's own format): see function `read.snp`

SNP can also be extracted from aligned DNA sequences with the fasta format, using `fasta2genlight`

=== EXPORTING DATA ===

 `adegenet` exports data from

Genotypes can also be recoded from a genind object into a data.frame of character strings, using any separator between alleles. This covers formats from many softwares like GENETIX or STRUCTURE. For this, see `genind2df`.

Also note that the `pegas` package imports genind objects using the function `as.loci`.

=== MANIPULATING DATA ===

Several functions allow one to manipulate genind or genpop objects

- `genind2genpop`: convert a genind object to a genpop

- `seploc`: creates one object per marker; for genlight objects, creates blocks of SNPs.

- `seppop`: creates one object per population

- - `tab`: access the allele data (counts or frequencies) of an object (genind and genpop )

- x[i,j]: create a new object keeping only genotypes (or populations) indexed by 'i' and the alleles indexed by 'j'.

- `makefreq`: returns a table of allelic frequencies from a genpop object.

- `repool` merges genoptypes from different gene pools into one single genind object.

- `propTyped` returns the proportion of available (typed) data, by individual, population, and/or locus.

- `selPopSize` subsets data, retaining only genotypes from a population whose sample size is above a given level.

- `pop` sets the population of a set of genotypes.

=== ANALYZING DATA ===

Several functions allow to use usual, and less usual analyses:

- `HWE.test.genind`: performs HWE test for all populations and loci combinations

- `dist.genpop`: computes 5 genetic distances among populations.

- `monmonier`: implementation of the Monmonier algorithm, used to seek genetic boundaries among individuals or populations. Optimized boundaries can be obtained using `optimize.monmonier`. Object of the class `monmonier` can be plotted and printed using the corresponding methods.

- `spca`: implements Jombart et al. (2008) spatial Principal Component Analysis

- `global.rtest`: implements Jombart et al. (2008) test for global spatial structures

- `local.rtest`: implements Jombart et al. (2008) test for local spatial structures

- `propShared`: computes the proportion of shared alleles in a set of genotypes (i.e. from a genind object)

- `propTyped`: function to investigate missing data in several ways

- `scaleGen`: generic method to scale genind or genpop before a principal component analysis

- `Hs`: computes the average expected heterozygosity by population in a genpop . Classically Used as a measure of genetic diversity.

- `find.clusters` and `dapc`: implement the Discriminant Analysis of Principal Component (DAPC, Jombart et al., 2010).

- `seqTrack`: implements the SeqTrack algorithm for recontructing transmission trees of pathogens (Jombart et al., 2010) .


`glPca`: implements PCA for genlight objects.

- `gengraph`: implements some simple graph-based clustering using genetic data. - `snpposi.plot` and `snpposi.test`: visualize the distribution of SNPs on a genetic sequence and test their randomness. - `adegenetServer`: opens up a web interface for some functionalities of the package (DAPC with cross validation and feature selection).

=== GRAPHICS ===

- `colorplot`: plots points with associated values for up to three variables represented by colors using the RGB system; useful for spatial mapping of principal components.

- `loadingplot`: plots loadings of variables. Useful for representing the contribution of alleles to a given principal component in a multivariate method.

- `scatter.dapc`: scatterplots for DAPC results.

- `compoplot`: plots membership probabilities from a DAPC object.

=== SIMULATING DATA ===

- `hybridize`: implements hybridization between two populations.

- `haploGen`: simulates genealogies of haplotypes, storing full genomes.


`glSim`: simulates simple genlight objects.

=== DATASETS ===

- `H3N2`: Seasonal influenza (H3N2) HA segment data.

- `dapcIllus`: Simulated data illustrating the DAPC.

- `eHGDP`: Extended HGDP-CEPH dataset.

- `microbov`: Microsatellites genotypes of 15 cattle breeds.

- `nancycats`: Microsatellites genotypes of 237 cats from 17 colonies of Nancy (France).

- `rupica`: Microsatellites genotypes of 335 chamois (Rupicapra rupicapra) from the Bauges mountains (France).

- `sim2pop`: Simulated genotypes of two georeferenced populations.

- `spcaIllus`: Simulated data illustrating the sPCA.

For more information, visit the adegenet website using the function `adegenetWeb`.

Tutorials are available via the command `adegenetTutorial`.

To cite adegenet, please use the reference given by `citation("adegenet")` (or see references below).

## References

Jombart T. (2008) adegenet: a R package for the multivariate analysis of genetic markers **Bioinformatics** 24: 1403-1405. doi: 10.1093/bioinformatics/btn129

Jombart T. and Ahmed I. (2011) adegenet 1.3-1: new tools for the analysis of genome-wide SNP data. **Bioinformatics**. doi: 10.1093/bioinformatics/btr521

Jombart T, Devillard S and Balloux F (2010) Discriminant analysis of principal components: a new method for the analysis of genetically structured populations. BMC Genetics 11:94. doi:10.1186/1471-2156-11-94

Jombart T, Eggo R, Dodd P, Balloux F (2010) Reconstructing disease outbreaks from genetic data: a graph approach. **Heredity**. doi: 10.1038/hdy.2010.78.

Jombart, T., Devillard, S., Dufour, A.-B. and Pontier, D. (2008) Revealing cryptic spatial patterns in genetic variability by a new multivariate method. **Heredity**, 101 , 92--103.

See adegenet website: [http://adegenet.r-forge.r-project.org/](http://adegenet.r-forge.r-project.org/)

Please post your questions on 'the adegenet forum': adegenet-forum@lists.r-forge.r-project.org

## See Also

adegenet is related to several packages, in particular:

- `ade4` for multivariate analysis

- `pegas` for population genetics tools

- `ape` for phylogenetics and DNA data handling

- `seqinr` for handling nucleic and proteic sequences

- `shiny` for R-based web interfaces

## Author(s)

Thibaut Jombart <t.jombart@imperial.ac.uk>

Developers: Zhian N. Kamvar <zkamvar@gmail.com>, Caitlin Collins <caitiecollins17@gmail.com>, Ismail Ahmed <ismail.ahmed@inserm.fr>, Federico Calboli, Tobias Erik Reiners, Peter Solymos, Anne Cori,

Contributed datasets from: Katayoun Moazami-Goudarzi, Denis Laloë, Dominique Pontier, Daniel Maillard, Francois Balloux.



