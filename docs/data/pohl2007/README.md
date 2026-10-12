# Pohl et al. (2007): digitized spectra through Figure 7

Source: DOI 10.1039/B705098D, Phys. Chem. Chem. Phys. 9, 4698–4708.

25 main traces: Figures 2, 3, 5, 6 and 7, panels a–e. Figures 1 and 4 are molecular structures. Panels a/b/c/d are DCM solution, DMSO solution, Kr matrix and Ar matrix; e is the calculated total. The individual dashed/dotted/thin-solid conformer component curves in panel e are NOT separately digitized.

Figures 2/3: Ac-Gly-NHMe IR, amide I/II and amide A respectively.
Figures 5/6: Ac-L-Ala-NHMe IR, amide I/II and amide A respectively.
Figure 7: Ac-L-Ala-NHMe VCD, amide I/II. Its caption incorrectly labels the region amide A; the wavenumber axis and main text establish amide I/II.

## Units and processing

Each CSV has wavenumber_cm-1 and intensity_rel. Wavenumber is ascending. Calibration is a linear least-squares fit to printed ticks, recorded in manifest.json. Native embedded bitmap resolution was used, with one sample per image column (approximately 0.19 cm-1 for amide I/II IR, 0.20 for VCD, 0.26 for amide A). This sampling is not experimental resolution or a claim of corresponding frequency accuracy.

IR: subtract the minimum observed intensity (maximum vertical image coordinate), then normalize the maximum to 1. This removes display offsets but is not a solvent/background correction. It does not establish a physical absorbance zero.
VCD: use the printed delta-A=0 reference and divide by the largest absolute excursion, retaining signs. Each trace is independently normalized; absolute intensities and intensity ratios across panels cannot be recovered.

Curves were traced from native image pixels, excluding axes, panel letters and isolated annotation symbols. Real water/aggregate bands remain. Short gaps caused by reference-line masking were linearly interpolated. The number of interpolated columns and actual extracted bounds are in manifest.json. Near-zero portions coincident with the reference line have limited precision. No extrapolation beyond recovered trace endpoints was applied; Figure 7a ends before the right plot border and Figure 6b loses a short flat segment obscured by the panel border. Calculated VCD total extraction is less certain where component strokes overlap.

## Validation

Open review.html to toggle the red extraction over each source figure. Individual normalized plots and overlays are in validation/. All files remain pending user validation. Visual inspection confirmed alignment of main bands; no quantitative error bars are inferred. No smoothing, theoretical reconstruction of peaks, or spectral fitting was applied.

Reproduce with digitize.py (Python, pymupdf for image extraction, numpy, scipy, Pillow, matplotlib). The source PDF and original embedded images are retained. The CSVs are digitizations of published graphical data, not original instrument data.
