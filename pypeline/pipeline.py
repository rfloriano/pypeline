class Pipeline(object):

    def __init__(self, action_list, before_action=None, after_acton=None, before_forward=None, after_forward=None,
                 before_backward=None, after_backward=None):
        self.action_list = action_list
        self.before_action = lambda act, ctx: None if before_action is None else before_action
        self.after_acton = lambda act, ctx: None if after_acton is None else after_acton
        self.before_forward = lambda act, ctx: None if before_forward is None else before_forward
        self.after_forward = lambda act, ctx: None if after_forward is None else after_forward
        self.before_backward = lambda act, ctx: None if before_backward is None else before_backward
        self.after_backward = lambda act, ctx: None if after_backward is None else after_backward

    def execute(self, context=None):
        if context is None:
            context = {}
        executed = []
        failed = False
        for action in self.action_list:
            self.before_action(action, context)
            executed.insert(0, action)
            try:
                self.before_forward(action, context)
                action.forward(context)
                self.after_forward(action, context)
            except Exception, e:
                failed = True
                break
            self.after_acton(action, context)

        if failed:
            for action in executed:
                self.before_action(action, context)
                self.before_backward(action, context)
                action.backward(e, context)
                self.after_backward(action, context)
                self.after_acton(action, context)
