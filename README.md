# LED Spectrum Lab

Add, edit, mix and analyse LED spectra in the browser. One self-contained HTML file; no server, no external
dependencies, works offline from `file://`.

**Analysis:** CCT / Duv (exact nearest-point on the Planckian locus), CRI R1-R14, full TM-30 (Rf, Rg, Rf,skin, Rf,h, Rcs,h,
Rhs,h, colour vector graphic, 99 CES), zoomable CIE 1931 xy and 1976 u'v' diagram with Planckian locus, isotherms and
ANSI Duv bands, photopic / scotopic / 10° quantities, LER and radiant power per lumen, wall-plug efficiency and lm/W,
PPF / ePAR and band splits, CIE S 026 alpha-opic quantities (melanopic, S, M, L, rhodopic) with DER and EDI.

**LEDs:** an editable library (stored in the browser), an editor that builds a monochromatic LED from a peak wavelength
(Gaussian with typical width and asymmetry) or a phosphor-converted white from a target CCT, mixing of channels with
current scaling, and import / export as JSON (`led-spectrum-lab` format), CSV (hcri.io style), Argyll `.sp`, or share links.
PDF / CSV report export.

## Use

* Open `docs/index.html` (or `dist/led-spectrum-lab.html` after building) in a browser. With GitHub Pages
  (Settings -> Pages -> branch `main`, folder `/docs`) it is served directly.

## Build

```sh
python3 build.py                              # -> dist/led-spectrum-lab.html and docs/index.html
LSL_REPO_URL=https://github.com/you/repo python3 build.py   # sets the source link shown in the app (required by AGPL §13 courtesy)
python3 tools/gendata.py                      # optional: regenerate src/data.js from data/ (needs numpy)
node tests/smoke.js                           # sanity checks of the colorimetry core
```

Source layout: `src/core.js` (colorimetry / CRI / TM-30 / generators, no DOM), `src/ui1.js` (state, library, file formats),
`src/ui2.js` (chart engines), `src/ui3.js` (library, editor, mix panels), `src/ui4.js` (analysis tabs, PDF, wiring).

## Limits

Results are engineering estimates; verify against calibrated instruments or certified software before certification.
LED flux is modelled as linear in current (no droop or thermal effects). See `NOTICE.md` for data provenance.

## License

Copyright (C) 2026 the LED Spectrum Lab authors. Licensed under the **GNU Affero General Public License v3.0 or later**
(`AGPL-3.0-or-later`). If you run a modified version as a network service, you must offer its users the corresponding
source. Replace the placeholder `LICENSE` with the official text before publishing (`sh tools/get-license.sh`).
Reference data tables keep their owners' terms (see `NOTICE.md`).
