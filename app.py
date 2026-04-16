import cowsay
import getpass
utilisateur = getpass.getuser()
cowsay.turkey(f"Salut {utilisateur} ! Je tourne dans Docker sans polluer ton Windows.")