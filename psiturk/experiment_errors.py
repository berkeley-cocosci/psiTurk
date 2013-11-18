#----------------------------------------------
# ExperimentError Exception, for db errors, etc.
#----------------------------------------------
# Possible ExperimentError values.

from flask import render_template

class ExperimentError(Exception):
    """
    Error class for experimental errors, such as subject not being found in
    the database.
    """
    def __init__(self, value):
        experiment_errors = dict(
            status_incorrectly_set = 1000,
            hit_assign_worker_id_not_set_in_mturk = 1001,
            hit_assign_worker_id_not_set_in_consent = 1002,
            hit_assign_worker_id_not_set_in_exp = 1003,
            hit_assign_appears_in_database_more_than_once = 1004,
            already_started_exp = 1008,
            already_started_exp_mturk = 1009,
            already_did_exp_hit = 1010,
            tried_to_quit= 1011,
            intermediate_save = 1012,
            improper_inputs = 1013,
            ie_not_allowed = 1014,
            page_not_found = 404,
            in_debug = 2005,
            unknown_error = 9999
        )
        self.value = value
        self.errornum = experiment_errors[self.value]
        self.template = "error.html"
    def __str__(self):
        return repr(self.value)
    def error_page(self, request):
        return render_template(self.template, 
                               errornum=self.errornum, 
                               **request.args)