#!/usr/bin/env python3
"""Regenerate src/data.js from the tables in data/. Needs numpy. Run from anywhere."""
import numpy as np, json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
D = lambda f: os.path.join(ROOT, 'data', f)
def load(fn):
    return np.array([[float(v) for v in l.split(',')] for l in open(D(fn)).read().split('\n') if l.strip()])
W = np.arange(380, 781, 5)
def fmt(a, nd=6):
    return [float(f"{x:.{nd}g}") for x in np.asarray(a, float).ravel()]
cmf31, cmf64, alpha, tcs, d65, ds, vp = (load(f) for f in ('cmf31.csv', 'cmf64.csv', 'alpha.csv', 'tcs.csv', 'd65.csv', 'dseries.csv', 'vprime.csv'))
for t in (cmf31, cmf64, alpha, tcs, d65, vp): assert (t[:, 0] == W).all()
ces = np.load(D('ces99.npy'))               # 60 x 99, 380..675 nm
full = np.vstack([ces] + [ces[-1:]] * 21)   # 680..780 nm held at the 675 nm value (data not available)
assert full.shape == (81, 99)
data = {'wl0': 380, 'step': 5, 'n': 81,
 'x31': fmt(cmf31[:, 1]), 'y31': fmt(cmf31[:, 2]), 'z31': fmt(cmf31[:, 3]),
 'x64': fmt(cmf64[:, 1]), 'y64': fmt(cmf64[:, 2]), 'z64': fmt(cmf64[:, 3]), 'vp': fmt(vp[:, 1]),
 'aS': fmt(alpha[:, 1]), 'aM': fmt(alpha[:, 2]), 'aL': fmt(alpha[:, 3]), 'aR': fmt(alpha[:, 4]), 'aMel': fmt(alpha[:, 5]),
 'd65': fmt(d65[:, 1]), 'ds0': fmt(ds[:, 1]), 'ds1': fmt(ds[:, 2]), 'ds2': fmt(ds[:, 3]), 'ds_wl0': 380, 'ds_step': 10,
 'tcs': [fmt(tcs[:, 1 + k], 4) for k in range(14)], 'ces': [fmt(full[:, k], 5) for k in range(99)]}
hdr = open(os.path.join(ROOT, 'src', 'data.js'), encoding='utf-8').readline() if os.path.exists(os.path.join(ROOT, 'src', 'data.js')) else ''
open(os.path.join(ROOT, 'src', 'data.js'), 'w').write(hdr + 'var LSL_DATA=' + json.dumps(data, separators=(',', ':')) + ';\n')
print('wrote src/data.js')
