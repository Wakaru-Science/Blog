---
layout: post
date: 2020-05-26
comments: true
title: Testing Post
usemathjax: true
---

Hello World
This is my first post

a given wire happens to be carrying "$$\lvert 0\rangle$$."
By that we mean that it's carrying the linear combination

katex.render("c = \\pm\\sqrt{a^2 + b^2}", element, {
    throwOnError: false
});

var html = katex.renderToString("c = \\pm\\sqrt{a^2 + b^2}", {
    throwOnError: false
});
// '<span class="katex">...</span>'

\\( a^2 + b^2 = c^2 \\)
\( a^2 + b^2 = c^2 \)

\\[ a^2 + b^2 = c^2 \\]

$\lvert$

$$\begin{psmallmatrix} 1 \\ 0 \end{psmallmatrix}$$

\( \psi \)
\( $\psi$ \)
\$ \psi \$
\$$ \psi \$$
\[  \]

\psi

\\( 1/x^{2} \\)

\\[ \frac{1}{n^{2}} \\]


\$$
\begin{align}
  \nabla\times\vec{\mathbf{B}}-\frac{1}{c}\frac{\partial\vec{\mathbf{E}}}{\partial t} &= \frac{4\pi}{c}\vec{\mathbf{j}} \\
  \nabla\cdot\vec{\mathbf{E}} &= 4\pi\rho \\
  \nabla\times\vec{\mathbf{E}}+\frac{1}{c}\frac{\partial\vec{\mathbf{B}}}{\partial t} &= \vec{\mathbf{0}} \\
  \nabla\cdot\vec{\mathbf{B}} &= 0
\end{align}
\$$

$$
\begin{align}
  \nabla\times\vec{\mathbf{B}}-\frac{1}{c}\frac{\partial\vec{\mathbf{E}}}{\partial t} &= \frac{4\pi}{c}\vec{\mathbf{j}} \\
  \nabla\cdot\vec{\mathbf{E}} &= 4\pi\rho \\
  \nabla\times\vec{\mathbf{E}}+\frac{1}{c}\frac{\partial\vec{\mathbf{B}}}{\partial t} &= \vec{\mathbf{0}} \\
  \nabla\cdot\vec{\mathbf{B}} &= 0
\end{align}
$$


$$mean = \frac{\displaystyle\sum_{i=1}^{n} x_{i}}{n}$$

k_{n+1} = n^2 + k_n^2 - k_{n-1}