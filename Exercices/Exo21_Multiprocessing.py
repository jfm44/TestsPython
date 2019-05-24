import sys
import datetime

maintenant = datetime.now()

print("Anne de naissance ? ", end='')
sys.stdout.flush()
data = sys.stdin.read()
print("Vous avez ", maintenant.year - int(data), "ans")
sys.exit(0)
