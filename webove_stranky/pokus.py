import smtplib
server = smtplib.SMTP('fs2025.erneks.cz', 587)
server.starttls()
server.login('mpeschout@erneks.cz', 'Andelove73')
print("OK")
server.quit()