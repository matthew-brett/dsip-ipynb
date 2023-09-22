---
jupyter:
  jupytext:
    notebook_metadata_filter: all,-language_info
    split_at_heading: true
    text_representation:
      extension: .Rmd
      format_name: rmarkdown
      format_version: '1.2'
      jupytext_version: 1.13.7
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Some algebra with summation

We use the symbol $\Sigma$ for
[summation](https://en.wikipedia.org/wiki/Summation).

Say we have a series of four values $x_1, x_2, x_3, x_4$.

We can write the sum $x_1 + x_2 + x_3 + x_4$ as:

$$\Sigma_{i=1}^{4} x_i$$

You can read this summation as "the sum of values $x$ subscript
$i$ from $i=1$ through $i=4$".

So:

$$
\Sigma_{i=1}^{4} x_i = x_1 + x_2 + x_3 + x_4
$$

When the indices of the summation are obvious, they may quietly
disappear. For example, it may be obvious that we are summing
over all $i = 1, 2, 3, 4$, in which case we could write the
$Sigma$ with or without the indices:

$$\Sigma_{i=1}^{4} x_i = \Sigma x_i$$

## Algebra of sums

### Addition inside sum

Say we have two series of numbers $x_1, x_2 cdots x_n$ and $y_1,
y_2 cdots y_n$.

$$\begin{aligned}
\Sigma_{i=1}^n (x_i + y_i) = \\
(x_1 + y_1) + (x_2 + y_2) + \cdots (x_n + y_n) = \\
(x_1 + x_2 + \cdots x_n) + (y_1 + y_2 + \cdots y_n) = \\
\Sigma_{i=1}^n x_i + \Sigma_{i=1}^n y_i
\end{aligned}$$

### Multiplying by constant inside sum

$$\begin{aligned}
\Sigma c x_i = \\
c x_1 + c x_2 + \cdots c x_n = \\
c (x_1 + x_2 + \cdots x_n) = \\
c \Sigma x_i
\end{aligned}$$

### Sum of constant value

$$
\Sigma_{i=1}^n c = n c
$$

## More reading

- [A basic tutorial on summation with
  tests](http://www.psychstat.missouristate.edu/IntroBook3/sbk10.htm);
- A list of [summation
  identities](https://en.wikipedia.org/wiki/Summation#Identities)
