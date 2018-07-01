from setuptools import setup

setup(name='grpc_testauth',
    version='0.2',
    packages=['grpc_testauth'],
    install_requires = [
        'grpcio',
        'googleapis-common-protos'
    ],
    zip_safe = False
)