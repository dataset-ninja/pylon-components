# https://zenodo.org/record/4573988

import os
import numpy as np
import supervisely as sly
from supervisely.io.fs import (
    get_file_name_with_ext,
    get_file_name,
    get_file_ext,
    file_exists,
    get_file_size,
)
import xml.etree.ElementTree as ET
from supervisely.io.json import load_json_file
from dotenv import load_dotenv


# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "pylon components"
dataset_path = "./APP_DATA/UAS_training_data"
batch_size = 30
ds_name = "ds"
images_ext = ".jpg"
ann_ext = ".txt"


def create_ann(image_path):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    bbox_path = image_path.split(".")[0] + ann_ext

    if file_exists(bbox_path):
        with open(bbox_path) as f:
            content = f.read().split("\n")

            for curr_data in content:
                if len(curr_data) != 0:
                    curr_data = list(map(float, curr_data.split(" ")))
                    obj_class = idx_to_class[int(curr_data[0])]

                    left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
                    right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
                    top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                    bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                    rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                    label = sly.Label(rectangle, obj_class)
                    labels.append(label)

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


obj_class_insolator = sly.ObjClass("insolator", sly.Rectangle)
obj_class_pylon = sly.ObjClass("pylon", sly.Rectangle)
obj_class_covered_insolator = sly.ObjClass("covered_insolator", sly.Rectangle)

idx_to_class = {
    0: obj_class_insolator,
    1: obj_class_pylon,
    2: obj_class_covered_insolator,
}

def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=list(idx_to_class.values()))
    api.project.update_meta(project.id, meta.to_json())

    images_names = [
        im_name for im_name in os.listdir(dataset_path) if get_file_ext(im_name) == images_ext
    ]

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [os.path.join(dataset_path, im_name) for im_name in img_names_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(img_names_batch))

    return project

