from setuptools import setup

setup(
    name="grpc_testauth",
    version="0.6",
    packages=["grpc_testauth"],
    install_requires=["grpcio", "googleapis-common-protos"],
    zip_safe=False,
)
