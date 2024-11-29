# Nom du fichier à lire et fichier de sortie
input_file = "user_agent.txt"
output_file = "user_agent.txt"

# Lire le fichier et ajouter les guillemets
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Ajouter les guillemets à chaque ligne
modified_lines = [f'"{line.strip()}",\n' for line in lines]

# Écrire les modifications dans le fichier de sortie
with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(modified_lines)

print(f"Le fichier modifié a été enregistré dans {output_file}.")
