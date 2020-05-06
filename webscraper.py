from selenium import webdriver
import pandas as pd





def get_diplay_links(driver, startpage, limit):
    loop = True
    list = []
    number_of_links =0
    driver.get(startpage)

    while loop:
        elements = driver.find_elements_by_class_name('ellipsis')
        number_of_links = number_of_links + len(elements)
        for element in elements:
            list.append(element.get_attribute("href"))
        try:
            nextpage = driver.find_element_by_xpath('//*[@id="srchrslt-pagination"]/div/div[2]/a').get_attribute("href")
            driver.get(nextpage)
        except:
            print("Reached end of file")

        print("New Page")
        print("Number of Links: ",number_of_links)
        if number_of_links >= limit:
            print(list)
            break
    return list

def get_data(driver, link_list):
    keys =["title", "price", "location", "date", "views"]
    keys2 = ["brand","model", "km", "year_made", "fuel","power","trans","type","doors","hu","environment","emission","color","interior","condition"]

    datasets = dict.fromkeys(keys)
    for key in datasets:
        datasets[key] = []
    done_counter = 0
    for link in link_list:
        try:
            driver.get(link)
            datasets['title'].append(driver.find_element_by_id("viewad-title").get_attribute('textContent').strip('\n').strip())
            datasets['price'].append(driver.find_element_by_xpath('//*[@id="viewad-price"]').get_attribute('textContent').strip('\n').strip())
            datasets['location'].append(driver.find_element_by_id("viewad-locality").get_attribute('textContent').strip('\n').strip())
            datasets['date'].append(driver.find_element_by_id("viewad-extra-info").get_attribute('textContent').split('\n')[1].strip())
            datasets['views'].append(driver.find_element_by_id("viewad-cntr-num").get_attribute('textContent').strip('\n').strip())
            details_keys = driver.find_elements_by_class_name('addetailslist--detail')
            details_values = driver.find_elements_by_class_name('addetailslist--detail--value')

            done_counter = done_counter + 1
            for i in range(len(details_keys)):
                if details_keys[i].get_attribute("textContent").split('\n')[1].strip() in datasets:
                    datasets[details_keys[i].get_attribute("textContent").split('\n')[1].strip()].append(details_values[i].get_attribute('textContent').strip('\n').strip())
                else:
                    datasets[details_keys[i].get_attribute("textContent").split('\n')[1].strip()] =[]+['XXX']*(done_counter-1)
                    datasets[details_keys[i].get_attribute("textContent").split('\n')[1].strip()].append(details_values[i].get_attribute('textContent').strip('\n').strip())
            for key in datasets:
                if len(datasets[key]) < done_counter:
                    datasets[key].append('XXX')
        except Exception as e:
            print(e)
            continue

    print(datasets)
    datasets.pop('', None)
    return(datasets)
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.implicitly_wait(4)  # seconds
    startpage = "https://www.ebay-kleinanzeigen.de/s-autos/volkswagen/golf/k0c216+autos.marke_s:volkswagen+autos.model_s:golf"

    #list = ['https://www.ebay-kleinanzeigen.de/s-anzeige/lt-28-volkswagen-wohnmobil-bulli-transporter-caravan/1389180226-216-5325', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-v-1-9-tdi-comfortline-105-ps-diesel-09-2005-151-000-km/1393722449-216-9457', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-country/1383214057-216-8296', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-plus-2-0-tdi-dpf-trendline/1396459119-216-2588', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-solider-golf-5-golf-1-9-tdi-comfortline/1396457700-216-1699', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-3-1-8-cabrio-karmann/1396456802-216-8348', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-polo-cross-1-6-tdi-standheizung-led-xenon-top-/1396456021-216-16629', 'https://www.ebay-kleinanzeigen.de/s-anzeige/pkw-zu-verkaufen/1396455551-216-17624', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-1-6-tdi-dpf-match/1396455611-216-8888', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-3-silber-tuev-bis-11-2021-1-8-75ps/1396455047-216-4320', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-cabrio-1-8-joker/1396455135-216-2706', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-plus-2-0-tdi-dpf-dsg-team/1396454646-216-941', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-1-9-tdi-special/1396453507-216-2632', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-gti-bluemotion-technology-dsg/1396452863-216-6185', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-7-150-ps-neue-inspektion-reifen-continental/1396452651-216-1142', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-1-4-trendline/1396451965-216-16362', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-2-0-tdi-dpf-highline/1396451648-216-2436', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-3-variant-mit-tuev-12-2021/1396451485-216-17554', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-1-4-goal-scheckheftgepflegt/1396450419-216-3545', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-5-1-4/1396450081-216-8260', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-gti-223-ps-tiefbett-klima-sport-tuev-top/1391849589-216-3365', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-1-4-comfortline/1396449011-216-4650', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-5-gti-pirelli-dsg-edition-30-r32-hg-remus-bilstein-mtm/1396447945-216-3276', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-4-1-6-sr/1396447921-216-5191', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-6-1-4-tsi-dsg-highline-5-tuerig-silber/1396447895-216-8993', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-gti-1-8t-agu-tausch-moeglich/1396447490-216-9137', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-lupo-rot/1396447219-216-3144', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-2-vr6-panoramadach-neulack-tuev-neu/1395225374-216-8834', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-sportsvan-highline-standh-dsg-xenon-ahk-navi-kess/1332649926-216-2643', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-4-zu-verkaufen/1396446391-216-12923', 'https://www.ebay-kleinanzeigen.de/s-anzeige/schicker-golf-6/1396446281-216-7921', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-4-comfortline/1396445607-216-20942', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-plus-mit-abnehmbarer-anhaengerkupplung/1396445540-216-8534', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-iv-1-6/1396445394-216-1938', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-1-4-tsi-highline/1396445252-216-4987', 'https://www.ebay-kleinanzeigen.de/s-anzeige/verkaufe-golf-4-1999-1-9-tdi/1396445137-216-2633', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-5-gti-edition-30/1380722655-216-5781', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-4-cabriolet-diesel-mit-city-filter-/1396444440-216-8702', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-1-4-klima/1396444399-216-3069', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-6-variant-zum-verkaufen/1396443870-216-2104', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-6-gti-sehr-guter-zustand/1396443857-216-5394', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-vii-2-0-tdi-dsg-xenon-pano-klima-pdc-highl/1396443502-216-4283', 'https://www.ebay-kleinanzeigen.de/s-anzeige/verkauf-golf-lv-1-6/1396443309-216-7529', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-2-gl-top-zustand-gutachten-bbs-kein-rost/1396442414-216-5257', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-4-1999/1396442366-216-8907', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-gti-performance-bluemotion-technology/1396442419-216-1953', 'https://www.ebay-kleinanzeigen.de/s-anzeige/verkaufe-vw-golf-garagenfahrzeug/1396441741-216-7901', 'https://www.ebay-kleinanzeigen.de/s-anzeige/vw-golf-v-golf-plus-golf-5-schwarz/1396441568-216-2557', 'https://www.ebay-kleinanzeigen.de/s-anzeige/-golf-5-1-4fsi-/1396440868-216-1835', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-iii-automatik-erst-115-tkm-gelaufen/1396440838-216-2492', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-1-4-edition/1396440523-216-2636', 'https://www.ebay-kleinanzeigen.de/s-anzeige/golf-4-1-6-sr/1396439712-216-8238', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-1-2-tsi-dsg-trendline/1396439623-216-7615', 'https://www.ebay-kleinanzeigen.de/s-anzeige/volkswagen-golf-variant-1-6-tdi-dpf-comfortline/1396439463-216-4951']
    list = get_diplay_links(driver, startpage, 100)
    print(list)
    df = pd.DataFrame(get_data(driver, list))
    print(df.head())
    df.to_csv("golf_ebay.csv")

    driver.close()
