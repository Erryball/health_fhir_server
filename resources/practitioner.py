from flask import request
from common import Resource
from resources import SearchRecords
from resources import ReadRecord
from resources import ValidateRecord
from resources import Routing

class HP_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'Not implemented', 405

class HP_Search(Resource):
    def get(self):
        '''Search interaction'''
        action = SearchRecords(endpoint='practitioner', request=request)
        return action.records

class HP_Validate(Resource):
    def post(self, log_id=None):
        '''Validate interaction'''
        action = ValidateRecord(endpoint='practitioner', record=request.data)
        return action.valid

class HP_Record(Resource):
    def get(self, log_id):
        '''Read interaction'''
        action = ReadRecord(endpoint='practitioner', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class HP_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

routing = Routing('Practitioner')
routing['create'] = HP_Create
routing['search'] = HP_Search
routing['validate'] = HP_Validate
routing['record'] = HP_Record
routing['version'] = HP_Version

__all__=['routing']
