# Band gap calculation
This tool is used to automate band gap determination. It allows to make a fully automated band gap energy analysis
for thin-film libraries.

<p align="center">
    <a href="https://ruhr-uni-bochum.sciebo.de/s/DDnRoGzBRAAhWYg" target="_blank">
        <img align="center" alt="download" src="https://www.screentogif.com/wiki/download-now.png"/>
    </a>
</p>

## Overview
The method used in this tool is simple, fast, robust to preprocessing errors and unifies the problems of curvature evaluation, curve decomposition and Tauc segmentation extraction. The main idea is to decompose the given curve by breakpoints and select the fragment 
which contains the most linear feature that could represent Tauc segment. The breakpoints are divided into cusps and inflection points by 
testing their significant changes in curvature using adaptive smoothing techniques. Applying this method to experimental data indicated 
that it could handle all kinds of thin-film library data without prior knowledge.

## Basic algorithm
The detailed algorithm used in this tool could be found in [documentation](/assets/algorithm_bandgap.pdf). Below is just a short description of this method:


Figure 1 shows a typical analytic procedure. Firstly, the absorbance data from a thin-film sample is collected, which covers a range of energies from below the band gap transition to above it. Then based on Beer-Lambert’s law `(α ∝ Ln(I/I0))`, the absorption coefficient α is calculated. Finally, the band gap energy could be derived from the equation `(α·hv)1/n = B(hv - Eg)`, where hν is the photon energy and B is a constant. The n factor depends on the nature of the electron transition. For direct allowed band gap energy, `n = ½`, and indirect allowed band gap, `n = 2`. In either case, the linear region of the plot is extrapolated, and the interception with the x-axis corresponds to the estimated band gap value. The initial breakpoints between decomposed fragments are defined as either cusps or inflection points. Cusps and inflection points, which are mathematically simple, are the most significant features for straight-line segment identification. A cusp stands for a 
point between two consecutive convex or concave, whereas an inflection point is a point where the curve changes from being convex to concave or vice versa. Their detection is related to local curvature characteristics such as extremes or stationary point, and several examples are shown in Figure 2. For example, the local minimum curvature happens when the inflection point preceded by a convex and followed by a concave means, while local maximum occurs when an inflection point experiences the reverse way. 

![1](/assets/overview1.png)

Figure 1. Tauc method allows to determinate the band gap energy (Eg) from absorption spectrum. UV-VIS spectrum and Tauc plots for band gap determination. 



![2](/assets/overview2.png)

Figure 2. Possible types of cusps and inflection points for curve decomposition. A cusp stands for a point between two consecutive convex or concave, whereas an inflection point is a point where the curve changes from being convex to concave or vice versa.

## Python dependen
