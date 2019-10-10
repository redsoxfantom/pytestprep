from distutils.core import setup

setup(
    name="pytestprep",
    version="0.1",
    description="Parses Security+ docx test bank and quizzes the user",
    packages=['pytestprep'],
    install_requires=['python-docx']
)