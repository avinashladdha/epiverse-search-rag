UTF-8

methods

# Auxiliary functions for adegenet

## Description

adegenet implements a number of auxiliary procedures that might be of interest for users. These include graphical tools to translate variables (numeric or factors) onto a color scale, adding transparency to existing colors, pre-defined color palettes, extra functions to access documentation, and low-level treatment of character vectors.

These functions are mostly auxiliary procedures used internally in adegenet.

These items include:

 * `num2col`: translates a numeric vector into colors.
 * `fac2col`: translates a factor into colors.
 * `any2col`: translates a vector of type numeric, character or factor into colors.
 * `transp`: adds transparency to a vector of colors. Note that transparent colors are not supported on some graphical devices.
 * `corner`: adds text to a corner of a figure.
 * `checkType`: checks the type of markers being used in a function and issues an error if appropriate.
 * `.rmspaces`: remove peripheric spaces in a character string.
 * `.genlab`: generate labels in a correct alphanumeric ordering.
 * `.readExt`: read the extension of a given file.
 * `.render.server.info` used to display session information for the dapcServer

Color palettes include:

 * `bluepal`: white -\> dark blue
 * `redpal`: white -\> dark red
 * `greenpal`: white -\> dark green
 * `greypal`: white -\> dark grey
 * `flame`: gold -\> red
 * `azur`: gold -\> blue
 * `seasun`: blue -\> gold -\> red
 * `lightseasun`: blue -\> gold -\> red (light variant)
 * `deepseasun`: blue -\> gold -\> red (deep variant)
 * `spectral`: red -\> yellow -\> blue (RColorBrewer variant)
 * `wasp`: gold -\> brown -\> black
 * `funky`: many colors
 * `virid`: adaptation of the `viridis` palette, from the `viridis` package.
 * `hybridpal`: reorder a color palette (`virid` by default) to display sharp contrast between the first two colors, and interpolated colors after; ideal for datasets where two parental populations are provided first, followed by various degrees of hybrids.

## See Also

The R package RColorBrewer, proposing a nice selection of color palettes. The `viridis` package, with many excellent palettes.

```r
.genlab(base, n)
corner(text, posi="topleft",  inset=0.1, ...)
num2col(x, col.pal=heat.colors, reverse=FALSE,
        x.min=min(x,na.rm=TRUE), x.max=max(x,na.rm=TRUE),
        na.col="transparent")
fac2col(x, col.pal=funky, na.col="transparent", seed=NULL)
any2col(x, col.pal=seasun, na.col="transparent")
transp(col, alpha=.5)
hybridpal(col.pal = virid)
```

## Arguments

- `base`: a character string forming the base of the labels
- `n`: the number of labels to generate
- `text`: a character string to be added to the plot
- `posi`: a character matching any combinations of "top/bottom" and "left/right".
- `inset`: a vector of two numeric values (recycled if needed) indicating the inset, as a fraction of the plotting region.
- ``...``: further arguments to be passed to `text`
- `x`: a numeric vector (for `num2col`) or a vector converted to a factor (for `fac2col`).
- `col.pal`: a function generating colors according to a given palette.
- `reverse`: a logical stating whether the palette should be inverted (TRUE), or not (FALSE, default).
- `x.min`: the minimal value from which to start the color scale
- `x.max`: the maximal value from which to start the color scale
- `na.col`: the color to be used for missing values (NAs)
- `seed`: a seed for R's random number generated, used to fix the random permutation of colors in the palette used; if NULL, no randomization is used and the colors are taken from the palette according to the ordering of the levels.
- `col`: a vector of colors
- `alpha`: a numeric value between 0 and 1 representing the alpha coefficient; 0: total transparency; 1: no transparency.

## Returns

For `.genlab`, a character vector of size "n". `num2col` and `fac2col` return a vector of colors. `any2col` returns a list with the following components: `$col` (a vector of colors), `$leg.col` (colors for the legend), and `$leg.txt` (text for the legend).

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
.genlab("Locus-",11)

## transparent colors using "transp"
plot(rnorm(1000), rnorm(1000), col=transp("blue",.3), pch=20, cex=4)


## numeric values to color using num2col
plot(1:100, col=num2col(1:100), pch=20, cex=4)
plot(1:100, col=num2col(1:100, col.pal=bluepal), pch=20, cex=4)
plot(1:100, col=num2col(1:100, col.pal=flame), pch=20, cex=4)
plot(1:100, col=num2col(1:100, col.pal=wasp), pch=20, cex=4)
plot(1:100, col=num2col(1:100, col.pal=azur,rev=TRUE), pch=20, cex=4)
plot(1:100, col=num2col(1:100, col.pal=spectral), pch=20, cex=4)
plot(1:100, col=num2col(1:100, col.pal=virid), pch=20, cex=4)

## factor as colors using fac2col
dat <- cbind(c(rnorm(50,8), rnorm(100), rnorm(150,3),
rnorm(50,10)),c(rnorm(50,1),rnorm(100),rnorm(150,3), rnorm(50,5)))
fac <- rep(letters[1:4], c(50,100,150,50))
plot(dat, col=fac2col(fac), pch=19, cex=4)
plot(dat, col=transp(fac2col(fac)), pch=19, cex=4)
plot(dat, col=transp(fac2col(fac,seed=2)), pch=19, cex=4)

## use of any2col
x <- factor(1:10)
col.info <- any2col(x, col.pal=funky)
plot(x, col=col.info$col, main="Use of any2col on a factor")
legend("bottomleft", fill=col.info$leg.col, legend=col.info$leg.txt, bg="white")

x <- 100:1
col.info <- any2col(x, col.pal=wasp)
barplot(x, col=col.info$col, main="Use of any2col on a numeric")
legend("bottomleft", fill=col.info$leg.col, legend=col.info$leg.txt, bg="white")
```



