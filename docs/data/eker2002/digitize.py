from pathlib import Path
import numpy as np,json
from PIL import Image,ImageDraw
from scipy.ndimage import label
P=Path(__file__).parent
(P/'csv').mkdir(exist_ok=True);(P/'validation').mkdir(exist_ok=True)
configs=[]
def add(fig,name,box,cal,guide=None,method='guide',zero=None,color='black',masks=[],note=''):
 configs.append(dict(fig=fig,name=name,box=box,cal=cal,guide=guide,method=method,zero=zero,color=color,masks=masks,note=note))
# Coordinates are in review images; mapped to native source pixels at extraction.
for j,(l,r) in enumerate([(43,237),(315,508),(587,780)]):
 for color,mol in [('black','AAA'),('red','A_DA_A')]:
  masks=[(l+65,12,r-2,74)] if j else [(110,12,232,47),(116,52,147,76),(152,76,178,110)]
  add(1,f'{mol}_zwitterion_D2O_'+['ir','raman_iso','raman_aniso'][j],(l+2,14,r-2,280),[(l,1550),(r,1750)],method='envelope',zero=268 if j==0 else 278,color=color,masks=masks)
# Broad IR/VCD plots. Guides identify each printed spectrum, not spectral fits.
G={
3:[
[(115,103),(240,104),(271,92),(296,66),(310,82),(326,159),(335,133),(355,150),(375,180),(401,154),(421,112),(499,107),(524,94),(547,125),(592,103),(640,112),(691,130),(720,134),(738,104),(758,82),(774,22),(783,34),(790,118),(795,112)],
[(115,153),(241,154),(273,103),(289,153),(307,237),(321,214),(335,169),(348,179),(383,236),(403,198),(429,153),(472,156),(520,134),(549,171),(562,178),(586,157),(630,153),(651,166),(670,195),(688,189),(713,192),(731,132),(756,111),(775,63),(784,122),(792,151),(795,140)],
[(115,226),(200,215),(240,213),(270,186),(284,245),(303,439),(314,374),(326,296),(338,251),(370,235),(401,230),(491,230),(518,219),(547,232),(560,257),(576,235),(619,232),(635,247),(652,232),(678,265),(697,246),(737,226),(762,190),(775,190),(795,182)],
[(115,643),(220,639),(263,612),(290,529),(317,468),(334,509),(350,541),(377,469),(396,526),(412,587),(460,603),(488,584),(521,478),(550,480),(574,537),(593,559),(609,533),(628,590),(647,596),(670,585),(700,611),(736,622),(795,620)],
[(115,748),(224,746),(250,723),(270,626),(286,627),(310,596),(326,661),(345,684),(359,655),(377,557),(389,600),(409,684),(452,729),(483,719),(507,676),(524,609),(539,646),(556,637),(573,682),(594,703),(610,653),(629,711),(646,719),(660,694),(684,701),(710,729),(754,743),(795,750)],
[(115,834),(159,827),(191,796),(214,772),(243,777),(273,702),(287,702),(304,679),(318,728),(335,792),(358,817),(405,823),(477,811),(503,775),(524,690),(538,718),(557,718),(579,779),(606,799),(632,790),(649,803),(675,782),(696,795),(716,812),(760,816),(795,806)]],
6:[
[(115,51),(230,50),(290,65),(318,116),(350,121),(378,145),(406,85),(430,63),(489,51),(521,15),(539,49),(558,89),(580,58),(613,36),(642,83),(665,137),(686,201),(702,111),(716,105),(725,56),(744,126),(761,74),(783,39),(795,20)],
[(115,131),(230,128),(273,137),(296,202),(314,220),(332,156),(352,181),(373,216),(394,211),(417,146),(484,134),(523,105),(554,145),(585,132),(611,133),(640,151),(660,195),(675,214),(688,245),(705,186),(725,151),(744,216),(756,168),(775,140),(786,93),(795,118)],
[(115,230),(202,219),(240,241),(264,225),(273,239),(290,331),(306,435),(322,381),(337,275),(359,234),(438,225),(489,217),(517,200),(541,205),(560,229),(584,218),(627,200),(641,228),(656,264),(675,263),(690,309),(712,278),(725,214),(741,249),(760,266),(781,214),(787,169),(795,247)],
[(115,678),(239,668),(272,619),(295,536),(323,456),(348,521),(357,551),(380,468),(397,518),(414,599),(457,635),(492,607),(527,479),(547,481),(568,527),(590,575),(613,539),(632,603),(648,615),(676,633),(719,675),(761,689),(795,687)],
[(115,777),(230,770),(255,744),(279,646),(292,640),(315,610),(330,647),(346,704),(361,676),(380,586),(394,629),(412,689),(457,735),(481,726),(511,689),(531,602),(548,618),(569,661),(592,678),(613,640),(631,690),(658,721),(690,743),(731,752),(795,750)],
[(115,837),(174,834),(215,789),(230,800),(242,822),(255,800),(278,713),(297,704),(310,689),(325,736),(343,811),(365,839),(401,846),(471,830),(506,788),(528,684),(545,678),(565,741),(592,801),(612,806),(623,792),(638,810),(652,796),(680,806),(708,820),(737,837),(765,840),(795,862)]],
11:[
[(115,78),(220,77),(268,61),(305,38),(326,53),(348,112),(365,153),(383,140),(403,97),(433,75),(490,72),(541,62),(565,80),(628,66),(658,67),(687,99),(710,112),(727,99),(745,73),(776,74),(795,49)],
[(115,233),(153,227),(180,205),(205,174),(235,178),(249,147),(263,91),(270,139),(284,347),(295,425),(307,385),(326,290),(345,244),(388,218),(430,211),(472,205),(507,184),(522,159),(544,156),(563,221),(579,213),(594,227),(637,213),(661,269),(684,282),(698,277),(712,297),(729,272),(759,257),(779,245),(795,219)],
[(115,663),(238,660),(268,622),(309,530),(327,536),(341,562),(367,503),(391,556),(418,619),(465,638),(497,610),(523,523),(546,465),(565,493),(585,538),(606,549),(628,588),(651,603),(688,631),(739,649),(795,671)],
[(115,827),(163,819),(188,777),(215,744),(244,754),(270,647),(291,640),(308,676),(329,778),(350,818),(389,839),(448,837),(488,812),(520,712),(546,665),(562,706),(584,762),(606,779),(625,770),(649,780),(669,764),(691,793),(721,811),(762,820),(795,866)]],
14:[
[(115,94),(218,88),(251,79),(274,27),(287,80),(307,165),(321,140),(334,104),(350,108),(371,166),(385,156),(414,94),(445,88),(491,75),(526,47),(554,78),(578,69),(608,73),(622,65),(648,100),(666,121),(703,105),(727,84),(765,86),(795,60)],
[(115,176),(167,171),(214,152),(244,166),(269,115),(281,163),(295,372),(306,434),(319,345),(331,239),(349,198),(371,186),(413,179),(446,186),(472,177),(493,181),(522,168),(540,164),(565,189),(592,176),(628,176),(651,194),(681,215),(730,215),(767,211),(795,182)],
[(115,675),(174,672),(212,656),(240,654),(273,611),(309,599),(333,637),(350,625),(381,536),(397,514),(414,469),(432,513),(458,600),(489,639),(509,650),(525,627),(539,630),(557,642),(580,620),(600,575),(620,621),(649,642),(688,647),(717,654),(758,665),(795,669)],
[(115,827),(164,818),(190,797),(214,710),(228,669),(241,672),(258,693),(272,691),(289,711),(306,725),(325,770),(342,809),(370,828),(448,830),(498,819),(524,777),(537,774),(558,788),(580,804),(602,810),(620,788),(637,750),(652,779),(684,800),(719,761),(734,775),(754,806),(795,832)]]}
for fig,mol,states,zeroes in [(3,'AAA',['anionic','zwitterion','cationic'],[103,153,229]),(6,'VVV',['anionic','zwitterion','cationic'],[51,131,229]),(11,'SSS',['anionic','cationic'],[77,235]),(14,'KKK',['neutral_label','acidic_label'],[94,190])]:
 n=len(states)
 for i,g in enumerate(G[fig]):
  obs='vcd' if i<n else 'ir';state=states[i%n]
  add(fig,f'{mol}_{state}_D2O_{obs}',(115,8 if obs=='vcd' else 451,794,440 if obs=='vcd' else 860),[(112,1800),(746,1300)],g,zero=zeroes[i] if i<n else None,note=('Figure 11 caption says VVV; main text identifies SSS.' if fig==11 else 'Figure 14 labels acidic/neutral; text says pD 1 and 2, so exact pD is unresolved.' if fig==14 else ''))
