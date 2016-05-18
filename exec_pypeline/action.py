import traceback
import uuid

STATUSES = ['queued', 'doing', 'done', 'undoing', 'undone', 'failed']


class Action(object):
    name = 'Action'
    status = STATUSES[0]
    error = None
    outcome = None

    def __init__(self, *args, **kwargs):
        super(Action, self).__init__(*args, **kwargs)
        self.id = str(uuid.uuid4())

    def mark_as_doing(self):
        self.status = STATUSES[1]

    def mark_as_done(self):
        self.status = STATUSES[2]

    def mark_as_undoing(self):
        self.status = STATUSES[3]

    def mark_as_undone(self):
        self.status = STATUSES[4]

    def mark_as_failed(self, e):
        self.status = STATUSES[5]
        self.error = e

    def set_outcome(self, outcome):
        self.outcome = outcome

    def to_dict(self):
        error_str = None
        error_traceback = None
        if self.error:
            error_str = str(self.error)
            error_traceback = traceback.format_exc(self.error)
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'error': {
                'msg': error_str,
                'traceback': error_traceback,
            },
            'outcome': self.outcome,
        }

    def backward(self, err, context):
        raise NotImplementedError(
            'backward method need to be specified for an Action')

    def forward(self, context):
        raise NotImplementedError(
            'forward method need to be specified for an Action')
