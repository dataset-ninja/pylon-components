Dataset **Pylon Components** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEzMDlfUHlsb24gQ29tcG9uZW50cy9weWxvbi1jb21wb25lbnRzLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIjJPWHJMbm80VXBVZFhzSmVrLzYxSFd0UGdiK1llZFcvM21VMkcyMFNFeUk9In0=)

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
