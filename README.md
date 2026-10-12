# Tripeptide Spectra Atlas

Site: https://EricBoittier.github.io/tripeptide-spectra-atlas/

70 digitized profiles with individual CSVs, metadata, source overlays, and remote comparison instructions. All extractions await user validation. Five Pohl profiles are published calculated totals, not experiments. EFieldPhysNet ML/MM predictions for 65 profiles (run `efieldphysnet_mlmm_20261012`, generated 2026-10-12) are under `docs/results/` with overlays, metrics and provenance on [results.html](https://EricBoittier.github.io/tripeptide-spectra-atlas/results.html); the gas-phase tripeptide library snapshot is under `docs/library/`. No paper-model reconstruction has been produced yet.

Static GitHub Pages site is served from `docs/` on `main`. No build step or dependencies are required. Serve locally with `python3 -m http.server 8000 --directory docs`.

See [remote handoff](docs/REMOTE_HANDOFF.md) for run requirements. Source figures remain attributed to their publishers; no blanket license is asserted over third-party figures or data. Full articles and signed access URLs are not redistributed.
