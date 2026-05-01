# 2026-04-24

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    contagem = courses["class"].value_counts()

    big_classes_series = contagem[contagem >= 5]

    big_classes = pd.DataFrame(big_classes_series.index, columns=["class"])

    return big_classes