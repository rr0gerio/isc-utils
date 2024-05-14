from setuptools import setup, find_packages

setup(
    name='access_profile_manager',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'certifi==2024.2.2',
        'charset-normalizer==2.0.12',
        'idna==3.7',
        'PyYAML==5.3.1',
        'requests==2.26.0',
        'tk==0.1.0',
        'urllib3==1.26.18'  
        # Adicione outras dependências aqui conforme necessário
    ],
    entry_points={
        'console_scripts': [
            'access-profile-manager = main:main'
        ]
    },
    author='Seu Nome',
    author_email='seu@email.com',
    description='Um gerenciador de perfis de acesso para IdentityNow',
    license='MIT',
    keywords='IdentityNow access-profile-manager',
    url='https://github.com/rr0gerio/access-profile-manager',
    project_urls={
        'Source': 'https://github.com/rr0gerio/access-profile-manager',
        'Documentation': 'https://github.com/rr0gerio/access-profile-manager/blob/main/README.md',
        'Tracker': 'https://github.com/rr0gerio/access-profile-manager/issues',
    },
)
