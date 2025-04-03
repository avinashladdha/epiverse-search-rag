UTF-8

# Graphics for Discriminant Analysis of Principal Components (DAPC)

## Description

These functions provide graphic outputs for Discriminant Analysis of Principal Components (DAPC, Jombart et al. 2010). See `?dapc` for details about this method. DAPC graphics are detailed in the DAPC tutorial accessible using `vignette("adegenet-dapc")`.

These functions all require an object of class `dapc` (the ".dapc" can be ommitted when calling the functions):

- `scatter.dapc`: produces scatterplots of principal components (or 'discriminant functions'), with a screeplot of eigenvalues as inset.

- `assignplot`: plot showing the probabilities of assignment of individuals to the different clusters.

```r
## S3 method for class 'dapc'
scatter(x, xax=1, yax=2, grp=x$grp, col=seasun(length(levels(grp))),
      pch=20, bg="white", solid=.7, scree.da=TRUE,
      scree.pca=FALSE, posi.da="bottomright",
      posi.pca="bottomleft", bg.inset="white", ratio.da=.25,
      ratio.pca=.25, inset.da=0.02, inset.pca=0.02,
      inset.solid=.5, onedim.filled=TRUE, mstree=FALSE, lwd=1,
      lty=1, segcol="black", legend=FALSE, posi.leg="topright",
      cleg=1, txt.leg=levels(grp), cstar = 1, cellipse = 1.5,
      axesell = FALSE, label = levels(grp), clabel = 1, xlim =
      NULL, ylim = NULL, grid = FALSE, addaxes = TRUE, origin =
      c(0,0), include.origin = TRUE, sub = "", csub = 1, possub =
      "bottomleft", cgrid = 1, pixmap = NULL, contour = NULL, area
      = NULL, label.inds = NULL, ...)

assignplot(x, only.grp=NULL, subset=NULL, new.pred=NULL, cex.lab=.75,pch=3)
```

## Arguments

- `x`: a `dapc` object.
- `xax,yax`: `integers` specifying which principal components of DAPC should be shown in x and y axes.
- `grp`: a factor defining group membership for the individuals. The scatterplot is optimal only for the default group, i.e. the one used in the DAPC analysis.
- `col`: a suitable color to be used for groups. The specified vector should match the number of groups, not the number of individuals.
- `pch`: a `numeric` indicating the type of point to be used to indicate the prior group of individuals (see `points` documentation for more details); one value is expected for each group; recycled if necessary.
- `bg`: the color used for the background of the scatterplot.
- `solid`: a value between 0 and 1 indicating the alpha level for the colors of the plot; 0=full transparency, 1=solid colours.
- `scree.da`: a logical indicating whether a screeplot of Discriminant Analysis eigenvalues should be displayed in inset (TRUE) or not (FALSE).
- `scree.pca`: a logical indicating whether a screeplot of Principal Component Analysis eigenvalues should be displayed in inset (TRUE) or not (FALSE); retained axes are displayed in black.
- `posi.da`: the position of the inset of DA eigenvalues; can match any combination of "top/bottom" and "left/right".
- `posi.pca`: the position of the inset of PCA eigenvalues; can match any combination of "top/bottom" and "left/right".
- `bg.inset`: the color to be used as background for the inset plots.
- `ratio.da`: the size of the inset of DA eigenvalues as a proportion of the current plotting region.
- `ratio.pca`: the size of the inset of PCA eigenvalues as a proportion of the current plotting region.
- `inset.da`: a vector with two numeric values (recycled if needed) indicating the inset to be used for the screeplot of DA eigenvalues as a proportion of the current plotting region; see `?add.scatter` for more details.
- `inset.pca`: a vector with two numeric values (recycled if needed) indicating the inset to be used for the screeplot of PCA eigenvalues as a proportion of the current plotting region; see `?add.scatter` for more details.
- `inset.solid`: a value between 0 and 1 indicating the alpha level for the colors of the inset plots; 0=full transparency, 1=solid colours.
- `onedim.filled`: a logical indicating whether curves should be filled when plotting a single discriminant function (TRUE), or not (FALSE).
- `mstree`: a logical indicating whether a minimum spanning tree linking the groups and based on the squared distances between the groups inside the entire space should added to the plot (TRUE), or not (FALSE).
- `lwd,lty,segcol`: the line width, line type, and segment colour to be used for the minimum spanning tree.
- `legend`: a logical indicating whether a legend for group colours should added to the plot (TRUE), or not (FALSE).
- `posi.leg`: the position of the legend for group colours; can match any combination of "top/bottom" and "left/right", or a set of x/y coordinates stored as a list (`locator` can be used).
- `cleg`: a size factor used for the legend.
- `cstar,cellipse,axesell,label,clabel,xlim,ylim,grid,addaxes,origin,include.origin,sub,csub,possub,cgrid,pixmap,contour,area`: arguments passed to `s.class`; see `?s.class` for more informations
- `only.grp`: a `character` vector indicating which groups should be displayed. Values should match values of `x$grp`. If `NULL`, all results are displayed
- `subset`: `integer` or `logical` vector indicating which individuals should be displayed. If `NULL`, all results are displayed
- `new.pred`: an optional list, as returned by the `predict` method for `dapc` objects; if provided, the individuals with unknown groups are added at the bottom of the plot. To visualize these individuals only, specify `only.grp="unknown"`.
- `cex.lab`: a `numeric` indicating the size of labels.
- `txt.leg`: a character vector indicating the text to be used in the legend; if not provided, group names stored in `x$grp` are used.
- `label.inds`: Named list of arguments passed to the `orditorp` function. This will label individual points witout overlapping. Arguments `x` and `display` are hardcoded and should not be specified by user.
- ``: further arguments to be passed to other functions. For `scatter`, arguments passed to `points`; for `compoplot`, arguments passed to `barplot`.

