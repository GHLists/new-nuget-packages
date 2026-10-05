# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-05 04:20 UTC

New packages created between 2026-10-05 03:20 UTC and 2026-10-05 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T04-20-21-228594Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 04:01:46 | [Godex](https://www.nuget.org/packages/Godex) | 0.1.2 | altamkp | Extension library for Godot in C#. |
| 2026-10-05 04:01:47 | [Godex.Async](https://www.nuget.org/packages/Godex.Async) | 0.1.2 | altamkp | Asynchronous extension library for Godot in C#. |
| 2026-10-05 04:01:48 | [Godex.Hosting](https://www.nuget.org/packages/Godex.Hosting) | 0.1.2 | altamkp | Hosting extension library for Godot in C#. |
| 2026-10-05 04:07:09 | [Depa.Cozo](https://www.nuget.org/packages/Depa.Cozo) | 0.1.0 | Depa | Thin .NET binding for the Cozo native C API. |
| 2026-10-05 04:13:35 | [Depa.Datalog.Core](https://www.nuget.org/packages/Depa.Datalog.Core) | 0.1.0 | Depa | Portable Datalog parser, validator, normalized IR, and diagnostics. |
| 2026-10-05 04:13:37 | [Depa.Datalog.Cozo](https://www.nuget.org/packages/Depa.Datalog.Cozo) | 0.1.0 | Depa | CozoScript backend for Depa Datalog IR. |
| 2026-10-05 04:13:40 | [Depa.Ontology](https://www.nuget.org/packages/Depa.Ontology) | 0.1.0 | Depa | Depa object-model and ontology runtime. |
| 2026-10-05 04:13:42 | [Depa.Ontology.Portability.Yaml](https://www.nuget.org/packages/Depa.Ontology.Portability.Yaml) | 0.1.0 | Depa | Safe YAML adapter for Depa ontology behavior manifests. |
| 2026-10-05 04:13:44 | [Depa.Ontology.Scripting.Jint](https://www.nuget.org/packages/Depa.Ontology.Scripting.Jint) | 0.1.0 | Depa | Optional Jint adapter for Depa ontology callbacks. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
