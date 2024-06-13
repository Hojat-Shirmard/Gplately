import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt

OUTPUT_DIR = "output"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

MODEL_REPO_DIR = "plate-model-repo"


def save_fig(filename):
    output_file = f"{OUTPUT_DIR}/{Path(filename).stem}.png"
    plt.gcf().savefig(output_file, dpi=120, bbox_inches="tight")  # transparent=True)
    print(f"Done! The {output_file} has been saved.")
    plt.close(plt.gcf())


def get_test_loca_code_flag():
    if "GPLATELY_TEST_LOCAL_FLAG" in os.environ and (
        os.environ["GPLATELY_TEST_LOCAL_FLAG"].lower() == "false"
        or os.environ["GPLATELY_TEST_LOCAL_FLAG"].lower() == "0"
    ):
        return False
    return True


if get_test_loca_code_flag():
    sys.path.insert(0, f"{os.path.dirname(os.path.realpath(__file__))}/../..")
