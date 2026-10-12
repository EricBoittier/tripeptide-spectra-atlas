from pathlib import Path
import json, csv
import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import label
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).parent
(P/'csv').mkdir(exist_ok=True);(P/'validation').mkdir(exist_ok=True)
configs={
2:dict(file='page4_img0.png',edges=[1,426,850,1275,1699,2123],left=75,ticks=[287,552,816,1081,1346],vals=[1700,1650,1600,1550,1500]),
3:dict(file='page5_img0.png',edges=[1,430,858,1286,1714,2142],left=73,ticks=[169.5,558,947,1337],vals=[3500,3400,3300,3200]),
5:dict(file='page7_img0.png',edges=[1,430,857,1284,1711,2139],left=76,ticks=[286,551,816,1081,1346.5],vals=[1700,1650,1600,1550,1500]),
6:dict(file='page8_img0.png',edges=[1,423,845,1266,1686,2107],left=88,ticks=[181.5,566.5,953,1338.5],vals=[3500,3400,3300,3200]),
7:dict(file='page9_img1.png',edges=[2,454,907,1360,1813,2265],left=125,ticks=[328,584,840.5,1095.5,1351.5],vals=[1700,1650,1600,1550,1500],zeros=[156.5,642,1057.5,1587,1998])}
rows=[]
for fig,c in configs.items():
 a=np.array(Image.open(P/c['file']).convert('L')); ink=a>128
 overlay=Image.fromarray(255-a).convert('RGB');draw=ImageDraw.Draw(overlay)
 coeff=np.polyfit(c['ticks'],c['vals'],1)
 plots,axs=plt.subplots(5,1,figsize=(9,10),sharex=True,layout='constrained')
 for i,panel in enumerate('abcde'):
  top,bot=c['edges'][i:i+2];left=c['left'];right=1529
  mask=ink.copy();mask[:top+7]=False;mask[bot-7:]=False;mask[:,:left+5]=False;mask[:,right-4:]=False
  # Panel letter and annotation symbols are disconnected from the spectrum.
  mask[top:top+105,left:left+105]=False
  if fig==7:
   zero=c['zeros'][i]
   # Detect thin horizontal zero reference, excluding the spectral stroke.
   if i==4:
    sums=ink[top+30:bot-30,left+10:right-10].sum(1)
    zero=top+30+int(np.argmax(sums))
   mask[int(zero)-2:int(zero)+3]=False
   labs,n=label(mask)
   keep=[]
   for j in range(1,n+1):
    yy,xx=np.where(labs==j)
    if len(xx)>18 and xx.max()-xx.min()>5:keep.append(j)
   mask=np.isin(labs,keep)
  else:
   labs,n=label(mask)
   sizes=np.bincount(labs.ravel());sizes[0]=0
   mask=labs==np.argmax(sizes)
  xs=np.arange(left+6,right-4);ys=np.full(len(xs),np.nan)
  for k,x in enumerate(xs):
   candidates=np.where(mask[:,x])[0]
   if len(candidates):
    if fig==7:
     # Total curve is the outer solid trace; thin conformer components lie inward.
     groups=np.split(candidates,np.where(np.diff(candidates)>1)[0]+1)
     group=max(groups,key=lambda g:abs(np.median(g)-zero))
     ys[k]=np.median(group)
    else:ys[k]=np.median(candidates)
  valid=np.isfinite(ys)
  # Never extrapolate a curve beyond its printed endpoints.
  first,last=np.where(valid)[0][[0,-1]];xs=xs[first:last+1];ys=ys[first:last+1];valid=np.isfinite(ys)
  gaps=int((~valid).sum());ys=np.interp(xs,xs[valid],ys[valid])
  baseline=float(zero if fig==7 else np.max(ys))
  intensity=baseline-ys;scale=float(np.max(np.abs(intensity)));intensity/=scale
  wn=np.polyval(coeff,xs);order=np.argsort(wn)
  molecule='Ac-Gly-NHMe' if fig in (2,3) else 'Ac-L-Ala-NHMe'
  kind='vcd' if fig==7 else 'ir';env=['dcm','dmso','kr_matrix','ar_matrix','dft_total'][i]
  name=f'pohl2007_fig{fig}{panel}_{kind}_{env}.csv'
  np.savetxt(P/'csv'/name,np.column_stack([wn[order],intensity[order]]),delimiter=',',header='wavenumber_cm-1,intensity_rel',comments='',fmt='%.7f')
  draw.line(list(zip(xs.tolist(),ys.tolist())),fill=(225,55,35),width=2)
  axs[i].plot(wn,intensity,color='#156b85',lw=1);axs[i].axhline(0,color='0.7',lw=.6)
  axs[i].set_ylabel('Rel. intensity');axs[i].set_title(f'{panel} · {env.replace("_"," ")}',loc='left',fontsize=10)
  rows.append(dict(file=name,figure=fig,panel=panel,molecule=molecule,observable=kind,environment=env,source_page={2:4,3:5,5:7,6:8,7:9}[fig],baseline_pixel=baseline,scale_pixels=scale,pixel_to_wavenumber=coeff.tolist(),range_cm1=[float(wn.min()),float(wn.max())],interpolated_columns=gaps,points=len(xs),status='pending user validation'))
 axs[-1].set_xlabel('Wavenumber (cm⁻¹)');axs[-1].invert_xaxis();plots.suptitle(f'Figure {fig} · {molecule} · {kind.upper()}')
 plots.savefig(P/'validation'/f'fig{fig}_digitized.png',dpi=150);plt.close(plots)
 overlay.save(P/'validation'/f'fig{fig}_overlay.png')
(P/'manifest.json').write_text(json.dumps(rows,indent=2))
print('Extracted',len(rows),'traces')
for r in rows: print(r['file'],r['points'],r['interpolated_columns'],r['baseline_pixel'])
