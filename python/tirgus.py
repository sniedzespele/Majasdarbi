class Tirgus:
    nosaukums = "none"
    darba_laiks = "08-18"
    veikali = 10
    paviljoni = 3

    def __init__(self, nosaukums, darba_laiks, paviljoni, veikali):
        self.nosaukums = nosaukums
        self.darba_laiks = darba_laiks
        self.veikali = veikali
        self.paviljoni = paviljoni
        print(self.nosaukums, "darba laiks ir no plkst. ", self.darba_laiks, "Šinī tirgū ir", self.paviljoni,"paviljoni.", "Katrā paviljonā ir", self.veikali, "veikali." )


Centrāltirgus = Tirgus ("Centrāltirgus", "07 - 19.", 90, 5)

Vidzemes_tirgus = Tirgus ("Vidzemes tirgus", "08 - 18.", 40, 4)


