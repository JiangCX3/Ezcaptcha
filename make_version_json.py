import json
import re

setup_py = open("setup.py", "r").read()
version_text = re.findall('version_ = \"(.*)\"', setup_py)[0]

version = re.findall("^([\d.]*[\d])", version_text)[0]
stage = re.findall("^[\d.]*[\d]([a-z]*)", version_text)[0]
stage_full = stage
stage_version = re.findall("^[\d.]*[\d][a-z]*([0-9]*)", version_text)[0]

if stage == "a":
    stage_full = "Alpha"
elif "b":
    stage_full = "Beta"
elif "r":
    stage_full = "Candidate"
elif "rc":
    stage_full = "Release Candidate"

result = {
    "version": version,
    "stage": stage,
    "stage_full": stage_full,
    "stage_version": stage_version,
}

f = open("version.json", "w").write(json.dumps(result))
