# Notice: third-party data and provenance

The program code is licensed under AGPL-3.0-or-later (see `LICENSE`). The numerical tables
in `data/` (compiled into `src/data.js`) are standard colorimetric reference data. They are
facts published by standards bodies and are **not** re-licensed under the AGPL; they remain
under their owners' terms. Before publishing, please check that your use matches those terms.

| Table | File | Source |
|---|---|---|
| CIE 1931 2° colour-matching functions | `data/cmf31.csv` | CIE (files.cie.co.at), 5 nm |
| CIE 1964 10° colour-matching functions | `data/cmf64.csv` | CIE / CVRL |
| Scotopic V'(λ) | `data/vprime.csv` | CIE |
| CIE S 026 alpha-opic action spectra (S, M, L, rhodopic, melanopic) | `data/alpha.csv` | CIE S 026/E:2018 |
| CIE standard illuminant D65 and D-series basis functions S0, S1, S2 | `data/d65.csv`, `data/dseries.csv` | CIE |
| CIE 13.3-1995 test colour samples TCS01-14 | `data/tcs.csv` | CIE 13.3-1995 |
| TM-30 colour evaluation samples (99 CES) | `data/ces/`, `data/ces99.npy` | ANSI/IES TM-30-20 / CIE 224:2017 |

Known data limits

* The CES reflectance values above 675 nm are not included in the source data and are held constant at the
  675 nm value up to 780 nm (`tools/gendata.py`). One value (480 nm for samples 52-61) was interpolated from its
  neighbours because the source row was unreadable. The effect on Rf and Rg is estimated to be far below 0.1 but
  has not been measured against a reference implementation.
* The example LEDs in the default library are synthetic (Gaussian / phosphor-band shapes), not measurements of real parts.

Algorithms follow the published methods (CIE 15, CIE 13.3-1995, CIECAM02 / CAM02-UCS, ANSI/IES TM-30-20, CIE S 026,
McCamy 1992) and were written from the specifications; no code from other tools was copied.
Spectrum file formats read and written: Argyll CMS `.sp` (SPECT) and simple wavelength/intensity CSV.
"Argyll CMS" and "hcri.io" are names of other projects and are not affiliated with this one.
