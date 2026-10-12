# Capped tripeptide harmonic library (EFieldPhysNet rw_neutral, gas phase)

Snapshot of 2026-10-12 20:48: 7969 sequences (99.6 % of the 8,000), 23907 L minima plus mirror images (47814 structures), 237 shards processed; one shard (31 sequences) was still queued when this snapshot was taken.

- `summary_20261012b.csv.gz`: one row per minimised structure. Columns: shard, seq, conf, chirality, x1, x2, x3, n_atoms, energy, energy_rel, zpe, fmax, opt_steps, converged, n_imag, n_imag_first, retried, min_freq, phi2, psi2, basin2, duplicate_of, boltzmann_w, dipole, alpha_iso, ir_max, raman_max, vcd_absmax, vcd_absmax_800_1800, g_absmax_800_1800, cov_dE, charged.
  Energies in eV (energy_rel relative to the sequence minimum), fmax in eV/Å, frequencies in cm⁻¹, dipole in e·Å, alpha_iso in Å³, IR km/mol, Raman Å⁴/amu, VCD 10⁻⁴⁴ esu² cm²; boltzmann_w at 300 K within a sequence; cov_dE is the |E(L) − E(D)| mirror-covariance check in eV.
- `summary.json`: counts, convergence statistics, basin populations, L/D covariance maxima, GPU time.
- `overview.json`: basin populations by residue and position and amide VCD statistics.
- `fig_*_20261012b.png`: overview figures used on results.html.
- `trialanine_zw_20261012.json` / `.png`: zwitterionic trialanine (uncapped, gas phase) harmonic amide modes for PPII, β and αR starts, H and D isotopologues.

The stick spectra of every structure (not only the summary) are kept on sciCORE (lib/ and lib256/ shards) and can be added on request; they are about 2 GB.
