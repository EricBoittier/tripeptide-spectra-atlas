# Eker et al. 2002 — digitized spectra

DOI: 10.1021/ja027381w. Tripeptides Adopt Stable Structures in Water. JACS 124, 14330–14341.

45 main profiles from Figures 1, 3, 5, 6, 9, 10, 11, 13, 14 and 16. Source publisher figure images are retained at full resolution. Source captions and URLs: figure_sources.json. Table 1 is transcribed directly from publisher HTML to table1_published_parameters.csv; footnote markers remain in the cells. Read the footnotes in article.txt before interpreting widths or ambiguous entries.

Coverage:
- Fig 1: zwitterionic AAA and L-Ala-D-Ala-L-Ala (A_DA_A), IR/isotropic Raman/anisotropic Raman in D2O, six traces.
- Fig 3: AAA, cationic/zwitterionic/anionic, VCD and IR in D2O, six traces.
- Fig 5: VVV, anionic left and cationic right, IR/isotropic Raman/anisotropic Raman, six traces. The caption mentions all three states; main text explicitly says the zwitterionic spectra are not shown. H2O/D2O panel assignment is not explicit, so solvent is flagged unspecified.
- Fig 6: VVV, three protonation states, VCD and IR in D2O, six traces.
- Fig 9: cationic VVV isotropic Raman in H2O, one trace. AAA is only a peak-position annotation.
- Fig 10: anionic SSS, IR/isotropic Raman/anisotropic Raman/VCD in D2O, four traces.
- Fig 11: SSS, cationic/anionic, VCD and IR in D2O, four traces. Caption erroneously says VVV; surrounding Triserine discussion explicitly identifies SSS.
- Fig 13: KKK at acid pD 1 and neutral pD 7, IR/isotropic Raman/anisotropic Raman, six traces.
- Fig 14: KKK, printed acidic/neutral labels, VCD and IR in D2O, four traces. Text says measurements at pD 1 and 2, inconsistent with the neutral label and surrounding discussion; exact pD remains unresolved. Do not infer net-neutral lysine from the word neutral.
- Fig 16: KKK and AAA, acidic aqueous isotropic Raman, two traces.

Figures 2, 8, 12 and 17 are structures. Figures 4, 7 and 15 are amide-I model comparisons using experimental profiles already represented in the broader spectra; retained as reference images, not counted as new spectra. Thin fitted components and theoretical alternatives are not digitized. Where experimental markers overlap a total fitted line, the extraction represents the visible main profile and cannot reliably distinguish them.

## Units and extraction

Spectrum CSVs have two columns: wavenumber_cm-1,intensity_rel. Frequencies are ascending. Native image columns are calibrated linearly against axis ticks. Many images are enlarged low-resolution originals: fine CSV spacing does NOT establish corresponding experimental resolution or accuracy.

Each trace is independently normalized to max(abs(intensity)) = 1. Isolated IR/Raman panels use the plotted zero tick; vertically stacked IR uses minimum observed intensity to remove display offsets. VCD retains sign relative to an approximate trace-specific zero, using off-resonance reference plateaus for vertically offset spectra and plotted zero for Figure 10. VCD baseline uncertainty can affect weak signals close to zero. Absolute intensities and cross-spectrum intensity ratios are not retained. No physical baseline fit, solvent correction or amplitude calibration is claimed.

Traces are derived from source pixels, guided by manually placed corridors. Color separates red/black measurements. Text, axes and vertical assignment lines are masked; gaps are linearly interpolated only inside recovered bounds. A local median rejects isolated large pixel outliers; it is not a spectral smooth or peak fit. Some noisy point plots retain uncertainty between markers, total-fit strokes and scatter. Configurations and extraction code are included for inspection. Manifest records calibration, offset, scale, interpolation counts and identity notes. All spectra remain pending user validation.

## Review

Open review.html and toggle the extraction overlay. Orange corresponds to black source curves; blue corresponds to red source curves. Review especially Fig 5 solvent metadata, Fig 14 pD metadata and noisy Raman traces. Paper table values are direct transcription rather than fitted to these digitizations.