# Main experimental profiles from fit figures; thin components not extracted.
for fig,xcols,edges,mol,states in [(5,[(108,440),(440,774)],[11,261,511,760],'VVV',['anionic','cationic']),(13,[(94,353),(353,614)],[11,313,616,918],'KKK',['acid_pD1','neutral_pD7'])]:
 for j,(l,r) in enumerate(xcols):
  for k,obs in enumerate(['ir','raman_iso','raman_aniso']):
   top,bot=edges[k:k+2]
   masks=[]
   if fig==5 and k==0:masks=[(112,14,299,48),(210,48,283,82)] if j==0 else [(444,14,562,82),(650,62,731,91)]
   if fig==13 and k==0:masks=[(100,18,205,57),(203,46,280,77),(286,21,346,65)] if j==0 else [(487,15,609,69),(437,66,498,97),(485,144,555,181)]
   # Full-height frequency guides are removed in the extractor.
   add(fig,f'{mol}_{states[j]}_'+('solvent_unspecified_' if fig==5 else 'D2O_')+obs,(l+3,top+4,r-3,bot-4),[(l,1550 if fig==5 or j==0 else 1500),(r,1750)],method='envelope',zero=bot-3,masks=masks,note='Main observed profile; experimental points and total fit overlap. Individual components excluded.'+(' Caption allows H2O or D2O without assigning panels; solvent left unresolved.' if fig==5 else ''))
