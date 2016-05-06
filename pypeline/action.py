STATUSES = ['queued', 'doing', 'done', 'undoing', 'undone', 'failed']


class Action(object):
    name = 'Action'
    status = STATUSES[0]

    def mark_as_doing(self):
        self.status = STATUSES[1]

    def mark_as_done(self):
        self.status = STATUSES[2]

    def mark_as_undoing(self):
        self.status = STATUSES[3]

    def mark_as_undone(self):
        self.status = STATUSES[4]

    def mark_as_failed(self):
        self.status = STATUSES[5]

    def to_dict(self):
        return {
            'name': self.name,
            'status': self.status,
        }

    def backward(self, err, context):
        pass

    def forward(self, context):
        pass
