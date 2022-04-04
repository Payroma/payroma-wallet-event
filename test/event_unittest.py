import unittest
import event


class Color(event.EventForm):
    def __init__(self, name: str):
        self.events_listening()
        self.name = name

    def app_started_event(self):
        print("Current Color: %s" % self.name)

    def color_changed_event(self, name: str):
        self.name = name
        print("Color Changed: %s" % self.name)


# Create objects
color1 = Color('Red')
color2 = Color('Yellow')
color3 = Color('Blue')
color4 = Color('Black')
color5 = Color('White')


def function_name(text: str):
    print(f"\n[ + ] Start for: {text}")


class MyTestCase(unittest.TestCase):
    def test_app_started(self):
        function_name("test_app_started")

        # Notify to all listeners listening for appStarted event
        event.appStarted.notify()

        self.assertEqual(color1.name, 'Red')
        self.assertEqual(color2.name, 'Yellow')
        self.assertEqual(color3.name, 'Blue')
        self.assertEqual(color4.name, 'Black')
        self.assertEqual(color5.name, 'White')

    def test_color_changed(self):
        function_name("test_color_changed")

        # Notify to all listeners listening for colorChanged event
        # to change current color to ( Green ) color
        event.colorChanged.notify(name='Green')

        self.assertEqual(color1.name, 'Green')
        self.assertEqual(color2.name, 'Green')
        self.assertEqual(color3.name, 'Green')
        self.assertEqual(color4.name, 'Green')
        self.assertEqual(color5.name, 'Green')


if __name__ == '__main__':
    unittest.main()
