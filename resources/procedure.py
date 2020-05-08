from flask import request
from common import Resource
from resources import SearchRecords
from resources import ReadRecord
from resources import ValidateRecord
from resources import Routing

class OP_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'Not implemented', 405

class OP_Search(Resource):
    def get(self):
        '''Search interaction'''
        action = SearchRecords(endpoint='procedure', request=request)
        return action.records

class OP_Validate(Resource):
    def post(self, log_id=None):
        '''Validate interaction'''
        action = ValidateRecord(endpoint='procedure', record=request.data)
        return action.valid

class OP_Record(Resource):
    def get(self, log_id):
        '''Read interaction'''
        action = ReadRecord(endpoint='procedure', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class OP_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

routing = Routing('Procedure')
routing['create'] = OP_Create
routing['search'] = OP_Search
routing['validate'] = OP_Validate
routing['record'] = OP_Record
routing['version'] = OP_Version

__all__=['routing']