for i,obs in enumerate(['ir','raman_iso','raman_aniso','vcd']):
 top,bot=[12,242,470,698,926][i:i+2]
 add(10,f'SSS_anionic_D2O_{obs}',(107,top+4,640,bot-4),[(104,1550),(643,1750)],method='envelope' if i<3 else 'guide',guide=None if i<3 else [(108,804),(170,824),(210,885),(233,914),(257,901),(290,839),(318,784),(346,764),(380,768),(418,789),(464,804),(520,810),(637,814)],zero=814 if i==3 else bot-4,masks=[(110,17,412,63)] if i==0 else [],note='Main observed profile; experimental markers and total fit overlap.')
add(9,'VVV_cationic_H2O_raman_iso',(144,125,790,522),[(140,1200),(736,1400)],method='envelope',zero=516,masks=[(420,130,650,170)],note='Only VVV is plotted; AAA is an annotated peak position, not a second spectrum.')
for col,mol in [('black','KKK'),('red','AAA')]:
 add(16,f'{mol}_acid_H2O_raman_iso',(142,120,763,623),[(138,1200),(768,1500)],method='envelope',zero=554,color=col,masks=[(598,290,715,339),(566,340,640,387)])



# Refinements after overlay inspection.
for c in configs:
 f=c['fig'];name=c['name']
 if f==1:
  if 'raman_iso' in name:
   c['masks']=[(325,20,412,52),(440,19,481,48),(378,126,409,153)]
   c['guide']=[(317,274),(359,276),(378,258),(397,211),(412,157),(425,49 if c['color']=='black' else 82),(435,113),(442,224),(459,267),(491,276),(506,276)]
  elif 'raman_aniso' in name:
   c['masks']=[(606,19,750,70)]
   c['guide']=[(588,274),(605,250),(625,160),(636,193),(650,242),(663,202),(678,91 if c['color']=='black' else 139),(692,97 if c['color']=='black' else 124),(707,79 if c['color']=='black' else 115),(721,205),(737,264),(778,275)]
  else:
   c['masks']=[(112,45,147,77),(152,78,181,108)]
   c['guide']=[(45,233 if c['color']=='black' else 255),(60,218),(69,163),(81,115 if c['color']=='black' else 24),(92,143),(107,211),(119,173),(134,113 if c['color']=='black' else 83),(144,123),(162,138),(179,231),(194,258),(235,268)]
 if f==5 and name.endswith('_ir'):
  if 'anionic' in name:c['guide']=[(112,250),(142,217),(172,106),(187,124),(204,184),(222,160),(247,109),(264,128),(287,189),(312,233),(351,258),(437,259)]
  else:c['guide']=[(444,250),(491,257),(532,245),(555,212),(575,131),(597,16),(615,42),(633,43),(646,76),(663,168),(678,184),(707,169),(728,183),(750,224),(770,247)]
 if f==9:
  c['masks']=[(326,133,630,187),(712,251,775,322)]
  c['guide']=[(145,509),(182,492),(216,425),(246,310),(273,207),(293,157),(309,179),(331,255),(352,294),(378,268),(403,343),(422,380),(451,348),(478,377),(509,448),(536,499),(569,474),(591,486),(615,519),(638,506),(666,466),(695,451),(723,427),(745,393),(764,442),(791,477)]
 if f==6 and name.endswith('zwitterion_D2O_ir'):
  c['guide']=[(115,777),(230,770),(255,744),(279,646),(292,640),(315,610),(330,647),(346,704),(361,676),(380,586),(394,629),(412,689),(457,735),(481,726),(501,692),(519,621),(532,601),(544,603),(559,641),(579,666),(592,678),(613,640),(631,690),(658,721),(690,743),(731,752),(795,750)]
 if f==11 and name.endswith('cationic_D2O_vcd'):c['guide'][-3:]=[(759,257),(777,221),(791,159),(795,148)]
 if f==13:
  if 'acid_pD1' in name:
   if name.endswith('_ir'):c['guide']=[(97,301),(135,308),(171,301),(196,254),(220,174),(239,131),(255,94),(278,131),(302,83),(318,130),(337,246),(350,282)]
   elif name.endswith('raman_iso'):c['guide']=[(97,608),(165,609),(196,589),(219,528),(239,443),(255,382),(275,410),(302,358),(318,438),(337,551),(351,590)]
   else:c['guide']=[(97,881),(110,898),(132,886),(148,903),(185,881),(219,625+0),(237,578+0),(257,573+0),(274,655),(302,685),(319,737),(339,855),(350,898)];c['guide']=[(97,881),(110,898),(132,886),(148,903),(185,881),(219,773),(237,736),(257,733),(274,764),(302,685),(319,737),(339,855),(350,898)]
  else:
   if name.endswith('_ir'):c['guide']=[(357,308),(378,281),(397,193),(417,30),(429,46),(440,136),(453,183),(475,298),(492,263),(503,229),(519,241),(533,246),(548,288),(565,310),(611,310)]
   elif name.endswith('raman_iso'):c['guide']=[(405,603),(427,603),(457,609),(480,597),(500,532),(527,451),(540,471),(555,567),(576,610),(611,608)];c['box']=(405,c['box'][1],c['box'][2],c['box'][3])
   else:c['guide']=[(357,916),(376,887),(390,849),(410,757),(422,751),(440,736),(447,707),(463,760),(476,903),(489,894),(503,829),(527,781),(545,823),(566,876),(592,912),(611,912)]
 if f==16:
  c['masks']=[(590,285,721,340),(574,350,638,409)]
  c['guide']=([(144,537),(171,505),(197,463),(221,402),(239,301),(258,184),(277,161),(292,203),(309,361),(332,471),(373,517),(423,443),(456,526),(496,484),(522,518),(559,448),(580,508),(605,567),(649,570),(671,522),(695,535),(729,549),(762,545)] if c['color']=='red' else [(144,529),(174,471),(201,417),(226,356),(252,308),(276,303),(304,360),(321,391),(349,380),(378,406),(413,429),(445,460),(476,436),(506,415),(528,401),(552,443),(575,473),(606,498),(629,521),(661,531),(689,559),(725,550),(761,560)])
 if c['guide'] is not None:c['method']='guide'

