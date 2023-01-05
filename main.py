import utils

if __name__ == "__main__":

    import utils
    lista = utils.get_init_all()
    links=[]
    for link in lista:
        links.append(utils.get_final_link(link))

    for link in links:
        utils.download_csv(link)