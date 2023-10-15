Dataset **Pylon Components** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/S/D/VQ/zcrA71ILHX6h7kcAKxVrwPwo6bdknFPFFNpAYqWEmqPHU4LxYES9bXLP5ApnmULZfk4IdHkmg0azxAlcGixV6pZKIWqNoD7Tbw8WFOCdga0DSJXAzO6jYPy7uN1d.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Pylon Components', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [README.md](https://zenodo.org/record/4573988/files/README.md?download=1)
- [UAS_training_data.zip](https://zenodo.org/record/4573988/files/UAS_training_data.zip?download=1)
