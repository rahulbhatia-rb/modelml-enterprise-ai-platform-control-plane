import json,sys
from gate import evaluate
with open(sys.argv[1]) as f: result=evaluate(json.load(f))
if result["allowed"]:
 print("READY"); raise SystemExit(0)
print("BLOCKED")
for x in result["findings"]: print("- "+x)
raise SystemExit(1)
