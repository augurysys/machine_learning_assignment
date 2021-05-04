import setuptools

setup_config = {
    "name": 'gender_classification_pipeline',
    "description": 'Augury Machine Learning assignment - gender classification pipeline',
    "version": '1.0.0',
    "maintainer": 'Augury',
    "maintainer_email": 'info@augury.com',
    "packages": setuptools.find_packages(),
    "include_package_data": True,
    "package_data": {'': ['README.md'],
                     'gender_classification_pipeline': ['data/features.dat']},
    "install_requires": [
        "joblib==1.0.1",
        "protobuf==3.15.8",
    ],
}

setuptools.setup(**setup_config)