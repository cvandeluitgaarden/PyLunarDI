class DictionaryInterface:
    GOOD_MORNING = None
    GOOD_AFTERNOON = None
    GOOD_NIGHT = None
    HEART = None

class AbstractDictionary(DictionaryInterface):
    HEART = "ILOVEYOUILOVEYOUILOVEYOUILOVEYOUILOVEYOUILOVEYOUILOVEYOU\nILOVEYOUILO ****** VEYOU ****** ILOVEYOUILOVEYOUILOVEYOU\nILOVEYOU *********** I *********** LOVEYOUILOVEYOUILOVEY\nOUIUI *************** *************** VEYOUILOVEYOUILOVE\nYOUI ********************************** LOVEYOUILOVEYOUI\nIL ************************************* OVEYOUILOVEYOUI\nL *************I**LOVE**YOU*!************ OVEYOUILOVEYOU\nI *************************************** LOVEYOUILOVEYO\nU *************************************** ILOVEYOUILOVEY\nOU ************************************* ILOVEYOUILOVEYO\nUIL *********************************** OVEYOUILOVEYOUIL\nOVEYO ******************************* ULOVEYOUILOVEYOUIL\nOVEYOUI **************************** LOVEYOUILOVEYOUILOV\nEYOUILOVE *********************** YOUILOVEYOUILOVEYOUILO\nVEYOUILOVEYOU ***************** ILOVEYOUILOVEYOUILOVEYOU\nILOVEYOUILOVEYO ************* LOVEYOUILOVEYOUILOVEYOUILO\nUILOVEYOUILOVEYOU ********* LOVEYOUILOVEYOUILOVEYOUILOVE\nLOVEYOUILOVEYOUILOV ***** ILOVEYOUILOVEYOUILOVEYOUILOVEY\nEYOUILOVEYOUILOVEYOU *** YOULOVEYOUILOVEYOUILOVEYOUILOVE\nVEYOUILOVEYOUILOVEYOU * VEYOUILOVEYOUILOVEYOUILOVEYOUILO\nOVEYOUILOVEYOUILOVEYOUILOVEYOUILOVEYOUILOVEYOUILOVEYOUIL"

class DictionaryDE(AbstractDictionary):
    GOOD_AFTERNOON = "Guten Tag"
    GOOD_MORNING = "Guten Morgen"
    GOOD_NIGHT = "Gute Nacht"

class DictionaryEN(AbstractDictionary):
    GOOD_AFTERNOON = "Good afternoon"
    GOOD_MORNING = "Good morning"
    GOOD_NIGHT = "Good night"

class DictionaryNL(AbstractDictionary):
    GOOD_AFTERNOON = "Goedemiddag"
    GOOD_MORNING = "Goedemorgen"
    GOOD_NIGHT = "Goedenacht"

class DictionaryTR(AbstractDictionary):
    GOOD_AFTERNOON = "Tünaydın"
    GOOD_MORNING = "Günaydın"
    GOOD_NIGHT = "İyi geceler"