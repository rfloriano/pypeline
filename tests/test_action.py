from unittest import TestCase
from preggy import expect

from pypeline.action import Action


class MyAction(Action):
    name = "My super action"


class ActionTestCase(TestCase):

    def test_my_action(self):
        act = MyAction()
        expect(act.name).to_equal("My super action")
        expect(act.forward({})).to_equal(None)
        expect(act.backward(None, {})).to_equal(None)
