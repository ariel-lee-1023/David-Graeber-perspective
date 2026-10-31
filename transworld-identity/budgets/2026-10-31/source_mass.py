from pathlib import Path
import json,re,hashlib
import argparse
ap=argparse.ArgumentParser(description='Reproduce primary-context mass counts; no model calls or raw text output.')
ap.add_argument('--sources',type=Path,required=True);args=ap.parse_args()
B=Path(__file__).resolve().parent;P=B.parents[2];S=args.sources
coverage=json.loads((P/'transworld-identity/full-read-coverage.json').read_text())
def clean(t):return re.sub(r'<[^>]*>','',t).replace('**','').strip()
def inside(n,r):return any(a<=n<=b for a,b in r)
def compress(ns):
 out=[]
 for n in sorted(ns):
  if out and out[-1][1]==n-1:out[-1][1]=n
  else:out.append([n,n])
 return out
sources={};pool={}
for s in coverage['sources']:
 raw=(S/s['filename']).read_bytes();assert hashlib.sha256(raw).hexdigest()==s['sha256'];lines=raw.decode().splitlines();eligible={};speaker=None
 for n,t in enumerate(lines,1):
  if not inside(n,s['ranges']):continue
  c=clean(t)
  if s['id']=='UT' and n in (569,798):speaker=None
  if s['id']=='AN' and c.startswith('#'):speaker=None
  if not c or c.startswith(('#','![','<!--')):continue
  use=True
  if s['id']=='AN':
   m=re.match(r"^([A-Z][A-Z .’'\-]{1,40}):",c)
   if m:speaker=m[1]
   use=speaker in ['DG','DAVID GRAEBER']
  elif s['id']=='UT':
   if inside(n,[[569,650],[798,875]]):
    m=re.match(r'^(Graeber|Appel|Moderators|Thomas Piketty|David Graeber):',c)
    if m:speaker=m[1]
    use=speaker in ['Graeber','David Graeber']
   else:use=inside(n,[[690,797],[883,1084],[1257,1411],[1726,2000],[2008,2113],[2121,2223]])
  if use:eligible[n]=len(t.split())
 pool[s['id']]=eligible
 sources[s['id']]={'filename':s['filename'],'sha256':s['sha256'],'declared_body_ranges':s['ranges'],'eligible_line_ranges':compress(eligible),'primary_context_words':sum(eligible.values()),'authorship':'joint work retained as joint evidence' if s['id']=='DA' else 'DG speaker turns only' if s['id']=='AN' else 'selected sole/joint essays and DG interview turns; known UR/BJ reprints and editorial opening excluded' if s['id']=='UT' else 'sole-authored body with embedded quotations treated as attributed context'}
spans={
'action-value':{'VA':[[234,3645]],'UT':[[1992,2000]]},
'obligation-power':{'DE':[[194,5671]],'UT':[[798,875]]},
'cooperation-care':{'FR':[[56,237],[696,861]],'AN':[[318,347],[1132,1171],[1300,1343]],'UT':[[1033,1084],[1772,2000],[2099,2113]],'BJ':[[2384,2675]]},
'history-possibility':{'DA':[[234,6509]],'UT':[[1992,2000]]},
'play-inquiry':{'UT':[[1033,1084],[2008,2223]],'AN':[[628,833],[964,1091]]},
'work-purpose':{'BJ':[[107,2675]],'UT':[[652,686],[1918,1966]]},
'bureaucracy-technology':{'UR':[[343,435],[639,1306]],'DA':[[5308,5344]]},
'violence-audiences':{'UT':[[1033,1084],[1257,1411],[1760,1760]]},
'inquiry-revision':{'VA':[[3324,3382],[3448,3448]],'UT':[[569,875],[883,1253],[1309,1309],[1760,1760],[1992,2000],[2117,2223]],'DE':[[5102,5102]]},
'dialogue-episodes':{'AN':[[508,537],[588,627],[964,1027]],'UT':[[569,650],[798,875],[1353,1411],[2205,2223]],'UR':[[343,371]]}}
rows={}
for name,ss in spans.items():
 words={k:sum(w for n,w in pool[k].items() if inside(n,rr)) for k,rr in ss.items()}
 rows[name]={'audited_explicit_ranges':ss,'words_by_source':words,'words':sum(words.values()),'coverage':'Conservative explicit-locator mass only; chapter-only references and unspecified surrounding text are not guessed. Overlap across modules is allowed; no within-module line is double counted.'}
total=sum(s['primary_context_words'] for s in sources.values())
out={'schema_version':1,'denominator_words':total,'denominator_kind':'Primary-source textual contexts, including joint authorship and attributed embedded quotations; not a count of exclusively Graeber-spoken words.','method':'Body ranges inherit full-read coverage. AN keeps DG turns; UT keeps listed essays and DG turns, excluding editorial opening and recognized UR/BJ reprints. Tags/headings are omitted; remaining lines use whitespace word counts.','adaptation':'Maps the legacy words_firsthand parameter to this explicitly scoped primary-source pool. Targets are planning calculations, not formal research admission. A 0-to-400 mass-term sensitivity is also reported.','sources':sources,'modules':rows,'core_ceiling_inputs':{'total_declared_body_words':coverage['total_body_words'],'primary_context_ratio':total/coverage['total_body_words'],'n_clusters':10,'n_clusters_basis':'Current ten thematic source groups, overlapping across books; not ten independent books or statistically certified clusters.','temporal_spread':['2000–2009','2010–2020'],'tokens_exceed_250000':True,'token_lower_bound_reason':'The counted primary-context words alone exceed 250000; the prescribed estimator includes at least whitespace runs plus Latin token contributions.','ceiling':7500}}
(B/'source-mass.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('Primary-context pool',total,'words; ratio',round(total/coverage['total_body_words'],4))
