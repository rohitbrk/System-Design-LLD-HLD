# this principle states that -
# Clients should not be forced to depend upon methods that they do not use. 
# Interfaces belong to clients, not to hierarchies.
# If a class doesn’t use particular methods or attributes, then those methods and attributes should be segregated into more specific classes.

from abc import ABC, abstractmethod


class BWPrinter(ABC):
    @abstractmethod
    def bw_print(self, document):
        pass


class ColourPrinter(ABC):
    @abstractmethod
    def colour_print(self, document):
        pass


class OldPrinter(BWPrinter):
    def bw_print(self, document):
        print(f"Printing {document} in black and white...")


class ModernPrinter(BWPrinter, ColourPrinter):
    def bw_print(self, document):
        print(f"Printing {document} in black and white...")

    def colour_print(self, document):
        print(f"Printing {document} in colour...")

# In the example, separate classes for BWPrinter and ColourPrinter have been defined,
# instead of defining a single Printer with both functionalities.
# If there is only one Printer class with both functionalities, we would have to deal with the error in OldPrinter,
# as it doesn't support colour printing functionality.
