# Contact matrix heatmap

```r
plot_contact_matrix(x)
```

## Arguments

- `x`: data.frame; a contact matrix. See contact_matrix .

## Returns

A ggplot object that can be further customized using the `ggplot2` package.

## Description

Contact matrix heatmap

## Examples

```r
# Import the projected contact matrix for Greece:
conmat <- contact_matrix(country = "GRC")

plot_contact_matrix(conmat)
```



