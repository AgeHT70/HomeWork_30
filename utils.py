import csv
import json


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csv_file:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csv_file)

        # convert each csv row into python dict
        for row in csvReader:
            finish_row = {}
            # add this python dict to json array
            # finish_row = {"model": "ads.ads",
            #               "pk": row["id"],
            #               "fields": row}
            finish_row = {"model": "ads.categories",
                          "pk": row["id"],
                          "fields": row}
            jsonArray.append(finish_row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as json_file:

        json_file.write(json.dumps(jsonArray, indent=4, ensure_ascii=False))


# csv_to_json("data/ads.csv", "fixtures/ads.json")
csv_to_json("data/categories.csv", "fixtures/categories.json")
