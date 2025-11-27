Data = {   

    "Afghanistan": {
                "capital": "Kabul",
                "languages":"Pashto",
                "population": '27657145',
                "flag": "https://restcountries.eu/data/afg.svg",
                "currency": "Afghan afghani"
            },
    "Åland Islands":  {
                "capital": "Mariehamn",
                "languages": 
                    "Swedish",
                
                "population": '28875',
                "flag": "https://restcountries.eu/data/ala.svg",
                "currency": "Euro"
            },
    "Albania":       {
                "capital": "Tirana",
                "languages": 
                    "Albanian",
                
                "population": '2886026',
                "flag": "https://restcountries.eu/data/alb.svg",
                "currency": "Albanian lek"
            },

    "Algeria":        {
                
                "capital": "Algiers",
                "languages": 
                    "Arabic",
                
                "population": '40400000',
                "flag": "https://restcountries.eu/data/dza.svg",
                "currency": "Algerian dinar"
            },

    "American Samoa":  {
                "capital": "Pago Pago",
                "languages": 
                    "English",
                    "Samoan"
                "population": '57100',
                "flag": "https://restcountries.eu/data/asm.svg",
                "currency": "United State Dollar"
            }
}

from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = 'Countries'

headings = ['Name'] + list(Data["Afghanistan"].keys())
ws.append(headings)

for country in Data:
    list1 = list(Data[country].values())
    ws.append([country] + list1)

wb.save('Countries.xlsx')
