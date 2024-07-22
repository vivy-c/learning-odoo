#  Odoo project using Odoo 14.0

This repository contains custom modules for [Odoo][] 14, focusing on employee data import and invoice management via API endpoints.

<details>
<!-- prettier-ignore-start -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<summary>Table of contents</summary>

- [Prerequisites and Modules](#prerequisites-and-modules)
- [How to run](##how-to-run)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- prettier-ignore-end -->
</details>

## Prerequisites and Modules

Require to install these tools to use it:

- [Docker](https://docs.docker.com/)
- [python](https://www.python.org/) 3.8.1+

I use existing modules :

- [Queue Job](https://github.com/OCA/queue/tree/14.0/queue_job)
- [Base Import Async](https://github.com/OCA/queue/tree/14.0/base_import_async) 3.8.1+

## How to run

1. Begin by cloning the repository to your local machine.
2. Move to the project directory.
```
cd odoo-learning
```
3. Build and intall dependencies.
```
docker compose up --build
```
4. Run the program
```
docker compose up 
```

[odoo]: https://www.odoo.com/