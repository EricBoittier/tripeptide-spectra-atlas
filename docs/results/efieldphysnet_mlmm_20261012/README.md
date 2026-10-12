# EFieldPhysNet ML/MM predictions (efieldphysnet_mlmm_20261012)

Peptides of Eker et al. 2002 (D2O, measured charge states, counter-ions) and Pohl et al. 2007 (CH2Cl2, DMSO, Ar, Kr matrices),
minimised with EFieldPhysNet rw_neutral (peptide, float64) + CHARMM36 (solvent/ions, mechanical embedding), harmonic IR /
isotropic + anisotropic Raman / VCD from the model's dipole, polarizability and charges-only atomic axial tensors.
65 reference traces, 44 conformer minima. See run.json for provenance, metrics and limitations.

- predictions/<reference_id>__efieldphysnet_unscaled.csv and ..._scaled<f>.csv: `wavenumber_cm-1,intensity_rel` on the trace's grid
- overlays/<reference_id>.png: digitised trace vs prediction
- raw/<system>_<conformer>.json: stick spectra (H and D), minimised geometry, model charges, dipole, polarizability
- metrics.json: correlation and scale per reference; per-conformer correlations
