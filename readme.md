#  Odoo project using Odoo 14.0

This repository contains custom modules for [Odoo][] 14, focusing on employee data import and invoice management via API endpoints.

<details>
<!-- prettier-ignore-start -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<summary>Table of contents</summary>

- [Prerequisites and Modules](##prerequisites-and-modules)
- [How to run](##how-to-run)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- prettier-ignore-end -->
</details>

## Prerequisites and Modules

Require to install these tools to use:

- [Docker](https://docs.docker.com/)
- [python](https://www.python.org/) 3.8.1+
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) >= 2.0.0
- [Cerberus](https://docs.python-cerberus.org/) 
- [PyQueryString](https://pypi.org/project/pyquerystring/) 
- [Parse Accept Language](https://pypi.org/project/parse-accept-language/) 
- [Apispec](https://apispec.readthedocs.io/en/latest/) >= 4.0.0

I use existing Odoo modules :
<details>
<summary>For importing data in background process</summary>

- [Queue Job](https://github.com/OCA/queue/tree/14.0/queue_job)
- [Base Import Async](https://github.com/OCA/queue/tree/14.0/base_import_async)

</details>

<details>
<summary>For API endpoints and swagger</summary>

- [Component](https://github.com/OCA/server-tools/tree/14.0/component)
- [Base Rest](https://github.com/OCA/rest-framework)
- [Datamodel](https://github.com/OCA/rest-framework)
- [Base Rest Datamodel](https://github.com/OCA/rest-framework)
- [Auth API Key](https://github.com/OCA/server-auth)
- [Base Rest Auth API Key](https://github.com/OCA/rest-framework)

</details>

    
## How to run

1. Begin by cloning the repository to your local machine.
2. Move to the project directory.
```
cd learning-odoo
```
3. Build and install dependencies.
```
docker compose up --build
```
4. Run the program
```
docker compose up 
```

[odoo]: https://www.odoo.com/