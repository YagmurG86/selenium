# ===================================================================================================================================
# ================================================ DATEI LESEN - Konventionell ======================================================
# ===================================================================================================================================

# f = open("C:/Users/guemu/OneDrive/Desktop/Python/04 - Selenium STM (Youtube)/PythonForTesters/dictionary_read.txt", "r", encoding="utf-8")

# woerter = {}

# # Or read() resp. readLine()
# for line in f:
#     woerter[line.split(" ")[0]] = line.split(" ")[1].strip()

# print(woerter)
# f.close()

# while True:
#     print("Geben sie ein Wort ein: ")
#     suchwort = input()

#     if suchwort in woerter:
#         print(woerter[suchwort])
#     elif suchwort == "q":
#         break
#     else:
#         print("Kein Eintrag vorhanden")

# ===================================================================================================================================
# ================================================ DATEI SCHREIBEN - Konventionell ==================================================
# ===================================================================================================================================

# woerter = {"Turkey": "Türkei", "Germany": "Deutschland", "France": "Frankreich"}

# f = open("C:/Users/guemu/OneDrive/Desktop/Python/04 - Selenium STM (Youtube)/PythonForTesters/dictionary_write.txt", "w", encoding="utf-8")

# # I have to ensure, that f.close() will be executed for example even if a Exception occurs
# try:
#     for eintrag in woerter:
#         # f.write(eintrag + " " + woerter[eintrag] + "\n")
#         f.write("{} {}\n".format(eintrag, woerter[eintrag]))
# finally:
#     f.close()

# ===================================================================================================================================
# ================================================== Mit Kontext Onjekt - WITH ======================================================
# ===================================================================================================================================

# ------------------- Example -----------------------
woerter = {"Turkey": "Türkei", "Germany": "Deutschland", "France": "Frankreich"}

with open("C:/Users/guemu/OneDrive/Desktop/Python/04 - Selenium STM (Youtube)/PythonForTesters/dictionary_write.txt", "w", encoding="utf-8") as f:
    for eintrag in woerter:
        f.write("{} {}\n".format(eintrag, woerter[eintrag]))
# with is ensureing that the file is closed in any case

# -------------- This is possible to -----------------
# with open(".../file1.txt", "w", encoding="utf-8") as f1, open(".../file2.txt", "w", encoding="utf-8") as f2:
    