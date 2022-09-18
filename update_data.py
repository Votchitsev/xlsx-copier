import pandas as pd

class Updater:
    def __init__(self, source_file, target_files):
        self.source_file = source_file
        self.target_files = target_files

    def run(self):
        source_dataframe = self.read()
        self.write(source_dataframe)

    def read(self):
        dataframe = pd.read_excel(self.source_file)
        return dataframe.loc[dataframe['status'] == True]

    def write(self, dataframe):
        
        for file in self.target_files:
            dataframe.filter(items=['First name', 'Last name', 'e-mail']).to_excel(file, index=False)


