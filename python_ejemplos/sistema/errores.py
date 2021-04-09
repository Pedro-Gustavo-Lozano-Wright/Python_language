
def errores():

    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    try:
        print(3 / 0)
    except TypeError:
        print("puedes seleccionar de entre los muchos tipos de error")
    except:
        print("An exception occurred")
    else:
        print("Nothing went wrong")
    finally:
        print("The 'try except' is finished")
    raise Exception("tambien te puedes inventar errores jajaj")

    # errores