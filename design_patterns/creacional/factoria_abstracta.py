
def ejemplo_factoria_abstracta():

    class AbstractFactory():

        def new_cargador(self):
            print("new_cargador")

        def new_cables(self):
            print("new_cables")

    class FactoryApple(AbstractFactory):

        def new_Apple_Iphon10(self):
            print("new_Apple_Iphon10")
            return Iphon10()

        def new_Apple_IpadPro(self):
            print("new_Apple_IpadPro")
            return IpadPro()

    class FactorySamsung(AbstractFactory):

        def new_Samsung_Note10(self):
            print("new_Samsung_Note10")
            return Note10()

        def new_Samsung_GalaxyTab(self):
            print("new_Samsung_GalaxyTab")
            return GalaxyTab()

    class AbstractSmarphon():
        # atributo_a = ""
        # def __init__(self, atributo_a = "gus"):
        #     self.atributo_a = atributo_a

        def metodo_llamar(self):
            print("metodo_llamar")

    class Iphon10(AbstractSmarphon):

        def metodo_emojis_3D(self):
            print("metodo_emojis_3D")

    class Note10(AbstractSmarphon):

        def metodo_pencil(self):
            print("metodo_pencil")

    class AbstractTablet():
        # atributo_b = ""
        # def __init__(self, atributo_b = ""):
        #     self.atributo_b = atributo_b

        def metodo_desktop_mode(self):
            print("metodo_desktop_mode")

    class IpadPro(AbstractTablet):

        def metodo_realidad_aumentada(self):
            print("metodo_realidad_aumentada")

    class GalaxyTab(AbstractTablet):

        def metodo_teclado(self):
            print("metodo_teclado")

    myIphon10 = FactoryApple().new_Apple_Iphon10()
    myIpadPro = FactoryApple().new_Apple_IpadPro()
    myNote10 = FactorySamsung().new_Samsung_Note10()
    myGalaxyTab = FactorySamsung().new_Samsung_GalaxyTab()

    myIphon10.metodo_emojis_3D()
    myIpadPro.metodo_realidad_aumentada()
    myNote10.metodo_pencil()
    myGalaxyTab.metodo_teclado()
