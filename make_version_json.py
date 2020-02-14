import json
import re

setup_py = open("setup.py", "r").read()
version_text = re.findall('version_ = \"(.*)\"', setup_py)[0]

version = re.findall("^([\d.]*[\d])", version_text)[0]
stage = re.findall("^[\d.]*[\d]([a-z]*)", version_text)[0]
tag = stage
stage_version = re.findall("^[\d.]*[\d][a-z]*([\d.]*[\d])", version_text)[0]

if stage == "":
    stage_version = ""


if stage == "a":
    tag = "alpha #" + stage_version
elif "b":
    tag = "beta #" + stage_version
elif "r":
    tag = "candidate #" + stage_version
elif "rc":
    tag = "release candidate #" + stage_version
else:
    tag = ""

result = {
    "version": version,
    "stage": stage,
    "tag": tag,
    "stage_version": stage_version,
}

f = open("version.json", "w").write(json.dumps(result))
