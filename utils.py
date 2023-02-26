import csv
import json

ADS_MODEL = 'ads.Ads'
LOCATION_MODEL = 'users.Location'
USER_MODEL = 'users.User'
CATEGORY_MODEL = 'ads.Categories'


def csv_to_json(csvFilePath, jsonFilePath, model):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csv_file:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csv_file)

        # convert each csv row into python dict
        for row in csvReader:
            record = {"model": model}
            del row['id']

            if model == ADS_MODEL:
                row['price'] = float(row['price'])
                row['author_id'] = int(row['author_id'])
                row['category_id'] = int(row['category_id'])

                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            elif model == LOCATION_MODEL:
                row['lat'] = float(row['lat'])
                row['lng'] = float(row['lng'])

            elif model == USER_MODEL:
                row['locations'] = [int(row['location_id'])]
                del row['location_id']

            record['fields'] = row

            jsonArray.append(record)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as json_file:

        json_file.write(json.dumps(jsonArray, indent=4, ensure_ascii=False))


csv_to_json("data/ad.csv", "fixtures/ads.json", ADS_MODEL)
csv_to_json("data/category.csv", "fixtures/categories.json", CATEGORY_MODEL)
csv_to_json("data/location.csv", "fixtures/location.json", LOCATION_MODEL)
csv_to_json("data/user.csv", "fixtures/users.json", USER_MODEL)
