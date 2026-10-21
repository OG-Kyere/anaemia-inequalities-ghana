import base64
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

root=Path('work/review_package')
repo=os.environ['GITHUB_REPOSITORY']
token=os.environ['GITHUB_TOKEN']
manifest=[]
files=[p for p in (root/'final').rglob('*') if p.is_file()]
files += [p for p in (root/'qa').rglob('*') if p.suffix in ('.png','.pdf')]
for p in files:
    payload=json.dumps({'encoding':'base64','content':base64.b64encode(p.read_bytes()).decode()}).encode()
    req=Request('https://api.github.com/repos/'+repo+'/git/blobs',data=payload,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','Content-Type':'application/json'},method='POST')
    with urlopen(req) as response:
        result=json.load(response)
    manifest.append({'path':p.relative_to(root).as_posix(),'sha':result['sha'],'bytes':p.stat().st_size})
print('PACKAGE_TRANSFER_MANIFEST='+json.dumps(manifest,separators=(',',':')))
(root/'transfer_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')

