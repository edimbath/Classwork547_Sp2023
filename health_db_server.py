"""
Database = dictionary
keys -> ids for the patients
values -> dictionary with name and blood type and id and anything else added
"""
import logging
from flask import Flask, request, jsonify


db = {}  # global database variable to access from all functions


app = Flask(__name__)  # global app variable to link to flask to run server


# function to add patient to db with specific variables
def add_patient_to_db(patient_id, name, blood_type):
    new_patient = {"id": patient_id,
                   "name": name,
                   "blood_type": blood_type,
                   "tests": []}
    db[patient_id] = new_patient
    print(db)


def add_test_to_db(patient_id, test_name, test_value):
    db[patient_id]["tests"].append((test_name, test_value))
    print(db)


# first route for server to run, this is flask handler
@app.route("/new_patient", methods=["POST"])
def post_new_patient():  # name of type (post) then name of route
    # get input data
    in_data = request.get_json()  # need to get input data from client
    # call other function to do work
    answer, status_code = new_patient_driver(in_data)  # this does the work
    # don't know what it will do yet but set up here
    return jsonify(answer), status_code  # safest to jsonify all answers/returns
    # return a response


def new_patient_driver(in_data):  # this function brings in the data for above
    # validate input
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    validation = validate_input_data_generic(in_data, expected_keys,
                                             expected_types)
    # make sure indata is correct
    # this next part is done after having full validation done
    if validation is not True:
        return validation, 400
    # do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # return an answer
    return "Patient successfully added", 200


def validate_input_data_generic(in_data, expected_keys, expected_types):
    # this comes from above and does work to
    # validate
    if type(in_data) is not dict:  # make sure type is correct
        return "Input is not a dictionary"
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


@app.route("/add_test", methods=["POST"])
def post_new_test():
    # get input data
    in_data = request.get_json()
    # call other function to do work
    answer, status_code = new_test_driver(in_data)
    return jsonify(answer), status_code
    # return a response


def does_patient_exist_in_db(patient_id):
    if patient_id in db:
        return True
    else:
        return False


def new_test_driver(in_data):
    # validate input
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    validation = validate_input_data_generic(in_data, expected_keys,
                                             expected_types)
    if validation is not True:
        return validation, 400
    # do the work
    does_id_exist = does_patient_exist_in_db(in_data["id"])
    if does_id_exist is False:
        return "Patient id {} does not exist in database"\
            .format(in_data["id"]), 400
    add_test_to_db(in_data["id"], in_data["test_name"],
                   in_data["test_result"])
    # return an answer
    return "Test successfully added", 200


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_get_results(patient_id):
    answer, status = get_results_driver(patient_id)
    return jsonify(answer), status


def get_results_driver(patient_id):
    validation = validate_patient_id_from_get(patient_id)
    if validation is not True:
        return validation, 400
    patient = get_patient_from_dictionary(int(patient_id))
    return patient['tests'], 200


def get_patient_from_dictionary(patient_id):
    patient = db[patient_id]
    return patient


def validate_patient_id_from_get(patient_id):
    try:
        patient_num = int(patient_id)
    except ValueError:
        return "Patient_id should be an integer"
    if does_patient_exist_in_db(patient_num) is False:
        return "Patient_id of {} does not exist in database".format(patient_num)
    return True


if __name__ == "__main__":
    logging.basicConfig(filename="server.log", filemode='w')
    app.run()