## Details

See the documentation of `dapc` for more information about the method.

## Returns

All functions return the matched call.

## References

Jombart T, Devillard S and Balloux F (2010) Discriminant analysis of principal components: a new method for the analysis of genetically structured populations. BMC Genetics11:94. doi:10.1186/1471-2156-11-94

## See Also

- `dapc`: implements the DAPC.

- `find.clusters`: to identify clusters without prior.

- `dapcIllus`: a set of simulated data illustrating the DAPC

- `eHGDP`, `H3N2`: empirical datasets illustrating DAPC

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

data(H3N2)
dapc1 <- dapc(H3N2, pop=H3N2$other$epid, n.pca=30,n.da=6)

## defautl plot ##
scatter(dapc1)

## label individuals at the periphery
# air = 2 is a measure of how much space each label needs
# pch = NA suppresses plotting of points
scatter(dapc1, label.inds = list(air = 2, pch = NA))

## showing different scatter options ##
## remove internal segments and ellipses, different pch, add MStree
scatter(dapc1, pch=18:23, cstar=0, mstree=TRUE, lwd=2, lty=2, posi.da="topleft")

## only ellipse, custom labels, use insets
scatter(dapc1, cell=2, pch="", cstar=0, posi.pca="topleft", posi.da="topleft", scree.pca=TRUE,
inset.pca=c(.01,.3), label=paste("year\n",2001:2006), axesel=FALSE, col=terrain.colors(10))

## without ellipses, use legend for groups
scatter(dapc1, cell=0, cstar=0, scree.da=FALSE, clab=0, cex=3,
solid=.4, bg="white", leg=TRUE, posi.leg="topleft")

## only one axis
scatter(dapc1,1,1,scree.da=FALSE, legend=TRUE, solid=.4,bg="white")



## example using genlight objects ##
## simulate data
x <- glSim(50,4e3-50, 50, ploidy=2)
x
plot(x)

## perform DAPC
dapc2 <- dapc(x, n.pca=10, n.da=1)
dapc2

## plot results
scatter(dapc2, scree.da=FALSE, leg=TRUE, txt.leg=paste("group",
c('A','B')), col=c("red","blue"))

## SNP contributions
loadingplot(dapc2$var.contr)
loadingplot(tail(dapc2$var.contr, 100), main="Loading plot - last 100 SNPs")



## assignplot / compoplot ##
assignplot(dapc1, only.grp=2006)

data(microbov)
dapc3 <- dapc(microbov, n.pca=20, n.da=15)
compoplot(dapc3, lab="")
## End(Not run)
```



