# Returns original points in results paths of an object of class 'monmonier'

## Description

The original implementation of `monmonier` in package adegenet returns path coordinates, `coords.monmonier` additionally displays identities of the original points of the network, based on original coordinates.

```r
coords.monmonier(x)
```

## Arguments

- `x`: an object of class `monmonier`.

## Returns

Returns a list with elements according to the `x$nrun` result of the `monmonier` object. Corresponding path points are in the same order as in the original object.

run1 (run2, ...): for each run, a list containing a matrix giving the original points in the network (`first` and `second`, indicating pairs of neighbours). Path coordinates are stored in columns `x.hw` and `y.hw`. `first` and `second` are integers referring to the row numbers in the `x$xy` matrix of the original `monmonier` object.

## Author(s)

Peter Solymos, Solymos.Peter@aotk.szie.hu

## See Also

`monmonier`

## Examples

```r
## Not run:

if(require(spdep)){

load(system.file("files/mondata1.rda",package="adegenet"))
cn1 <- chooseCN(mondata1$xy,type=2,ask=FALSE)
mon1 <- monmonier(mondata1$xy,dist(mondata1$x1),cn1,threshold=2,nrun=3)

mon1$run1
mon1$run2
mon1$run3
path.coords <- coords.monmonier(mon1)
path.coords
}
## End(Not run)
```



