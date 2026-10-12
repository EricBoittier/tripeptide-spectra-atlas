import csv, hashlib, json, math
from pathlib import Path
root=Path(__file__).resolve().parents[1]/"docs"
rows=json.loads((root/"catalog.json").read_text())
for r in rows:
 p=root/r["path"]
 assert hashlib.sha256(p.read_bytes()).hexdigest()==r["sha256"], p
 with p.open() as f:
  reader=csv.reader(f); assert next(reader)==["wavenumber_cm-1","intensity_rel"]
  pts=[tuple(map(float,x)) for x in reader]
 assert all(math.isfinite(x) and math.isfinite(y) for x,y in pts), p
 assert all(a[0]<b[0] for a,b in zip(pts,pts[1:])), p
 assert abs(max(abs(y) for x,y in pts)-1)<1e-5, p
print(f"Verified {len(rows)} spectra: checksums, headers, finite values, ascending frequencies, normalization.")
