import pandas as pd
import re

def column_names(file_path):
    with open(file_path, 'r') as fp:
        columns = []
        comment = True
        while comment:
            line = fp.readline()
            line_split = re.split(r'\s{2,}', line)
            if (line_split[0]!='#'):
                comment = False
            else:
                column = re.sub(r'^[0-9 ]+', '', line_split[1])
                columns.append(column)
    return columns

def read_sex(file_path):
    columns = column_names(file_path)
    df = pd.read_table(file_path, comment='#', header=None, sep=r'\s+', engine='python', index_col=0, names=columns)
    return df

if __name__ == "__main__":
    file_path = 'output/catR.cat'
    df = read_sex(file_path)
    print(df)
    