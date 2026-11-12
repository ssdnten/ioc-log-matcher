"""Match exact IP and domain indicators against structured offline event logs with normalized values."""
import argparse
import ipaddress
import json
from pathlib import Path

def normalize(kind,value):
    if kind=='ip': return str(ipaddress.ip_address(value))
    if kind=='domain':
        host = value.rstrip('.').encode('idna').decode('ascii').lower()
        if not host or len(host)>253 or any(not label or len(label)>63 or label.startswith('-') or label.endswith('-') or any(not(c.isalnum() or c=='-') for c in label) for label in host.split('.')):
            raise ValueError('invalid domain')
        return host
    raise ValueError('indicator type must be ip or domain')

def match(indicators,events):
    index = {}
    for indicator in indicators:
        key = (indicator['type'],normalize(indicator['type'],indicator['value']))
        index.setdefault(key,set()).add(indicator.get('label','unlabelled'))
    findings=[]
    for number,event in enumerate(events,1):
        for field,kind in [('ip','ip'),('domain','domain')]:
            if field not in event: continue
            value=normalize(kind,event[field])
            if (kind,value) in index:
                findings.append(dict(event=number,type=kind,value=value,labels=sorted(index[(kind,value)])))
    return findings

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('indicators',type=Path)
    parser.add_argument('events',type=Path)
    args=parser.parse_args()
    try:
        indicators=json.loads(args.indicators.read_text(encoding='utf-8'))
        events=[json.loads(line) for line in args.events.read_text(encoding='utf-8').splitlines() if line.strip()]
        print(json.dumps(match(indicators,events),indent=2))
    except (OSError,ValueError,KeyError,TypeError) as exc:
        parser.exit(2,f'error: {exc}\n')

if __name__=='__main__': main()
