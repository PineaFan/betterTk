import betterTk

class Main(betterTk.BetterTk):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.add_tab("Test")

        self.tabs["Test"].create_input("test", "Test", "Test", w="100%")
        self.tabs["Test"].create_input("test2", "Test", "Test2", type="button", on_click=self.test, y=50, w="100%")
        self.tabs["Main"].create_input("test3", "Test", type="check")

    def test(self):
        print("Test")


window = Main(geometry=(1920/2, 1080/2))
window.start()