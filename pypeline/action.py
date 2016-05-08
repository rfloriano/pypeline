STATUSES = ['queued', 'doing', 'done', 'undoing', 'undone', 'failed']


class Action(object):
    name = 'Action'
    status = STATUSES[0]
    error = None

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

    def to_dict(self):
        error_str = ''
        if self.error:
            error_str = str(self.error)
        return {
            'name': self.name,
            'status': self.status,
            'error': error_str,
        }

    def backward(self, err, context):
        pass

    def forward(self, context):
        pass
