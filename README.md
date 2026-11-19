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

## Latest list — 2026-11-19 07:22 UTC

New packages created between 2026-11-19 06:21 UTC and 2026-11-19 07:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T07-22-11-33277Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 06:42:03 | [XHao.Queue.V2](https://www.nuget.org/packages/XHao.Queue.V2) | 1.0.0 | XHao.Queue.V2 | Package Description |
| 2026-11-19 06:42:06 | [XHao.Queue.V2.RabbitMQ](https://www.nuget.org/packages/XHao.Queue.V2.RabbitMQ) | 1.0.0 | XHao.Queue.V2.RabbitMQ | Package Description |
| 2026-11-19 06:42:11 | [XHao.Queue.V2.Redis](https://www.nuget.org/packages/XHao.Queue.V2.Redis) | 1.0.0 | XHao.Queue.V2.Redis | Package Description |
| 2026-11-19 06:52:48 | [Emission](https://www.nuget.org/packages/Emission) | 1.0.0 | Ghost Notes LLC | A fluent API for programmatically generating C# source code. |
| 2026-11-19 06:55:08 | [Bielu.AspNetCore.Arazzo.Scalar.Aspire](https://www.nuget.org/packages/Bielu.AspNetCore.Arazzo.Scalar.Aspire) | 3.1.1 | Arkadiusz Biel | Aspire hosting helper that renders Arazzo workflows in a Scalar.Aspire API Refe… |
| 2026-11-19 07:12:22 | [Ranvier.Plume](https://www.nuget.org/packages/Ranvier.Plume) | 0.1.0 | shayanhabibi | The state of a text editor as a fold over a log of edits, on Ranvier: an immuta… |
| 2026-11-19 07:12:23 | [Ranvier.Plume.Traced](https://www.nuget.org/packages/Ranvier.Plume.Traced) | 0.1.0 | shayanhabibi | The state of a text editor as a fold over a log of edits, on Ranvier: an immuta… |
| 2026-11-19 07:12:24 | [Ranvier.Plume.View](https://www.nuget.org/packages/Ranvier.Plume.View) | 0.1.0 | shayanhabibi | The EditorView component of Ranvier.Plume for Ranvier.View: a virtualised text… |
| 2026-11-19 07:12:26 | [Ranvier.Plume.View.Traced](https://www.nuget.org/packages/Ranvier.Plume.View.Traced) | 0.1.0 | shayanhabibi | The EditorView component of Ranvier.Plume for Ranvier.View: a virtualised text… |
| 2026-11-19 07:12:37 | [PhoenixConcreteContractors.Estimator](https://www.nuget.org/packages/PhoenixConcreteContractors.Estimator) | 1.0.0 | Phoenix Concrete Contractors | Concrete contractors estimator for .NET: slab, driveway, footing, column and st… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
