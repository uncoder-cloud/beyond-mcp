from setuptools import setup, find_packages

setup(
    name='beyond-mcp',
    version='0.1.0',
    description='A test MCP project that provides a set of tools to boost programmer productivity.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'flake8',
    ],
    entry_points={
        'console_scripts': [
            'beyond-mcp=mcp_server.mcp_server:main',
        ],
    },
)
