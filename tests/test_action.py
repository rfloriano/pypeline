from unittest import TestCase
from preggy import expect

from .pass_action import PassAction


class MyAction(PassAction):
    name = "My super action"


class ActionTestCase(TestCase):

    def test_my_action(self):
        act = MyAction()
        expect(act.name).to_equal("My super action")
        expect(act.forward({})).to_equal(None)
        expect(act.backward(None, {})).to_equal(None)

    def test_to_dict_method(self):
        act = MyAction()
        expect(act.to_dict()).to_equal({
            'id': act.id,
            'name': act.name,
            'status': act.status,
            'error': {
                'msg': None,
                'traceback': None,
                'class': None,
            },
            'outcome': None,
        })
