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

## Latest list — 2026-10-13 03:20 UTC

New packages created between 2026-10-13 02:21 UTC and 2026-10-13 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T03-20-07-597781Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 02:40:35 | [Meridian.Context](https://www.nuget.org/packages/Meridian.Context) | 1.0.0 | Angel Hernandez | Ambient execution context primitives shared across every Meridian subsystem. |
| 2026-10-13 02:41:00 | [Meridian.Knowledge](https://www.nuget.org/packages/Meridian.Knowledge) | 1.0.0 | Angel Hernandez | Embeddings, a pluggable semantic store, and retrieval (RAG) built on top of Mer… |
| 2026-10-13 02:41:08 | [Meridian.Agents](https://www.nuget.org/packages/Meridian.Agents) | 1.0.0 | Angel Hernandez | Agent construction, tools, memory and sequential/parallel workflows, built on t… |
| 2026-10-13 02:41:17 | [Meridian.Observability](https://www.nuget.org/packages/Meridian.Observability) | 1.0.0 | Angel Hernandez | Tracing (ActivitySource), metrics (Meter) and lightweight response evaluation s… |
| 2026-10-13 02:41:24 | [Meridian.Hosting](https://www.nuget.org/packages/Meridian.Hosting) | 1.0.0 | Angel Hernandez | The services.AddMeridian(...) front door: wires Models, Knowledge, Agents and O… |
| 2026-10-13 02:46:32 | [HcmIdentityProvisioning.Domain](https://www.nuget.org/packages/HcmIdentityProvisioning.Domain) | 1.1.0 | Mateus Ferreira | Enterprise Domain Models and Ports for HCM Identity Provisioning |
| 2026-10-13 02:46:33 | [HcmIdentityProvisioning.Application](https://www.nuget.org/packages/HcmIdentityProvisioning.Application) | 1.1.0 | Mateus Ferreira | Enterprise Application Use Cases and Services for HCM Identity Provisioning |
| 2026-10-13 02:46:37 | [HcmIdentityProvisioning](https://www.nuget.org/packages/HcmIdentityProvisioning) | 1.1.0 | Mateus Ferreira | Enterprise Microsoft Entra ID SCIM/HCM Provisioning & Reconciliation Engine |
| 2026-10-13 02:49:52 | [Hedgehog.MSTest](https://www.nuget.org/packages/Hedgehog.MSTest) | 1.0.0 | Andrii Chebukin, Alexey Raga | Hedgehog with convenience attributes for MSTest. - Test method arguments genera… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
