# PyScriptTPGen
Générateur de "feuilles de TP" au format html pour mes étudiants de tutorat, avec des REPL Python. Aucune installation requise.

Deux versions : 
- Script Python classique générant directement un fichier html
- Notebook plus "intuitif" qui affiche (entre autres) le code HTML final mais ne crée pas de fichier

Pour que le programme fonctionne, il faut avoir : 
- pandas installé. J'aurais pu faire sans mais je l'ai utilisé par réflexe.
- un fichier json contenant les questions, astuces et solutions (voir détails dans le fichier fourni)
- un autre json contenant les détails de la page et de l'environnement (//)

Le code est assez simple, mais prenez garde à la partie HTML incluse dans le code Python.
Il ne faut pas toucher cette dernière (à moins d'avoir tout lu) car j'ai transformé le HTML en une f-string.
Si j'ai le temps, j'écrirai un convertisseur HTML->fstring.
