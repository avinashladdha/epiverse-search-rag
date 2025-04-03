UTF-8

# Identify mutations between DNA sequences

## Description

The function `findMutations` identifies mutations (position and nature) of pairs of aligned DNA sequences. The function `graphMutations` does the same thing but plotting mutations on a directed graph.

Both functions are generics, but the only methods implemented in adegenet so far is for `DNAbin` objects.

```r
findMutations(...)

## S3 method for class 'DNAbin'
findMutations(x, from=NULL, to=NULL, allcomb=TRUE, ...)

graphMutations(...)

## S3 method for class 'DNAbin'
graphMutations(x, from=NULL, to=NULL, allcomb=TRUE, plot=TRUE,
               curved.edges=TRUE, ...)
```

## Arguments

- `x`: a `DNAbin` object containing aligned sequences, as a matrix.
- `from`: a vector indicating the DNA sequences from which mutations should be found. If `NULL`, all sequences are considered (i.e., `1:nrow(x)`).
- `to`: a vector indicating the DNA sequences to which mutations should be found. If `NULL`, all sequences are considered (i.e., `1:nrow(x)`).
- `allcomb`: a logical indicating whether all combinations of sequences (from and to) should be considered (TRUE, default), or not (FALSE).
- `plot`: a logical indicating whether the graph should be plotted.
- `curved.edges`: a logical indicating whether the edges of the graph should be curved.
- ``...``: further arguments to be passed to other methods. Used in `graphMutations` where it is passed to the plot method for `igraph` objects.

## Returns

For `findMutations`, a named list indicating the mutations from one sequence to another. For each comparison, a three-column matrix is provided, corresponding to the nucleotides in first and second sequence, and a summary of the mutation provided as: [position]:[nucleotide in first sequence]->[nucleotide in second sequence].

For `graphMutations`, a graph with the class `igraph`.

## See Also

The `fasta2DNAbin` to read fasta alignments with minimum RAM use.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk .

## Examples

```r
## Not run:

data(woodmouse)

## mutations between first 3 sequences
findMutations(woodmouse[1:3,])

## mutations from the first to sequences 2 and 3
findMutations(woodmouse[1:3,], from=1)

## same, graphical display
g <- graphMutations(woodmouse[1:3,], from=1)

## some manual checks
as.character(woodmouse)[1:3,35]
as.character(woodmouse)[1:3,36]
as.character(woodmouse)[1:3,106]
## End(Not run)
```



