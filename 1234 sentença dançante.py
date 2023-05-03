#  beecrowd | 1234
# Sentença Dançante

# Por TopCoder* EUA
# Timelimit: 1 

while True:
   try:
      setenca = input()

      maiusculo = True
      sentencaDancante = ""
      for letra in setenca:
         if letra == " ":
            sentencaDancante += " "
         else:
            if maiusculo:
               sentencaDancante += letra.upper()
            else:
               sentencaDancante += letra.lower()

            maiusculo = not maiusculo

      print(sentencaDancante)
   except EOFError:
      break