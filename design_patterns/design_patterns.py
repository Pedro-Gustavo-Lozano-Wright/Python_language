from design_patterns.creacional.factoria_abstracta import FactoryApple, FactorySamsung


def ejemplo_factoria_abstracta():
    myIphon10 = FactoryApple().new_Apple_Iphon10()
    myIpadPro = FactoryApple().new_Apple_IpadPro()
    myNote10 = FactorySamsung().new_Samsung_Note10()
    myGalaxyTab = FactorySamsung().new_Samsung_GalaxyTab()

    myIphon10.metodo_emojis_3D()
    myIpadPro.metodo_realidad_aumentada()
    myNote10.metodo_pencil()
    myGalaxyTab.metodo_teclado()