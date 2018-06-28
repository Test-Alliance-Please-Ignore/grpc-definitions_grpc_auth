from setuptools import setup

setup(name='testauth_grpc',
    version='0.1',
    packages=['grpc_testauth'],
    install_requires = [
        'grpcio',
        'googleapis-common-protos'
    ],
    zip_safe = False
)