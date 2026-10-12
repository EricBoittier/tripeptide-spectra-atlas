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

# stored model predictions: same CSV contract, entries resolvable against the catalog
ids={r["id"] for r in rows}
for runjson in sorted((root/"results").glob("*/run.json")):
 run=json.loads(runjson.read_text()); n=0
 for e in run["entries"]:
  assert e["reference_id"] in ids and e["method"] in ("paper_model","efieldphysnet"), e["reference_id"]
  for f in e["files"].values():
   p=runjson.parent/f
   with p.open() as fh:
    reader=csv.reader(fh); assert next(reader)==["wavenumber_cm-1","intensity_rel"], p
    pts=[tuple(map(float,x)) for x in reader]
   assert all(math.isfinite(x) and math.isfinite(y) for x,y in pts) and all(a[0]<b[0] for a,b in zip(pts,pts[1:])), p
   assert abs(max(abs(y) for x,y in pts)-1)<1e-5, p; n+=1
 print(f"Verified {n} prediction CSVs in {runjson.parent.name} ({len(run['entries'])} entries).")
