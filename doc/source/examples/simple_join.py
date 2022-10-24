r"""
.. table:: ``main_df``
    :class: longtable

    =============== ========
    Fruit           ID Num
    =============== ========
    Banana          1
    Orange          2
    Apple           3
    =============== ========


.. table:: ``colour_df``
    :class: longtable

    =================== ========= ========
    Fruit               ID Num    Colour
    =================== ========= ========
    \                   1         Yellow
    Orange              \         Orange
    Apple               3         Red
    Apple               4         Green
    =================== ========= ========
"""
import numpy as np
import pandas as pd
from pandas import DataFrame

main_df = DataFrame(
    [
        ["Banana", 1],
        ["Orange", 2],
        ["Apple", 3],
    ],
    columns=["Fruit", "ID Num"],
)

colour_df = DataFrame(
    [
        [np.nan, 1, "Yellow"],
        ["Orange", np.nan, "Orange"],
        ["Apple", 3, "Red"],
        ["Apple", 4, "Green"],
    ],
    columns=["Fruit", "ID Num", "Colour"],
)

main_df["row_id"] = range(len(main_df))
name_join_df = main_df.merge(colour_df, how="inner", on="Fruit", suffixes=("", "_Name"))
name_join_df.drop(columns=["ID Num_Name"], inplace=True)

dupl_idx = name_join_df.duplicated(subset=main_df.columns, keep=False)
dupl_name_join_df = name_join_df.loc[dupl_idx]
one_name_join_df = name_join_df.loc[~dupl_idx]

main_dupl_idx = main_df.index.isin(dupl_name_join_df.index)
dupl_df = main_df.loc[main_dupl_idx]
no_name_join_df = main_df.loc[~main_dupl_idx]

id_dupl_join_df = dupl_df.merge(colour_df, how="inner", on=["Fruit", "ID Num"])
id_no_join_df = no_name_join_df.merge(
    colour_df, how="inner", on=["ID Num"], suffixes=("", "_ID")
)
id_no_join_df.drop(columns=["Fruit_ID"], inplace=True)

join_df = pd.concat([one_name_join_df, id_dupl_join_df, id_no_join_df], axis="index")
join_df.sort_values("row_id", inplace=True)
join_df.reset_index(drop=True, inplace=True)
join_df.drop(columns="row_id", inplace=True)
main_df.drop(columns="row_id", inplace=True)
