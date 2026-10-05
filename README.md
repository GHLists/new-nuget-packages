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

## Latest list — 2026-10-05 21:21 UTC

New packages created between 2026-10-05 20:20 UTC and 2026-10-05 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T21-21-12-976861Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 20:20:50 | [Durable.InMemory](https://www.nuget.org/packages/Durable.InMemory) | 0.4.0 | jchristn,joshclopton | In-memory backend for Durable ORM: the reference IRepositoryBackend implementat… |
| 2026-10-05 20:20:52 | [Durable.Conformance](https://www.nuget.org/packages/Durable.Conformance) | 0.4.0 | jchristn,joshclopton | Conformance kit for Durable ORM backends. Implement IConformanceTarget for your… |
| 2026-10-05 20:27:05 | [AuthV4](https://www.nuget.org/packages/AuthV4) | 4.0.2 | Authris | Authris license client SDK |
| 2026-10-05 20:30:39 | [Archestack.Cli](https://www.nuget.org/packages/Archestack.Cli) | 1.0.1 | Archestack | Build, test, plan and deploy an Archestack repository from a pipeline: a throwa… |
| 2026-10-05 20:33:11 | [Bambi.Yarp.Ntlm](https://www.nuget.org/packages/Bambi.Yarp.Ntlm) | 2.3.0 | Bambi på hal is | Yarp.ReverseProxy extension that enables proxying connection-based Windows auth… |
| 2026-10-05 20:39:08 | [Crono.Licenciamiento](https://www.nuget.org/packages/Crono.Licenciamiento) | 1.0.0 | Eduardo Rojas Ochante | Verificador de licencias de los módulos de Crono. |
| 2026-10-05 21:10:02 | [Mathesis.Validation](https://www.nuget.org/packages/Mathesis.Validation) | 0.1.0 | Damien Gilbert | DataAnnotations validation attributes for mathematical input: exact numbers, ra… |
| 2026-10-05 21:10:41 | [Mathesis.Symbolics](https://www.nuget.org/packages/Mathesis.Symbolics) | 0.1.0 | Damien Gilbert | The Mathesis expression tree: parser, printers, normalizer, assumptions, patter… |
| 2026-10-05 21:11:08 | [Mathesis.Numerics](https://www.nuget.org/packages/Mathesis.Numerics) | 0.1.0 | Damien Gilbert | Numerical analysis for Mathesis: root finding, quadrature, differentiation, int… |
| 2026-10-05 21:11:45 | [Mathesis.LinearAlgebra](https://www.nuget.org/packages/Mathesis.LinearAlgebra) | 0.1.0 | Damien Gilbert | Dense vectors and matrices for Mathesis with exact row reduction, determinants… |
| 2026-10-05 21:12:04 | [dxCompany.Script](https://www.nuget.org/packages/dxCompany.Script) | 2026.10.5.1 | dxCompany | Write a dxScript: a C# file that runs on its own, in dxStudio, or under dxAgent… |
| 2026-10-05 21:12:09 | [Mathesis.Knowledge](https://www.nuget.org/packages/Mathesis.Knowledge) | 0.1.0 | Damien Gilbert | The Mathesis knowledge catalog: verified laws, formulas and theorems with their… |
| 2026-10-05 21:12:40 | [Mathesis.Core](https://www.nuget.org/packages/Mathesis.Core) | 0.1.0 | Damien Gilbert | Exact numbers (BigRational, complex, dual, interval), results with budgets and… |
| 2026-10-05 21:13:09 | [Mathesis](https://www.nuget.org/packages/Mathesis) | 0.1.0 | Damien Gilbert | A computer algebra library for .NET with step-by-step explanations: simplify, d… |
| 2026-10-05 21:13:55 | [ShotDetector.Cli](https://www.nuget.org/packages/ShotDetector.Cli) | 0.3.0 | Jakob Boman | shotdetect: shot/cut detection from the command line, with the same results as… |
| 2026-10-05 21:15:46 | [MessageLoop.Web.Common](https://www.nuget.org/packages/MessageLoop.Web.Common) | 1.0.0 | Daniil Dudin | Provides a set of controllers for managing long-running operations and custom m… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
