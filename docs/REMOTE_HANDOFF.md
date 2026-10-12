# Remote model comparison handoff

## Get the data

```bash
git clone https://github.com/EricBoittier/tripeptide-spectra-atlas.git
cd tripeptide-spectra-atlas
python3 tools/verify_data.py
```

Alternatively download `spectra-data.zip` from the site. Spectrum CSV columns are `wavenumber_cm-1,intensity_rel`; frequencies ascend. Metadata and checksums are in `catalog.json`. Each spectrum is normalized independently. VCD sign is retained; offsets and baseline estimates are documented in each study's README. Fine pixel spacing is not experimental resolution. Use the DOI to inspect original methods and table footnotes.

## Requested comparison

Compare (1) digitized published profiles, (2) reconstruction with the paper's fitted bands / two-oscillator equations, and (3) predictions from the most recent appropriate EFieldPhysNet checkpoint available on dw. The checkpoint path, exact revision, and supported observables must be verified on dw; no command or checkpoint selection is assumed here.

- Pohl 2007: capped Ac-Gly-NHMe and Ac-Ala-NHMe, with solution, matrix, and published DFT profiles. These are not Ac-X-X-X-NHMe tripeptides. Keep environments distinct.
- Eker 2002: uncapped AAA, L-Ala-D-Ala-L-Ala, VVV, SSS, KKK with documented charge states, solvents, and spectroscopy. Match terminal chemistry and side-chain charge. Do not interpret neutral pD as net-neutral KKK.
- Schweitzer-Stenner 2001 (DOI 10.1021/ja016202s): requested next additions are Figure 1 trialanine spectra, Figure 4 triglycine spectra, and Figure 2 coupling/dipole-angle maps versus phi/psi. These are NOT digitized or reconstructed in this release. Figure 3 is a structure.

## Paper-model reconstruction

Eker Table 1 transcription is included in `data/eker2002/table1_published_parameters.csv`; retain superscript footnotes and verify their meanings against the article. Use reported frequencies, line-width definitions, and intensity ratios. Report assumptions where the paper does not fully specify line shapes. Do not present a fit to extracted curves as an independent prediction. Check the later correction to the two-oscillator mixing/coupling relation before applying the 2001 equations. Report contour-map method and transition-dipole geometry separately.

## EFieldPhysNet run requirements

Record checkpoint filename and SHA256, training/model variant, code commit, exact command, environment, charge, isotope substitutions, solvent treatment, conformers and weights, geometry optimization, frequency scaling, and broadening. A neutral checkpoint is not automatically applicable to the ionic experiments. D2O requires an explicit exchange/isotopologue convention. IR needs dipole response; Raman needs polarizability response; VCD needs appropriate chiroptical response. Do not infer unsupported observables from an energy-only model. Mark unavailable observables explicitly.

Export each broadened prediction as `wavenumber_cm-1,intensity_rel` with ascending frequencies. Retain raw frequencies/intensities separately. Use signed max-absolute normalization for VCD and a documented baseline for IR/Raman. The site's local comparison upload overlays an already-normalized prediction and does not shift or renormalize it silently.

## Return results

Create `results/<run-id>/` in a branch, with prediction CSVs, raw outputs, and a `run.json` recording the above provenance plus `reference_id` (the selected CSV stem), `method` (`paper_model` or `efieldphysnet`), and any limitations. Submit a pull request. Do not commit model checkpoints. The site can overlay a local result CSV immediately without uploading it to a server.

## Validation still needed

All extracted profiles await Eric's visual validation. In Eker Fig 5 solvent-to-panel assignment is unresolved; Fig 14 has conflicting pD descriptions. Experimental markers and fitted total lines sometimes overlap. Pohl individual theoretical components were not separately extracted. Inspect the study review pages before treating curves as benchmark ground truth.
