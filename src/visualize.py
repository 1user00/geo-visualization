import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from pathlib import Path
import sys
print(sys.executable)

# -----------------------------
# Путь к данным (относительный!)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "input" / "out_vectors.shp"
OUTPUT_PATH = "figures/vector_map.png"


def main():
    # 1. Загрузка данных
    gdf = gpd.read_file(DATA_PATH)

    # 2. Вычисление площади
    gdf["area"] = gdf.geometry.area

    # 3. Настройка визуализации
    fig, ax = plt.subplots(figsize=(12, 10))

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)

    # 4. Отрисовка карты
    gdf.plot(
        column="area",
        ax=ax,
        cax=cax,
        cmap="jet",
        legend=True,
        legend_kwds={"label": "Area of polygons"}
    )

    # 5. Границы
    gdf.boundary.plot(ax=ax, edgecolor="black", linewidth=0.5)

    ax.set_title("Vector Data Visualization")
    ax.set_xlabel("Eastings")
    ax.set_ylabel("Northings")

    plt.tight_layout()

    # создаём папку figures если её нет
    Path("figures").mkdir(exist_ok=True)

    plt.savefig(OUTPUT_PATH, dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
