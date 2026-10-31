#!/usr/bin/env python3
"""Reproduce this planning audit. No model calls, source acquisition or runtime edits.
Usage: python3 recalculate.py --tool-root /path/to/persona-distiller
"""
import argparse,hashlib,importlib.util,json,subprocess,sys
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--tool-root',type=Path,required=True);a=ap.parse_args()
B=Path(__file__).resolve().parent;P=B.parents[2];tool=a.tool_root.resolve()
def read(p):return json.loads(p.read_text())
def put(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def load(name):
 s=importlib.util.spec_from_file_location(name,tool/'scripts'/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
I=read(B/'inventory.json');M=read(B.parent/'2026-10-31/source-mass.json');tc=load('token_count');cb=load('cluster_budget')
spec={'words_firsthand':M['denominator_words'],'clusters':[{'cluster_id':n,'words':M['modules'][n]['words'],**c['counts']} for n,c in I['clusters'].items()]}
put(B/'cluster-inputs.json',spec)
subprocess.run([sys.executable,str(tool/'scripts/cluster_budget.py'),str(B/'cluster-inputs.json'),'--json',str(B/'cluster-calculation.json')],check=True,stdout=subprocess.DEVNULL)
rows=[]
def add(path,target,counts,breakdown,decision,sensitivity=None):
 actual=tc.count(str(P/path),1/.6,1.3);actual['file']=path;delta=round(actual['tokens_est']-target,2)
 row={'path':path,'target_tokens':target,'actual_tokens':actual['tokens_est'],'delta_tokens':delta,'delta_percent':round(100*delta/target,2),'within_ten_percent':abs(delta)<=.1*target,'target_kind':'source-grounded editorial planning target, not research-certified budget','counts':counts,'formula_terms':breakdown,'measurement':actual,'sha256':sha(P/path),'decision':decision}
 if sensitivity:row['sensitivity']=sensitivity
 rows.append(row)
C=I['core'];counts={k:len(C[k]) for k in ['cost_refusal','projectible','procedure','verdict','interactional','variation']};terms={'frame':2200}
for key,price,cap in [('cost_refusal',250,6),('projectible',180,7),('procedure',200,5),('verdict',150,8),('interactional',140,5),('variation',120,4)]:terms[key]=price*min(counts[key],cap)
core_supply=sum(terms.values());core_target=max(3000,min(core_supply,M['core_ceiling_inputs']['ceiling']))
add('SKILL.md',core_target,counts,terms,'REBUILT. Core source-supported census fixed before drafting: two procedures and one interactional move added to the previous census. All core sections re-organized around the complete-body distillation; implementation safeguards earn no persona-supply allowance.',{'corpus_ceiling':M['core_ceiling_inputs']['ceiling'],'target_with_conservative_4000_ceiling':max(3000,min(core_supply,4000))})
F=I['frameworks'];counts={k:len(v) for k,v in F.items()};terms={'frame':700}
for key,price,cap in [('constructs',120,20),('procedure',200,6),('epistemic',130,6),('verdict',90,24),('moves',110,10),('personal',70,6)]:terms[key]=price*min(counts[key],cap)
terms['construct_index_allowance']=25*min(counts['constructs'],40)
add('references/frameworks.md',max(2000,min(sum(terms.values()),7000)),counts,terms,'KEEP. The legacy formula budgets separate entries and an index; current prose combines them and routes concrete cases to topic modules. Do not duplicate those cases or add an index solely to consume the allowance.')
V=I['voice'];counts={k:len(V[k]) for k in ['registers','rules','avoid','pairs','nopool_pairs']};counts['within_family_gradient']=V['within_family_gradient'];terms={'frame':600,'registers':550*min(counts['registers'],4),'gradient':250*bool(counts['within_family_gradient']),'rules':90*min(counts['rules'],18),'avoid':40*min(counts['avoid'],25),'pairs':120*min(counts['pairs'],8),'nopool_pairs':60*min(counts['nopool_pairs'],6)}
add('references/voice.md',max(2000,min(sum(terms.values()),7000)),counts,terms,'KEEP. Five evidenced expressive occasions are represented concisely; they are not five statistically certified families. No quantified avoidance table or artificial contrast pairs are added to satisfy a legacy layout.',{'single_family_target':max(2000,min(sum(terms.values())-terms['registers']+550,7000))})
for name,c in I['clusters'].items():
 counts=c['counts'];words=M['modules'][name]['words'];supply,target,terms,floor,recut,regs=cb.compute(counts,words,M['denominator_words'],9,counts['registers'])
 assert not floor and not recut
 no_mass=sum(terms.values())-terms['mass'];one_reg=no_mass-terms['registers']
 add(c['path'],target,counts,terms,'KEEP. '+c['retention_decision'],{'source_mass_term_range':[0,400],'target_range_for_unknown_full_mass':[max(1800,min(no_mass,6000)),max(1800,min(no_mass+400,6000))],'single_register_target_same_mass':max(1800,min(one_reg+terms['mass'],6000))})
actual={r['path']:r['actual_tokens'] for r in rows};baseline=sum(actual[k] for k in ['SKILL.md','references/frameworks.md','references/voice.md']);topics=[r for r in rows if '/clusters/' in r['path']]
result={'schema_version':1,'basis_commit':I['basis_commit'],'method':'Default scoring.md size formulas with documented editorial counts and source-mass mapping; no empirical admission scores or certified register measurements are fabricated.','coefficients_changed':False,'module_coefficients':cb.coefficient_set(),'tokenizer':{'kind':'heuristic, not a model-specific BPE count','tokens_per_han_char':1/.6,'tokens_per_latin_word':1.3,'digit_run_base':1.2,'digit_length_divisor':3,'punctuation_run':1,'whitespace_run':1},'formula_source_hashes':{n:sha(tool/n) for n in ['references/scoring.md','scripts/token_count.py','scripts/cluster_budget.py']},'inventory_sha256':sha(B/'inventory.json'),'source_mass_sha256':sha(B.parent/'2026-10-31/source-mass.json'),'modules':rows,'runtime_load':{'actual_default':round(baseline,2),'actual_plus_two_largest_distinct_topics':round(baseline+sum(sorted(r['actual_tokens'] for r in topics)[-2:]),2),'actual_all_runtime':round(sum(actual.values()),2),'actual_refs_total':round(sum(v for k,v in actual.items() if k!='SKILL.md'),2),'legacy_two_module_formula':core_target+2*max(r['target_tokens'] for r in topics)+rows[1]['actual_tokens']+rows[2]['actual_tokens'],'loading_limit':'Current routing permits more than two topic modules. The legacy two-module formula is a comparison scenario, not an enforced worst-case ceiling. User input, history, tool output and response allowance are additional.'},'runtime_modified':True,'new_evaluation_calls':0,'strict_research_budget_compliance':'not_established; this is a source-supported planning application under the explicit no-new-tests instruction'}
put(B/'results.json',result)

plan=read(B/'core-plan.json')
assert core_target==plan['target_tokens'] and rows[0]['counts']==plan['counts']
result.update(revision='core-rebuild-01',core_plan_sha256=sha(B/'core-plan.json'),source_mass_file='../2026-10-31/source-mass.json',source_mass_revision_note=I['revision_notes']['mass'])
put(B/'results.json',result)
lines=['# Core rebuild and current runtime budgets — 2026-10-31',
'The core was substantially rewritten from the completed eight-book distillation and targeted original passages. The [core plan](core-plan.json) fixed its source-supported census and target before drafting. The prior compact-entry exception is withdrawn for this revision.',
'**Planning compliance is not empirical recognition certification.** These use Persona-Distiller’s unchanged size formulas, with the explicitly disclosed source-supported editorial counts. Transfer/pressure/discrimination metrics and certified register families remain unknown. The tokenizer is the prescribed heuristic, not a model-specific BPE count. No new behavioral tests were run.',
'## Core target',
f'Target **{core_target:,.0f}**, actual **{rows[0]["actual_tokens"]:,.2f}**, deviation **{rows[0]["delta_percent"]:+.2f}%**. The ±10% interval is **{core_target*.9:,.0f}–{core_target*1.1:,.0f}**. Frontmatter is included.',
'Counts: 2 commitments, 4 projectible orientations, 4 procedures, 0 dated verdicts, 5 interactional moves, 1 contextual variation. Supply = 2,200 + 500 + 720 + 800 + 0 + 700 + 120 = 5,040; the retained editorial corpus ceiling is 7,500. The previous 4,500 target rises by 540 for category reconstruction, internal critique and interlocutor-led exploration. No coefficients were tuned to the draft.',
'The [inventory](inventory.json) traces every counted element to evidence. Language, loading, memory and portrayal safeguards are not counted as historical persona procedures. Conceptual overlaps are not additional independent corroboration. At a conservative 4,000 ceiling, the new core would exceed tolerance; the richer ceiling depends on the same disclosed corpus mapping as the preceding audit.',
'## All runtime files',
'The two topic inventories account for the actual F62/F63 additions, with overlapping desire passages relinked rather than recounted. Frameworks adds two procedures within an already saturated formula cap. Voice elaborates an existing rule without inventing a new register. Unchanged modules retain their previous targets.',
'| File | Target | Actual | Delta | Delta % | Result |','|---|---:|---:|---:|---:|---|']
for r in rows:lines.append(f'| `{r["path"]}` | {r["target_tokens"]:,.0f} | {r["actual_tokens"]:,.2f} | {r["delta_tokens"]:+,.2f} | {r["delta_percent"]:+.2f}% | '+('Within ±10%' if r['within_ten_percent'] else 'Disclosed reference exception')+' |')
lines += ['', '## Scope of the retained reference exceptions',
'This task makes the **core** meet its budget. It does not claim every reference meets its target. Frameworks and voice still compress their legacy layout allowances; care and inquiry preserve longer argument/qualification chains. Play now also carries the category-reconstruction chain and its attribution limits. None was inflated or stripped of evidence merely to change a residual. The previous blanket statement that there was no important content omission is superseded: the core needed fuller concept generation, internal critique and shared exploration.',
I['revision_notes']['mass'],
'## Load cost and reproduction',
f'Default core + frameworks + voice: **{result["runtime_load"]["actual_default"]:,.2f}** estimated tokens; plus the two largest topic modules: **{result["runtime_load"]["actual_plus_two_largest_distinct_topics"]:,.2f}**. All runtime modules: **{result["runtime_load"]["actual_all_runtime"]:,.2f}**. '+result['runtime_load']['loading_limit'],
'Run `python3 transworld-identity/budgets/2026-10-31-core-rebuild/recalculate.py --tool-root /path/to/persona-distiller`. It reuses the preceding source-mass artifact, calls the official cluster calculator and tokenizer, and rewrites this report plus the numeric outputs. [Results](results.json) retain current hashes, contributions and sensitivities; the [preceding report](../2026-10-31/report.md) remains a historical audit of its recorded runtime.',
'Current recognition is not run. The three earlier diagnostic answers and original eight-call run remain historical evidence for their frozen inputs; neither certifies this rewrite. Source/package checks and arithmetic do not substitute for that evidence.']
start=next(i for i,l in enumerate(lines) if l.startswith('| File'))
end=start+2+len(rows)
(B/'report.md').write_text('\n\n'.join(lines[:start])+'\n\n'+'\n'.join(lines[start:end])+'\n\n'+'\n\n'.join(l for l in lines[end:] if l)+'\n')
print('\n'.join(f'{r["path"]:48} target={r["target_tokens"]:5} actual={r["actual_tokens"]:8.2f} delta={r["delta_percent"]:+7.2f}%' for r in rows))
