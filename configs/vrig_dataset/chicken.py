_base_ = "./hyper_default.py"

expname = "vrig/base-chicken"
basedir = "./logs/vrig_data"

data = dict(
    datadir="data/hypernerf/vrig-chicken",
    dataset_type="hyper_dataset",
    white_bkgd=False,
)
