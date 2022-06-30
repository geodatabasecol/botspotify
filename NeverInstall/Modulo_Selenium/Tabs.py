class tabcontrol:
    def __init__(self,driver):
        self.count_Tabs=0
        self.main_Tab=0
        self.vscode_Tab=1
        self.driver=driver

    def countTabs(self):
        self.count_Tabs=  self.driver.window_handles
        return self.count_Tabs
        
    def switch_to_mainTab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def switch_to_vscodeTab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
