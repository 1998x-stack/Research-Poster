#!/usr/bin/env python3
"""Generate a static, secure GitHub Pages gallery from poster.json files."""
import argparse, json, html, shutil
from pathlib import Path
from datetime import datetime

ROOT=Path(__file__).resolve().parents[1]
def h(s): return html.escape(str(s or ""),quote=True)

def papers():
    data=json.loads((ROOT/"catalog/taxonomy.json").read_text(encoding="utf8"))
    names={(c["id"],s["id"]):(c["name"],s["name"]) for c in data["categories"] for s in c["subfields"]}
    out=[]
    for f in sorted((ROOT/"posters").glob("*/*/*/poster.json")):
        p=json.loads(f.read_text(encoding="utf8"))
        if p["status"]!="published":continue
        if (p["category"],p["subcategory"]) not in names:raise ValueError(f"Unknown taxonomy: {f}")
        p["field_name"],p["subfield_name"]=names[p["category"],p["subcategory"]]
        folder=f.parent;rel=folder.relative_to(ROOT).as_posix()
        p["paths"]={k:rel+"/"+v for k,v in p["assets"].items() if (folder/v).is_file()}
        if not (p["paths"].get("svg") or p["paths"].get("preview")):raise ValueError(f"No preview: {f}")
        p["page"]="paper/"+p["id"]+"/"
        out.append(p)
    return sorted(out,key=lambda p:(not p.get("featured",False),-p["year"],p["title"].lower())),data

def detail(p,previous,nxt):
    paths=p["paths"]; image=paths.get("svg") or paths.get("preview")
    buttons="".join(f'<a class="button solid" href="../../{h(paths[k])}" download>{h(title)}</a>' for k,title in (("pdf","Download PDF"),("pptx","Editable PPTX"),("svg","Open SVG")) if k in paths)
    neighbors="".join(f'<a class="button outline" href="../../{h(x["page"])}">{h(label)}: {h(x["title"])}</a>' for x,label in ((previous,"← Previous"),(nxt,"Next →")) if x)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{h(p["title"])} · Research Poster</title><meta name="description" content="{h(p["summary"])}"><link rel="stylesheet" href="../../assets/style.css"></head><body><header class="header"><a class="logo" href="../../">R<span>·</span>P <small>RESEARCH POSTER</small></a><nav><a href="../../">← ALL POSTERS</a><a href="https://github.com/1998x-stack/Research-Poster">GITHUB ↗</a></nav></header><main class="detail"><p class="kicker">{h(p["field_name"])} / {h(p["subfield_name"])} · {h(p["year"])}</p><h1>{h(p["title"])}</h1><p class="lead">{h(p["takeaway"])}</p><p class="muted">{h(p["venue"])} · {h(", ".join(p["authors"]))}</p><div class="actions">{buttons}<a class="button outline" target="_blank" rel="noopener noreferrer" href="{h(p["source"]["url"])}">Original paper ↗</a></div><a href="../../{h(image)}" target="_blank" rel="noopener noreferrer" class="poster-view"><img src="../../{h(image)}" alt="Full research poster: {h(p["title"])}"></a><section class="detail-info"><div><h2>Research in brief</h2><p>{h(p["summary"])}</p><h3>Method</h3><p>{h(p.get("method"))}</p></div><div><h2>Limitations & provenance</h2><p>{h(p.get("limitations"))}</p><h3>Reference</h3><p>{h(p["source"]["citation"])}</p><p class="muted">{h(p["source"]["version"])}</p></div></section><div class="actions">{neighbors}</div></main><footer>RESEARCH POSTER · SCIENTIFIC FIDELITY FIRST. <a href="../../">← COLLECTION</a></footer></body></html>'''

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",default="_site");a=parser.parse_args()
    dest=Path(a.output).resolve()
    if dest==ROOT or dest in (ROOT/"site",ROOT/"posters",ROOT/"catalog"):raise ValueError("Unsafe output path")
    if dest.exists():shutil.rmtree(dest)
    shutil.copytree(ROOT/"site",dest)
    items,taxonomy=papers()
    for i,p in enumerate(items):
        for rel in set(p["paths"].values()):
            t=dest/rel;t.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,t)
        target=dest/p["page"]/"index.html";target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(detail(p,items[i-1] if i else None,items[i+1] if i+1<len(items) else None),encoding="utf8")
    payload={"generated_at":datetime.utcnow().isoformat()+"Z","total":len(items),"taxonomy":taxonomy["categories"],"posters":items}
    (dest/"catalog.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf8")
    print(f"Built {len(items)} poster pages in {dest}")

if __name__=="__main__":main()