for c in configs:
 if c['fig']==13:
  obs=c['name'].rsplit('_',1)[-1]
  if c['name'].endswith('_ir'):
   c['zero']=311
   if 'acid_pD1' in c['name']:c['guide']=None;c['method']='envelope'
  elif c['name'].endswith('raman_iso'):c['zero']=612
  else:c['zero']=902;c['guide']=None;c['method']='envelope'
 if c['fig']==5:c['zero']=260 if c['name'].endswith('_ir') else 506 if c['name'].endswith('raman_iso') else 751
 if c['fig']==10 and not c['name'].endswith('_vcd'):c['zero']=235 if c['name'].endswith('_ir') else 466 if c['name'].endswith('raman_iso') else 697
(P/'trace_config.json').write_text(json.dumps(configs,indent=2))
records=[];overlays={}
for c in configs:
 fig=c['fig'];im=Image.open(P/f'fig{fig}.png').convert('RGB');rgb=np.array(im);view=Image.open(P/f'view{fig}.png');sx=im.width/view.width;sy=im.height/view.height
 gray=rgb.mean(2);rr,gg,bb=rgb.transpose(2,0,1).astype(float)
 mask=(rr<120)&(gg<120)&(bb<120)&(abs(rr-gg)<35) if c['color']=='black' else (rr>gg+40)&(rr>bb+25)&(rr<245)
 if fig in [3,6,11,14]:
  labs,n=label(mask);keep=[]
  from scipy.ndimage import find_objects
  for j,sl in enumerate(find_objects(labs),1):
   if sl is not None and sl[1].stop-sl[1].start>80*sx:keep.append(j)
  mask=np.isin(labs,keep)
 x0,y0,x1,y1=c['box'];x0,x1=int(x0*sx),int(x1*sx);y0,y1=int(y0*sy),int(y1*sy)
 for l,t,r,b in c['masks']:mask[int(t*sy):int(b*sy),int(l*sx):int(r*sx)]=False
 # Remove vertical reference lines, which occupy most of the panel height.
 if fig in [5,9,10,13]:
  cs=mask[y0:y1,x0:x1].sum(0);cols=np.where(cs>(y1-y0)*.65)[0]+x0
  for x in cols:mask[y0:y1,max(0,x-1):x+2]=False
 
 if fig in [5,10,13]:
  guidecols={5:[241,267,599,637],10:[234,341,388],13:[222,257,302,417,447,503,527]}[fig]
  for gx in guidecols:mask[y0:y1,int((gx-1.2)*sx):int((gx+1.2)*sx)+1]=False
 xs=np.arange(x0,x1+1);ys=np.full(len(xs),np.nan)
 guide=np.array(c['guide']) if c['guide'] else None
 for ii,x in enumerate(xs):
  yy=np.where(mask[y0:y1,x])[0]+y0
  if not len(yy):continue
  groups=np.split(yy,np.where(np.diff(yy)>1)[0]+1)
  if guide is not None:
   target=np.interp(x/sx,guide[:,0],guide[:,1])*sy
   group=min(groups,key=lambda g:abs(np.median(g)-target))
   if fig in [3,6,11,14]:
    n=3 if fig in [3,6] else 2
    stateorder=['anionic','zwitterion','cationic'] if n==3 else ['anionic','cationic'] if fig==11 else ['neutral_label','acidic_label']
    idx=next(j for j,t in enumerate(stateorder) if '_'+t+'_' in c['name'])
    if len(groups)==n:group=groups[idx]
   if abs(np.median(group)-target)>45*sy:continue
  else:
   # Reject very thin strokes where possible, retaining experimental markers/main profile.
   thick=[g for g in groups if len(g)>=max(1,int(sy*.65))]
   group=(thick or groups)[0]
  ys[ii]=np.median(group)
 valid=np.isfinite(ys);first,last=np.where(valid)[0][[0,-1]];xs=xs[first:last+1];ys=ys[first:last+1];valid=np.isfinite(ys);missing=int((~valid).sum());ys=np.interp(xs,xs[valid],ys[valid])
 # Robustly remove isolated text/marker specks without smoothing the spectral profile.
 from scipy.ndimage import median_filter
 med=median_filter(ys,size=max(3,int(sx*3)//2*2+1));bad=abs(ys-med)>12*sy
 ys[bad]=med[bad]
 if c['zero'] is not None:baseline=c['zero']*sy
 else:baseline=float(np.max(ys))
 intensity=baseline-ys;scale=np.max(abs(intensity));intensity/=scale
 cal=np.array(c['cal']);coef=np.polyfit(cal[:,0]*sx,cal[:,1],1);wn=np.polyval(coef,xs);order=np.argsort(wn)
 name=f'eker2002_fig{fig}_{c["name"]}.csv'
 np.savetxt(P/'csv'/name,np.c_[wn[order],intensity[order]],delimiter=',',header='wavenumber_cm-1,intensity_rel',comments='',fmt='%.6f')
 if fig not in overlays:overlays[fig]=im.copy()
 draw=ImageDraw.Draw(overlays[fig]);draw.line(list(zip(xs,ys)),fill=(0,150,220) if c['color']=='red' else (239,104,0),width=max(2,round(sx*1.1)))
 records.append(dict(file=name,figure=fig,identity=c['name'],notes=c['note'],baseline_pixel=baseline,normalization_scale_pixels=float(scale),pixel_to_wavenumber=coef.tolist(),interpolated_columns=missing,isolated_outliers_replaced=int(bad.sum()),status='pending user validation',points=len(xs)))
for fig,im in overlays.items():
 im.save(P/'validation'/f'fig{fig}_overlay.png');im.thumbnail((800,1000));im.save(P/'validation'/f'fig{fig}_review.png')
(P/'manifest.json').write_text(json.dumps(records,indent=2));print('Extracted',len(records),'spectra')
