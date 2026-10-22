// Smoke test of the calculation core: node tests/smoke.js
const fs = require('fs'), vm = require('vm'), path = require('path');
const ctx = { console }; ctx.globalThis = ctx; vm.createContext(ctx);
for (const f of ['data.js', 'core.js']) vm.runInContext(fs.readFileSync(path.join(__dirname, '..', 'src', f), 'utf8'), ctx);
const L = ctx.LSL; let fail = 0;
function chk(name, got, want, tol) { const ok = Math.abs(got - want) <= tol; if (!ok) fail++; console.log((ok ? 'ok   ' : 'FAIL ') + name + ': ' + got.toFixed(4) + ' (expected ' + want + ' +/- ' + tol + ')'); }
const d65 = L.analyse(L.d65spd()), A = L.analyse(L.illumA()), bb = L.analyse(L.planck(3000));
chk('D65 CCT', d65.cct, 6504, 15); chk('D65 x', d65.xy.x, 0.3127, 0.0005); chk('D65 y', d65.xy.y, 0.3290, 0.0005);
chk('A x', A.xy.x, 0.4476, 0.0005); chk('A y', A.xy.y, 0.4074, 0.0005); chk('A CCT', A.cct, 2856, 5);
chk('D65 melanopic DER', d65.alpha.Mel.DER, 1, 1e-9); chk('D65 Ra', d65.cri.Ra, 100, 0.01);
chk('BB3000 Rf', bb.tm30.Rf, 100, 0.01); chk('BB3000 Rg', bb.tm30.Rg, 100, 0.01); chk('BB3000 Duv', bb.duv, 0, 1e-4);
chk('Equal-energy LER-ish check: 555 nm Gaussian FWHM 5 => LER', L.analyse(L.scale(L.gaussian(555, 5, 0), 1e-3)).LER, 683, 8);
process.exit(fail ? 1 : 0);
