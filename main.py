import math

import numpy as np
import pandas as pd
import plotly.express as px
import typer
from plotly import graph_objs as go
from sklearn.model_selection import train_test_split

np.random.seed(42)


def main(r: float = 1.0, d: float = 0.2, laps: int = 3, viz: bool = False):
    std_noise = 0.25
    n_samples = int((np.square(laps * np.pi) * r) / (2.0 * d))

    # https://math.stackexchange.com/questions/2335055/placing-points-equidistantly-along-an-archimedean-spiral-from-parametric-equatio
    t = np.sqrt((2.0 * d * np.arange(1, n_samples + 1)) / r)
    x0 = r * t * np.cos(t)
    x1 = r * t * np.sin(t)

    # create mirrored groups
    y = np.concatenate([np.ones((n_samples,)), np.zeros((n_samples,))]).astype(np.int32)
    x0 = np.concatenate([x0, -x0], axis=0)
    x1 = np.concatenate([x1, -x1], axis=0)

    # add noise
    x0 += np.random.normal(scale=std_noise, size=x0.shape)
    x1 += np.random.normal(scale=std_noise, size=x1.shape)

    # save data
    df = pd.DataFrame(dict(x0=x0, x1=x1, y=y))

    df_train, df_test = train_test_split(df, train_size=0.9, shuffle=True)

    df_train.to_csv("training-set.csv", index=False)
    df_test.to_csv("test-set.csv", index=False)

    print(df_train.shape, df_train.dtypes)
    print(df_test.shape, df_test.dtypes)

    if viz:
        (
            go.Figure(
                [
                    go.Scatter(
                        x=df_train.x0,
                        y=df_train.x1,
                        marker=go.scatter.Marker(
                            color=df_train.y,
                            # size=sizes,
                            line_width=1,
                            line_color="DarkSlateGrey",
                            # opacity=opacity,
                        ),
                        mode="markers",
                    ),
                    go.Scatter(
                        x=df_test.x0,
                        y=df_test.x1,
                        marker=go.scatter.Marker(
                            color=df_test.y,
                            # size=sizes,
                            line_width=1,
                            line_color="DarkSlateGrey",
                            # opacity=opacity,
                        ),
                        mode="markers",
                    ),
                ]
            )
            .update_layout(
                template="simple_white",
                yaxis=dict(scaleanchor="x", scaleratio=1),
                title=f"N = {len(df)}",
            )
            .show()
        )


if __name__ == "__main__":
    typer.run(main)
