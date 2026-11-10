#!/usr/bin/env python3
"""Validate poster metadata, taxonomy paths and security before publication."""
import json,re,sys
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
SLUG=re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
issues=[]
def report(where,msg):issues.append(f"{where}: {msg}")
def main():
    tax=json.loads((ROOT/"catalog/taxonomy.json").read_text(encoding="utf8"))
    cats={}
    for c in tax["categories"]:
        if not SLUG.fullmatch(c["id"]):report("taxonomy",f"bad category {c['id']}")
        if c["id"] in cats:report("taxonomy","duplicate field")
        ss=[s["id"] for s in c["subfields"]]
        if len(ss)!=len(set(ss)) or any(not SLUG.fullmatch(x) for x in ss):report("taxonomy","bad/duplicate subfield")
        cats[c["id"]]=set(ss)
    ids=set();docs=list((ROOT/"posters").glob("*/*/*/poster.json"))
    if not docs:report("posters","no poster.json metadata")
    for f in docs:
        try:p=json.loads(f.read_text(encoding="utf8"))
        except Exception as e:report(f,f"JSON parse failed: {e}");continue
        for name in ("id","title","authors","venue","year","category","subcategory","summary","takeaway","method","limitations","source","assets","status","added"):
            if not p.get(name):report(f,f"missing {name}")
        pid=p.get("id","")
        if not SLUG.fullmatch(pid):report(f,"bad id slug")
        if pid in ids:report(f,"duplicate paper id")
        ids.add(pid)
        cat=p.get("category","");sub=p.get("subcategory","")
        if sub not in cats.get(cat,set()):report(f,"unknown taxonomy path")
        if f.parent.parts[-3:]!=(cat,sub,pid):report(f,"directory does not match metadata")
        if type(p.get("year")) is not int or not 1900<p["year"]<2100:report(f,"year invalid")
        if not isinstance(p.get("authors"),list) or not p["authors"]:report(f,"authors invalid")
        if p.get("status") not in ("draft","published"):report(f,"invalid status")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}",p.get("added","")):report(f,"bad added date")
        source=p.get("source",{})
        if not isinstance(source,dict):report(f,"source must be object");source={}
        url=source.get("url","")
        parts=urlsplit(url)
        if parts.scheme!="https" or not parts.netloc or parts.username:report(f,"source must be HTTPS")
        for k in ("version","citation"):
            if not source.get(k):report(f,f"missing source.{k}")
        assets=p.get("assets",{})
        if not isinstance(assets,dict):report(f,"assets invalid");continue
        for typ,name in assets.items():
            if typ not in ("svg","pdf","pptx","preview"):report(f,"unsupported asset type")
            if not isinstance(name,str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*",name):report(f,"unsafe asset name");continue
            if p.get("status")=="published" and not (f.parent/name).is_file():report(f,f"asset missing: {name}")
        if p.get("status")=="published" and not ("svg" in assets or "preview" in assets):report(f,"missing preview asset")
    for issue in issues:print("ERROR",issue,file=sys.stderr)
    print(f"Validated {len(docs)} paper(s), {len(cats)} categories, {len(issues)} error(s)")
    return int(bool(issues))
if __name__=="__main__":sys.exit(main())
