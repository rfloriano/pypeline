class Pipeline(object):

    def __init__(self, action_list, before_action=None, after_action=None, before_forward=None, after_forward=None,
                 before_backward=None, after_backward=None, on_failed=None):
        self._executed = []
        self.action_list = action_list
        self.before_action = (lambda act, ctx, failed: None) if before_action is None else before_action
        self.after_action = (lambda act, ctx, failed: None) if after_action is None else after_action
        self.before_forward = (lambda act, ctx: None) if before_forward is None else before_forward
        self.after_forward = (lambda act, ctx: None) if after_forward is None else after_forward
        self.before_backward = (lambda act, ctx: None) if before_backward is None else before_backward
        self.after_backward = (lambda act, ctx: None) if after_backward is None else after_backward
        self.on_failed = (lambda act, ctx, e: None) if on_failed is None else on_failed

    def get_titles(self):
        return [a.name for a in self.action_list]

    def get_statuses(self):
        return [a.status for a in self.action_list]

    def actions_to_dict(self):
        return [a.to_dict() for a in self.action_list]

    def execute(self, context=None):
        if context is None:
            context = {}
        failed = False
        for action in self.action_list:
            self.before_action(action, context, failed)
            self._executed.insert(0, action)
            try:
                action.mark_as_doing()
                self.before_forward(action, context)
                action.forward(context)
                self.after_forward(action, context)
                action.mark_as_done()
            except Exception, e:
                failed = True
                action.mark_as_failed(e)
                self.on_failed(action, context, e)
                break
            self.after_action(action, context, failed)

        if failed:
            for action in self._executed:
                action.mark_as_undoing()
                self.before_action(action, context, failed)
                self.before_backward(action, context)
                action.backward(e, context)
                action.mark_as_undone()
                self.after_backward(action, context)
                self.after_action(action, context, failed)
        return self.actions_to_dict()
